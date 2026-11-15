import re
from datetime import datetime, timezone
from typing import Annotated, Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from backend.agent_service.app.dependencies import RedisClient
from backend.agent_service.app.event_store import append_event
from backend.agent_service.app.schemas import (
    AgentConfiguration,
    AgentCreate,
    AgentDraftUpdate,
    AgentInputDefinition,
    AgentPreviewRequest,
    AgentPreviewResponse,
    AgentResponse,
    AgentSessionCreate,
    AgentSessionListResponse,
    AgentSessionResponse,
    AgentVersionResponse,
)
from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import AgentDefinition, AgentSession, AgentVersion
from backend.ontology_service.app.security import Actor, get_current_user, require_role

router = APIRouter(prefix="/api/agents", tags=["Agent 管理"])
KNOWN_TOOLS = {"search_objects", "get_object", "execute_action"}
PLACEHOLDER_PATTERN = re.compile(r"\{\{\s*([a-z][a-z0-9_]*)\s*\}\}")


@router.get("", response_model=list[AgentResponse])
def list_agents(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> list[AgentResponse]:
    agents = session.scalars(
        select(AgentDefinition)
        .options(selectinload(AgentDefinition.versions))
        .order_by(AgentDefinition.display_name)
    ).all()
    return [_agent_response(agent) for agent in agents]


@router.post("", response_model=AgentResponse, status_code=status.HTTP_201_CREATED)
def create_agent(
    body: AgentCreate,
    actor: Annotated[Actor, Depends(require_role("admin"))],
    session: Annotated[Session, Depends(get_db)],
) -> AgentResponse:
    duplicate = session.scalar(select(AgentDefinition.id).where(AgentDefinition.api_name == body.api_name))
    if duplicate is not None:
        raise HTTPException(status_code=409, detail="Agent API 名已存在")

    config = body.draft_config or AgentConfiguration(
        model_provider="local",
        model_name="确定性本地预览",
        system_prompt=body.description or f"你是{body.display_name}。",
        allowed_tools=body.allowed_tools,
        allowed_actions=body.allowed_actions,
    )
    agent = AgentDefinition(
        project_id=UUID(actor.project_id),
        api_name=body.api_name,
        display_name=body.display_name,
        description=body.description,
        allowed_tools=config.allowed_tools,
        allowed_actions=config.allowed_actions,
        draft_config=config.model_dump(mode="json"),
    )
    session.add(agent)
    session.commit()
    session.refresh(agent)
    return _agent_response(agent)


@router.get("/{agent_id}", response_model=AgentResponse)
def get_agent(
    agent_id: UUID,
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> AgentResponse:
    agent = _get_agent(session, agent_id)
    return _agent_response(agent)


@router.put("/{agent_id}", response_model=AgentResponse)
def update_agent_draft(
    agent_id: UUID,
    body: AgentDraftUpdate,
    _actor: Annotated[Actor, Depends(require_role("admin"))],
    session: Annotated[Session, Depends(get_db)],
) -> AgentResponse:
    agent = _get_agent(session, agent_id)
    config = body.draft_config
    agent.draft_config = config.model_dump(mode="json")
    agent.allowed_tools = config.allowed_tools
    agent.allowed_actions = config.allowed_actions
    session.commit()
    session.refresh(agent)
    return _agent_response(agent)


@router.get("/{agent_id}/versions", response_model=list[AgentVersionResponse])
def list_agent_versions(
    agent_id: UUID,
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> list[AgentVersionResponse]:
    _get_agent(session, agent_id)
    versions = session.scalars(
        select(AgentVersion)
        .where(AgentVersion.agent_id == agent_id)
        .order_by(AgentVersion.version_number.desc())
    ).all()
    return [_version_response(version) for version in versions]


@router.post("/{agent_id}/publish", response_model=AgentVersionResponse, status_code=status.HTTP_201_CREATED)
def publish_agent(
    agent_id: UUID,
    actor: Annotated[Actor, Depends(require_role("admin"))],
    session: Annotated[Session, Depends(get_db)],
) -> AgentVersionResponse:
    agent = _get_agent(session, agent_id)
    config = AgentConfiguration.model_validate(agent.draft_config)
    if not config.system_prompt.strip():
        raise HTTPException(status_code=422, detail="发布前必须填写系统提示词")
    _validate_template_references(config)
    latest_number = session.scalar(
        select(func.max(AgentVersion.version_number)).where(AgentVersion.agent_id == agent.id)
    ) or 0
    version = AgentVersion(
        agent_id=agent.id,
        version_number=latest_number + 1,
        config=config.model_dump(mode="json"),
        created_by=UUID(actor.id),
        published_at=datetime.now(timezone.utc),
    )
    session.add(version)
    session.commit()
    session.refresh(version)
    return _version_response(version)


@router.post("/{agent_id}/preview", response_model=AgentPreviewResponse)
def preview_agent(
    agent_id: UUID,
    body: AgentPreviewRequest,
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> AgentPreviewResponse:
    agent = _get_agent(session, agent_id)
    config = AgentConfiguration.model_validate(agent.draft_config)
    _validate_inputs(config.inputs, body.inputs)
    _validate_template_references(config)
    variables = _evaluate_variables(config, body.inputs)
    values = _safe_template_values(config, body.inputs, variables)
    rendered_prompt = _render(config.system_prompt, values)
    if config.initial_user_message:
        rendered_prompt += "\n\n初始用户消息：" + _render(config.initial_user_message, values)
    return AgentPreviewResponse(
        mode="deterministic_dry_run",
        model_provider=config.model_provider,
        model_name=config.model_name,
        rendered_prompt=rendered_prompt,
        initial_user_message=_render(config.initial_user_message, values),
        variables=[
            {
                "name": variable.name,
                "expression": variable.expression,
                "status": "本地预览已解析",
                "value": _preview_value(variables.get(variable.name)),
            }
            for variable in config.precomputed_variables
        ],
        allowed_tools=config.allowed_tools,
        allowed_actions=config.allowed_actions,
        notices=["这是确定性本地预览；未调用模型、工具或 Ontology Action。"],
    )


@router.post(
    "/{agent_id}/sessions", response_model=AgentSessionResponse, status_code=status.HTTP_201_CREATED
)
def create_agent_session(
    agent_id: UUID,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    redis_client: RedisClient,
    body: AgentSessionCreate = AgentSessionCreate(),
) -> AgentSessionResponse:
    agent = _get_agent(session, agent_id)
    if not agent.enabled:
        raise HTTPException(status_code=409, detail="Agent 已停用")
    version_query = select(AgentVersion).where(AgentVersion.agent_id == agent.id)
    if body.version_number is None:
        version_query = version_query.order_by(AgentVersion.version_number.desc()).limit(1)
    else:
        version_query = version_query.where(AgentVersion.version_number == body.version_number)
    version = session.scalar(version_query)
    if version is None:
        if body.version_number is None:
            raise HTTPException(status_code=409, detail="Agent 尚无已发布版本，请先保存并发布")
        raise HTTPException(status_code=404, detail="指定的 Agent 发布版本不存在")
    config = AgentConfiguration.model_validate(version.config)
    _validate_inputs(config.inputs, body.inputs)

    agent_session = AgentSession(
        agent_id=agent.id,
        agent_version_id=version.id,
        actor_id=UUID(actor.id),
        input_values=body.inputs,
        origin_resource=body.origin_resource,
        status="active",
    )
    session.add(agent_session)
    session.commit()
    session.refresh(agent_session)
    agent_session.version = version
    try:
        redis_client.set(f"agent:session:{agent_session.id}:status", "active", ex=86400)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Redis 会话存储暂不可用") from exc
    append_event(
        session,
        redis_client,
        agent_session.id,
        event_type="session.created",
        status="succeeded",
        details={
            "version_number": version.version_number,
            "origin_resource": body.origin_resource,
            "input_names": sorted(body.inputs),
        },
    )
    return _session_response(agent_session)


def _get_agent(session: Session, agent_id: UUID) -> AgentDefinition:
    agent = session.scalar(
        select(AgentDefinition).where(AgentDefinition.id == agent_id).options(selectinload(AgentDefinition.versions))
    )
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent 不存在")
    return agent


def _agent_response(agent: AgentDefinition) -> AgentResponse:
    latest_version_number = max((item.version_number for item in agent.versions), default=None)
    return AgentResponse(
        id=agent.id,
        api_name=agent.api_name,
        display_name=agent.display_name,
        description=agent.description,
        allowed_tools=agent.allowed_tools,
        allowed_actions=agent.allowed_actions,
        enabled=agent.enabled,
        draft_config=agent.draft_config,
        latest_version_number=latest_version_number,
    )


def _version_response(version: AgentVersion) -> AgentVersionResponse:
    return AgentVersionResponse(
        id=version.id,
        agent_id=version.agent_id,
        version_number=version.version_number,
        config=version.config,
        created_by=version.created_by,
        published_at=version.published_at,
    )


def _session_response(agent_session: AgentSession) -> AgentSessionResponse:
    config = AgentConfiguration.model_validate(agent_session.version.config)
    return AgentSessionResponse(
        id=agent_session.id,
        agent_id=agent_session.agent_id,
        agent_version_id=agent_session.agent_version_id,
        version_number=agent_session.version.version_number,
        status=agent_session.status,
        inputs=_visible_inputs(config.inputs, agent_session.input_values),
        origin_resource=agent_session.origin_resource,
        created_at=agent_session.created_at,
        closed_at=agent_session.closed_at,
    )


def _validate_inputs(definitions: list[AgentInputDefinition], values: dict[str, Any]) -> None:
    by_name = {item.name: item for item in definitions}
    unknown = set(values) - set(by_name)
    if unknown:
        raise HTTPException(status_code=422, detail=f"不支持的 Agent 输入：{', '.join(sorted(unknown))}")
    for definition in definitions:
        if definition.required and definition.name not in values:
            raise HTTPException(status_code=422, detail=f"缺少必填 Agent 输入：{definition.display_name}")
        if definition.name not in values:
            continue
        value = values[definition.name]
        if value is None or (definition.required and isinstance(value, str) and not value.strip()):
            raise HTTPException(status_code=422, detail=f"Agent 输入不能为空：{definition.display_name}")
        valid = {
            "string": isinstance(value, str),
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
            "integer": isinstance(value, int) and not isinstance(value, bool),
            "boolean": isinstance(value, bool),
        }[definition.type]
        if not valid:
            raise HTTPException(status_code=422, detail=f"Agent 输入类型不匹配：{definition.display_name}")


def _validate_template_references(config: AgentConfiguration) -> None:
    declared = {item.name for item in config.inputs} | {item.name for item in config.precomputed_variables}
    prompt = f"{config.system_prompt}\n{config.initial_user_message}"
    unknown = sorted({name for name in PLACEHOLDER_PATTERN.findall(prompt) if name not in declared})
    if unknown:
        raise HTTPException(status_code=422, detail=f"提示词引用了未声明的输入或变量：{', '.join(unknown)}")


def _evaluate_variables(config: AgentConfiguration, inputs: dict[str, Any]) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for variable in config.precomputed_variables:
        expression = variable.expression.strip()
        if expression.startswith("input."):
            input_name = expression.removeprefix("input.")
            if input_name not in {item.name for item in config.inputs}:
                raise HTTPException(status_code=422, detail=f"变量引用了未声明的输入：{input_name}")
            values[variable.name] = inputs.get(input_name)
        elif expression.startswith("variable."):
            source_name = expression.removeprefix("variable.")
            if source_name not in values:
                raise HTTPException(status_code=422, detail=f"变量只能引用之前定义的变量：{source_name}")
            values[variable.name] = values[source_name]
        elif expression.startswith("literal:"):
            values[variable.name] = expression.removeprefix("literal:")
        else:
            raise HTTPException(status_code=422, detail=f"本地预览不支持此变量表达式：{variable.name}")
    return values


def _safe_template_values(
    config: AgentConfiguration, inputs: dict[str, Any], variables: dict[str, Any]
) -> dict[str, Any]:
    sensitive_names = {item.name for item in config.inputs if item.sensitive}
    values = {**inputs, **variables}
    return {name: ("[已遮蔽]" if name in sensitive_names else value) for name, value in values.items()}


def _render(template: str, values: dict[str, Any]) -> str:
    return PLACEHOLDER_PATTERN.sub(
        lambda match: str(values.get(match.group(1), "[未提供]")), template
    )


def _preview_value(value: Any) -> str:
    if value is None:
        return "[未提供]"
    if isinstance(value, (dict, list)):
        return str(value)
    return str(value)


def _visible_inputs(definitions: list[AgentInputDefinition], values: dict[str, Any]) -> dict[str, Any]:
    sensitive_names = {item.name for item in definitions if item.sensitive}
    return {
        name: ("[已遮蔽]" if name in sensitive_names else value)
        for name, value in values.items()
    }
