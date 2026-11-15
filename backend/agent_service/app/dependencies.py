from typing import Annotated

import httpx
import redis
from fastapi import Depends, Request

from backend.agent_service.app.ontology_client import OntologyApiClient
from backend.agent_service.app.model_provider import AgentModelProvider


def get_redis(request: Request) -> redis.Redis:
    return request.app.state.redis


def get_ontology_client(request: Request) -> OntologyApiClient:
    return request.app.state.ontology_client


def get_agent_model_provider(request: Request) -> AgentModelProvider | None:
    return request.app.state.agent_model_provider


RedisClient = Annotated[redis.Redis, Depends(get_redis)]
OntologyClient = Annotated[OntologyApiClient, Depends(get_ontology_client)]


def bearer_token(request: Request) -> str:
    authorization = request.headers.get("Authorization", "")
    prefix = "Bearer "
    if not authorization.startswith(prefix):
        return ""
    return authorization[len(prefix) :]
