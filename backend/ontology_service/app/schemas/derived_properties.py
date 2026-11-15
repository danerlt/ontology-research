from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from backend.ontology_service.app.schemas.proposals import DerivedPropertyDefinitionInput


class DerivedPropertyPreviewRequest(BaseModel):
    ontology_id: UUID
    object_id: UUID
    branch_id: UUID | None = None
    definition: DerivedPropertyDefinitionInput


class DerivedPropertyPreviewResponse(BaseModel):
    object_id: UUID
    api_name: str
    value: Any
    result_type: str
    aggregation: str | None
    matched_count: int
    path_object_count: int
    ignored_null_count: int
    trace: list[dict[str, Any]] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
