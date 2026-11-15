from typing import Annotated, Any

from fastapi import APIRouter, Depends, Request

from backend.agent_service.app.dependencies import get_agent_model_provider
from backend.agent_service.app.model_provider import AgentModelProvider
from backend.ontology_service.app.security import Actor, get_current_user

router = APIRouter(prefix="/api/agent-runtime", tags=["智能体运行时"])


@router.get("/capabilities")
def runtime_capabilities(
    _actor: Annotated[Actor, Depends(get_current_user)],
    request: Request,
    provider: Annotated[AgentModelProvider | None, Depends(get_agent_model_provider)],
) -> dict[str, Any]:
    settings = request.app.state.settings
    return {
        "providers": [
            {
                "id": "local",
                "display_name": "本地确定性预览",
                "available": True,
                "model_name": "确定性本地预览",
                "credential_source": "无需外部凭据",
            },
            {
                "id": "openai-compatible",
                "display_name": "OpenAI 兼容接口",
                "available": provider is not None,
                "model_name": settings.agent_model_default_name,
                "credential_source": "服务端环境配置" if provider is not None else "尚未配置服务端地址与密钥",
            },
        ]
    }
