from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ObjectCreate(BaseModel):
    ontology_id: UUID
    object_type_api_name: str = Field(min_length=2, max_length=80)
    primary_key_value: str = Field(min_length=1, max_length=160)
    properties: dict[str, Any] = Field(default_factory=dict)


class ObjectLinkCreate(BaseModel):
    link_type_api_name: str = Field(min_length=2, max_length=80)
    target_object_id: UUID


class ObjectLinkResponse(BaseModel):
    link_id: UUID
    link_type_api_name: str
    link_type_display_name: str
    direction: str
    source_object_id: UUID
    target_object_id: UUID
    linked_object_id: UUID
    linked_object_type_api_name: str
    linked_object_type_display_name: str
    linked_primary_key: str


class ObjectRecordResponse(BaseModel):
    id: UUID
    object_type_api_name: str
    object_type_display_name: str
    primary_key_value: str
    properties: dict[str, Any]
    version: int
    created_at: datetime
    updated_at: datetime
    links: list[ObjectLinkResponse] = Field(default_factory=list)


class ObjectListResponse(BaseModel):
    items: list[ObjectRecordResponse]
    total: int
    page: int
    page_size: int


class ActionExecuteRequest(BaseModel):
    object_id: UUID
    expected_version: int
    parameters: dict[str, Any] = Field(default_factory=dict)


class ActionDefinitionResponse(BaseModel):
    id: UUID
    api_name: str
    display_name: str
    description: str
    object_type_api_name: str
    allowed_properties: list[str]
    parameters_schema: dict[str, Any]
    enabled: bool

    model_config = ConfigDict(from_attributes=True)
