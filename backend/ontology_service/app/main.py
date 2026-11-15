from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.ontology_service.app.config import Settings, get_settings
from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.routers.auth import router as auth_router
from backend.ontology_service.app.routers.actions import router as actions_router
from backend.ontology_service.app.routers.audit import router as audit_router
from backend.ontology_service.app.routers.branches import router as branches_router
from backend.ontology_service.app.routers.data_sources import router as data_sources_router
from backend.ontology_service.app.routers.ontology import router as ontology_router
from backend.ontology_service.app.routers.objects import router as objects_router
from backend.ontology_service.app.routers.proposals import router as proposals_router


def create_app(settings: Settings | None = None) -> FastAPI:
    app = FastAPI(title="本体管理 API", version="0.1.0")
    app.state.settings = settings or get_settings()
    app.include_router(auth_router)
    app.include_router(actions_router)
    app.include_router(audit_router)
    app.include_router(branches_router)
    app.include_router(data_sources_router)
    app.include_router(ontology_router)
    app.include_router(objects_router)
    app.include_router(proposals_router)

    @app.get("/health/live", tags=["健康检查"])
    def live() -> dict[str, str]:
        return {"status": "正常"}

    @app.get("/health/ready", tags=["健康检查"])
    def ready(session: Session = Depends(get_db)) -> dict[str, str]:
        try:
            session.execute(text("SELECT 1"))
        except Exception as exc:
            raise HTTPException(status_code=503, detail="数据库暂不可用") from exc
        return {"status": "就绪"}

    return app


app = create_app()
