from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class AgentCreate(BaseModel):
    api_name: str = Field(min_length=2, max_length=80, pattern=r"^[a-z][a-z0-9_]*$")
    display_name: str = Field(min_length=1, max_length=160)
    description: str = Field(default="", max_length=2000)
    allowed_tools: list[str] = Field(min_length=1)
    allowed_actions: list[str] = Field(default_factory=list)


class AgentResponse(BaseModel):
    id: UUID
    api_name: str
    display_name: str
    description: str
    allowed_tools: list[str]
    allowed_actions: list[str]
    enabled: bool


class AgentSessionResponse(BaseModel):
    id: UUID
    agent_id: UUID
    status: str
    created_at: datetime
    closed_at: datetime | None


class ToolCallRequest(BaseModel):
    arguments: dict[str, Any] = Field(default_factory=dict)


class ToolCallResponse(BaseModel):
    session_id: UUID
    tool_name: str
    status: str
    result: Any


class AgentEventResponse(BaseModel):
    id: UUID
    sequence: int
    event_type: str
    tool_name: str | None
    status: str
    details: dict[str, Any]
    created_at: datetime


class AgentEventListResponse(BaseModel):
    items: list[AgentEventResponse]
