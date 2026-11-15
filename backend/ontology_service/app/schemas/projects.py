from uuid import UUID

from pydantic import BaseModel, EmailStr, Field
from typing import Literal


class ProjectCreate(BaseModel):
    api_name: str = Field(min_length=2, max_length=80, pattern=r"^[a-z][a-z0-9_]*$")
    display_name: str = Field(min_length=2, max_length=160)
    description: str = Field(default="", max_length=2000)


class ProjectResponse(BaseModel):
    id: UUID
    api_name: str
    display_name: str
    description: str
    role: str


class ProjectMemberUpsert(BaseModel):
    email: EmailStr
    role: Literal["admin", "editor", "viewer"]


class ProjectMemberResponse(BaseModel):
    id: UUID
    user_id: UUID
    email: EmailStr
    role: str
