from fastapi import Depends, FastAPI, HTTPException
from redis import Redis
from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.agent_service.app.dependencies import get_redis
from backend.agent_service.app.model_provider import OpenAICompatibleProvider
from backend.agent_service.app.ontology_client import OntologyApiClient
from backend.agent_service.app.routers.agents import router as agents_router
from backend.agent_service.app.routers.sessions import router as sessions_router
from backend.agent_service.app.routers.tools import router as tools_router
from backend.agent_service.app.routers.messages import router as messages_router
from backend.agent_service.app.routers.runtime import router as runtime_router
from backend.ontology_service.app.config import Settings, get_settings
from backend.ontology_service.app.database import get_db


def create_app(settings: Settings | None = None) -> FastAPI:
    active_settings = settings or get_settings()
    app = FastAPI(title="Ontology Agent 运行服务", version="0.1.0")
    app.state.settings = active_settings
    app.state.redis = Redis.from_url(active_settings.redis_url, decode_responses=True)
    app.state.ontology_client = OntologyApiClient(active_settings.ontology_api_url)
    model_key = active_settings.agent_model_api_key.get_secret_value().strip()
    app.state.agent_model_provider = (
        OpenAICompatibleProvider(
            base_url=active_settings.agent_model_base_url,
            api_key=model_key,
            timeout_seconds=active_settings.agent_model_timeout_seconds,
        )
        if active_settings.agent_model_base_url.strip() and model_key
        else None
    )
    app.include_router(agents_router)
    app.include_router(sessions_router)
    app.include_router(tools_router)
    app.include_router(messages_router)
    app.include_router(runtime_router)

    @app.get("/health/live", tags=["健康检查"])
    def live() -> dict[str, str]:
        return {"status": "正常"}

    @app.get("/health/ready", tags=["健康检查"])
    def ready(
        session: Session = Depends(get_db),
        redis_client=Depends(get_redis),
    ) -> dict[str, str]:
        try:
            session.execute(text("SELECT 1"))
            redis_client.ping()
        except Exception as exc:
            raise HTTPException(status_code=503, detail="Agent 服务依赖暂不可用：PostgreSQL 或 Redis") from exc
        return {"status": "就绪"}

    return app


app = create_app()
