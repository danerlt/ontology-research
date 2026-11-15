from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DataSourceCreate(BaseModel):
    ontology_id: UUID
    name: str = Field(min_length=2, max_length=160)
    description: str = Field(default="", max_length=2000)
    connector_type: Literal["local_file"] = "local_file"


class DataSourceResponse(BaseModel):
    id: UUID
    ontology_id: UUID
    created_by_id: UUID
    name: str
    description: str
    connector_type: str
    status: str
    mapping_count: int = 0
    last_run_status: str | None = None
    last_run_at: datetime | None = None
    created_at: datetime


class DataMappingUpsert(BaseModel):
    object_type_api_name: str = Field(min_length=2, max_length=80)
    primary_key_field: str = Field(min_length=1, max_length=160)
    field_mappings: dict[str, str] = Field(min_length=1, max_length=250)


class DataMappingResponse(BaseModel):
    id: UUID
    connection_id: UUID
    object_type_id: UUID
    object_type_api_name: str
    object_type_display_name: str
    primary_key_field: str
    field_mappings: dict[str, str]
    updated_at: datetime


class DataRowsRequest(BaseModel):
    rows: list[dict[str, Any]] = Field(min_length=1, max_length=5000)


class DataPreviewIssue(BaseModel):
    row: int
    field: str
    message: str


class DataPreviewItem(BaseModel):
    row: int
    primary_key_value: str
    properties: dict[str, Any]


class DataPreviewResponse(BaseModel):
    valid: bool
    rows_total: int
    items: list[DataPreviewItem]
    errors: list[DataPreviewIssue]


class DataImportRunResponse(BaseModel):
    id: UUID
    connection_id: UUID
    mapping_id: UUID
    actor_id: UUID
    status: Literal["completed", "failed"]
    rows_total: int
    rows_imported: int
    errors: list[dict[str, Any]]
    created_at: datetime
    completed_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
