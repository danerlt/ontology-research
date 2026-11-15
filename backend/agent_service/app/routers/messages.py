import json
from typing import Annotated, Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.agent_service.app.dependencies import (
    OntologyClient,
    RedisClient,
    bearer_token,
    get_agent_model_provider,
)
from backend.agent_service.app.event_store import append_event
from backend.agent_service.app.model_provider import AgentModelProvider, ModelProviderError
from backend.agent_service.app.routers.agents import (
    _evaluate_variables,
    _render,
    _safe_template_values,
)
from backend.agent_service.app.routers.sessions import _get_accessible_session
from backend.agent_service.app.routers.tools import invoke_session_tool
from backend.agent_service.app.schemas import (
    AgentConfiguration,
    AgentMessageRequest,
    AgentMessageResponse,
)
from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import AgentEvent, AgentSession
from backend.ontology_service.app.security import Actor, get_current_user

router = APIRouter(prefix="/api/sessions", tags=["Agent 对话运行"])
MAX_MODEL_ROUNDS = 4
MAX_TOOL_CALLS_PER_ROUND = 8


@router.post("/{session_id}/messages", response_model=AgentMessageResponse)
def send_message(
    session_id: UUID,
    body: AgentMessageRequest,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    redis_client: RedisClient,
    ontology_client: OntologyClient,
    token: Annotated[str, Depends(bearer_token)],
    provider: Annotated[AgentModelProvider | None, Depends(get_agent_model_provider)],
) -> AgentMessageResponse:
    agent_session = _get_accessible_session(session, session_id, actor)
    if agent_session.status != "active":
        raise HTTPException(status_code=409, detail="Agent 会话已结束")
    config = AgentConfiguration.model_validate(agent_session.version.config)
    if config.model_provider != "openai-compatible" or provider is None:
        append_event(
            session,
            redis_client,
            agent_session.id,
            event_type="model.unavailable",
            status="failed",
            details={"reason": "服务端未配置此模型运行时"},
        )
        raise HTTPException(status_code=409, detail="服务端尚未配置所选模型运行时")

    values = _safe_template_values(
        config,
        agent_session.input_values,
        _evaluate_variables(config, agent_session.input_values),
    )
    prompt = _render(config.system_prompt, values)
    initial_message = _render(config.initial_user_message, values)
    previous_turns = session.scalars(
        select(AgentEvent)
        .where(AgentEvent.session_id == agent_session.id)
        .order_by(AgentEvent.sequence)
    ).all()
    has_user_turn = any(event.event_type in {"message.initial", "message.user"} for event in previous_turns)
    if not has_user_turn and initial_message:
        append_event(
            session,
            redis_client,
            agent_session.id,
            event_type="message.initial",
            status="succeeded",
            details={"content": initial_message},
        )
    content = body.content.strip()
    if not content and not initial_message:
        raise HTTPException(status_code=422, detail="请输入会话消息，或先配置初始用户消息")
    if content:
        append_event(
            session,
            redis_client,
            agent_session.id,
            event_type="message.user",
            status="succeeded",
            details={"content": content},
        )

    events = session.scalars(
        select(AgentEvent)
        .where(AgentEvent.session_id == agent_session.id)
        .order_by(AgentEvent.sequence)
    ).all()
    messages = [{"role": "system", "content": prompt}]
    messages.extend(_conversation_messages(events))
    available_tools = _tool_definitions(config)
    executed_tools: list[str] = []
    latest_response: dict[str, Any] = {}

    for _ in range(MAX_MODEL_ROUNDS):
        try:
            latest_response = provider.complete(
                model=config.model_name,
                messages=messages,
                tools=available_tools,
            )
        except ModelProviderError as exc:
            append_event(
                session,
                redis_client,
                agent_session.id,
                event_type="model.failed",
                status="failed",
                details={"error": str(exc)},
            )
            raise HTTPException(status_code=502, detail=str(exc)) from exc
        except Exception as exc:
            append_event(
                session,
                redis_client,
                agent_session.id,
                event_type="model.failed",
                status="failed",
                details={"error": "模型运行时调用失败"},
            )
            raise HTTPException(status_code=502, detail="模型运行时调用失败") from exc

        model_message = latest_response.get("message")
        if not isinstance(model_message, dict):
            raise HTTPException(status_code=502, detail="模型服务未返回有效消息")
        tool_calls = model_message.get("tool_calls") or []
        request_id = latest_response.get("request_id")
        append_event(
            session,
            redis_client,
            agent_session.id,
            event_type="model.completed",
            status="succeeded",
            details={
                "provider": config.model_provider,
                "model": latest_response.get("model", config.model_name),
                "request_id": request_id,
                "usage": latest_response.get("usage") or {},
            },
        )
        if not tool_calls:
            assistant_message = model_message.get("content")
            if not isinstance(assistant_message, str) or not assistant_message.strip():
                raise HTTPException(status_code=502, detail="模型服务没有返回文本或工具调用")
            append_event(
                session,
                redis_client,
                agent_session.id,
                event_type="message.assistant",
                status="succeeded",
                details={"content": assistant_message, "request_id": request_id},
            )
            return AgentMessageResponse(
                session_id=agent_session.id,
                assistant_message=assistant_message,
                tool_calls=executed_tools,
                status=agent_session.status,
            )

        if len(tool_calls) > MAX_TOOL_CALLS_PER_ROUND:
            append_event(
                session,
                redis_client,
                agent_session.id,
                event_type="model.tool_limit",
                status="failed",
                details={"limit": MAX_TOOL_CALLS_PER_ROUND},
            )
            raise HTTPException(status_code=422, detail="单轮工具调用数量超过安全限制")
        assistant_call_message = {
            "role": "assistant",
            "content": model_message.get("content"),
            "tool_calls": tool_calls,
        }
        append_event(
            session,
            redis_client,
            agent_session.id,
            event_type="model.tool_calls",
            status="succeeded",
            details={"tool_calls": tool_calls, "request_id": request_id},
        )
        messages.append(assistant_call_message)
        for tool_call in tool_calls:
            function = tool_call.get("function") if isinstance(tool_call, dict) else None
            call_id = tool_call.get("id") if isinstance(tool_call, dict) else None
            name = function.get("name") if isinstance(function, dict) else None
            raw_arguments = function.get("arguments", "{}") if isinstance(function, dict) else "{}"
            try:
                if not isinstance(name, str) or not isinstance(raw_arguments, str):
                    raise ValueError("模型返回了无效工具名称或参数")
                arguments = json.loads(raw_arguments)
                if not isinstance(arguments, dict):
                    raise ValueError("模型工具参数必须是 JSON 对象")
                result = invoke_session_tool(
                    session,
                    redis_client,
                    ontology_client,
                    token,
                    actor,
                    agent_session,
                    name,
                    arguments,
                    str(call_id) if call_id else None,
                )
                executed_tools.append(name)
                tool_content = json.dumps(result, ensure_ascii=False, default=str)
            except ValueError as exc:
                append_event(
                    session,
                    redis_client,
                    agent_session.id,
                    event_type="tool.called",
                    tool_name=name if isinstance(name, str) else None,
                    status="failed",
                    details={"error": str(exc)},
                )
                tool_content = json.dumps({"error": str(exc)}, ensure_ascii=False)
            except HTTPException as exc:
                if exc.status_code >= 500:
                    raise
                tool_content = json.dumps(
                    {"error": exc.detail, "status_code": exc.status_code}, ensure_ascii=False
                )
            messages.append({
                "role": "tool",
                "tool_call_id": str(call_id or ""),
                "content": tool_content,
            })
    append_event(
        session,
        redis_client,
        agent_session.id,
        event_type="model.round_limit",
        status="failed",
        details={"limit": MAX_MODEL_ROUNDS},
    )
    raise HTTPException(status_code=502, detail="Agent 达到单轮工具调用次数限制，请缩小任务后重试")


