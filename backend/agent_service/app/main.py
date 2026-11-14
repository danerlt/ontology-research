from fastapi import Depends, FastAPI, HTTPException
from redis import Redis
from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.agent_service.app.dependencies import get_redis
from backend.agent_service.app.ontology_client import OntologyApiClient
from backend.agent_service.app.routers.agents import router as agents_router
from backend.agent_service.app.routers.sessions import router as sessions_router
from backend.agent_service.app.routers.tools import router as tools_router
from backend.ontology_service.app.config import Settings, get_settings
from backend.ontology_service.app.database import get_db


def create_app(settings: Settings | None = None) -> FastAPI:
    active_settings = settings or get_settings()
    app = FastAPI(title="Ontology Agent 运行服务", version="0.1.0")
    app.state.settings = active_settings
    app.state.redis = Redis.from_url(active_settings.redis_url, decode_responses=True)
    app.state.ontology_client = OntologyApiClient(active_settings.ontology_api_url)
    app.include_router(agents_router)
    app.include_router(sessions_router)
    app.include_router(tools_router)

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
