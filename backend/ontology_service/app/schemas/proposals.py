from datetime import datetime
from typing import Annotated, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

ApiName = Annotated[
    str,
    StringConstraints(min_length=2, max_length=80, pattern=r"^[a-z][a-z0-9_]*$"),
]


class AddObjectTypeChange(BaseModel):
    op: Literal["add_object_type"]
    api_name: ApiName
    display_name: str = Field(min_length=1, max_length=160)
    description: str = Field(default="", max_length=2000)
    primary_key_property: ApiName = "id"


class AddPropertyChange(BaseModel):
    op: Literal["add_property"]
    object_type_api_name: ApiName
    api_name: ApiName
    display_name: str = Field(min_length=1, max_length=160)
    data_type: Literal["string", "integer", "number", "boolean", "date", "datetime", "enum", "json"]
    required: bool = False
    editable: bool = True
    unique_value: bool = False
    sensitive: bool = False
    options: dict = Field(default_factory=dict)


class AddLinkTypeChange(BaseModel):
    op: Literal["add_link_type"]
    api_name: ApiName
    display_name: str = Field(min_length=1, max_length=160)
    description: str = Field(default="", max_length=2000)
    source_type_api_name: ApiName
    target_type_api_name: ApiName


SchemaChange = Annotated[
    AddObjectTypeChange | AddPropertyChange | AddLinkTypeChange,
    Field(discriminator="op"),
]


class ProposalCreate(BaseModel):
    ontology_id: UUID
    title: str = Field(min_length=1, max_length=240)
    description: str = Field(default="", max_length=4000)
    base_revision: int = Field(ge=0)
    changes: list[SchemaChange] = Field(min_length=1)


class ProposalResponse(BaseModel):
    id: UUID
    ontology_id: UUID
    author_id: UUID
    reviewer_id: UUID | None
    title: str
    description: str
    base_revision: int
    changes: list[dict]
    status: str
    review_comment: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProposalReject(BaseModel):
    reason: str = Field(min_length=1, max_length=2000)


class ProposalMergeResponse(BaseModel):
    proposal: ProposalResponse
    ontology_revision: int