def _conversation_messages(events: list[AgentEvent]) -> list[dict[str, Any]]:
    messages: list[dict[str, Any]] = []
    for event in events:
        details = event.details
        if event.event_type in {"message.initial", "message.user"}:
            messages.append({"role": "user", "content": details.get("content", "")})
        elif event.event_type == "message.assistant":
            messages.append({"role": "assistant", "content": details.get("content", "")})
        elif event.event_type == "model.tool_calls":
            messages.append({
                "role": "assistant",
                "content": None,
                "tool_calls": details.get("tool_calls", []),
            })
        elif event.event_type == "tool.called" and details.get("tool_call_id"):
            messages.append({
                "role": "tool",
                "tool_call_id": details["tool_call_id"],
                "content": json.dumps(details.get("result"), ensure_ascii=False, default=str),
            })
    return messages


def _tool_definitions(config: AgentConfiguration) -> list[dict[str, Any]]:
    definitions = {
        "search_objects": {
            "name": "search_objects",
            "description": "按本体对象类型、主键或名称搜索当前用户有权查看的记录。",
            "parameters": {
                "type": "object",
                "properties": {
                    "ontology_id": {"type": "string"},
                    "object_type_api_name": {"type": "string"},
                    "query": {"type": "string"},
                    "page": {"type": "integer", "minimum": 1},
                    "page_size": {"type": "integer", "minimum": 1, "maximum": 100},
                },
                "additionalProperties": False,
            },
        },
        "get_object": {
            "name": "get_object",
            "description": "按对象记录 ID 读取当前用户有权查看的对象和链接。",
            "parameters": {
                "type": "object",
                "properties": {"object_id": {"type": "string"}},
                "required": ["object_id"],
                "additionalProperties": False,
            },
        },
        "execute_action": {
            "name": "execute_action",
            "description": "在 Agent、当前用户和 Ontology API 三重授权通过后执行一个已配置 Action。",
            "parameters": {
                "type": "object",
                "properties": {
                    "action_api_name": {"type": "string", "enum": config.allowed_actions},
                    "object_id": {"type": "string"},
                    "expected_version": {"type": "integer", "minimum": 1},
                    "parameters": {"type": "object", "additionalProperties": True},
                },
                "required": ["action_api_name", "object_id", "expected_version", "parameters"],
                "additionalProperties": False,
            },
        },
    }
    return [
        {"type": "function", "function": definitions[name]}
        for name in config.allowed_tools
        if name in definitions and (name != "execute_action" or config.allowed_actions)
    ]
