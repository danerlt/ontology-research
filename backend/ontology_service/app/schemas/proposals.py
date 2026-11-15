from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

ApiName = Annotated[
    str,
    StringConstraints(min_length=2, max_length=80, pattern=r"^[a-z][a-z0-9_]*$"),
]


class AddObjectTypeChange(BaseModel):
    op: Literal["add_object_type"]
    api_name: ApiName
    display_name: str = Field(min_length=1, max_length=160)
    plural_display_name: str = Field(default="", max_length=160)
    description: str = Field(default="", max_length=2000)
    primary_key_property: ApiName = "id"
    title_key_property: ApiName | None = None
    aliases: list[str] = Field(default_factory=list, max_length=50)
    groups: list[str] = Field(default_factory=list, max_length=50)
    icon: str = Field(default="object", min_length=1, max_length=64)
    icon_color: str = Field(default="#4F8067", pattern=r"^#[0-9A-Fa-f]{6}$")


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


class UpdateObjectTypeChange(BaseModel):
    op: Literal["update_object_type"]
    api_name: ApiName
    display_name: str | None = Field(default=None, min_length=1, max_length=160)
    plural_display_name: str | None = Field(default=None, min_length=1, max_length=160)
    description: str | None = Field(default=None, max_length=2000)
    title_key_property: ApiName | None = None
    aliases: list[str] | None = Field(default=None, max_length=50)
    groups: list[str] | None = Field(default=None, max_length=50)
    icon: str | None = Field(default=None, min_length=1, max_length=64)
    icon_color: str | None = Field(default=None, pattern=r"^#[0-9A-Fa-f]{6}$")

    @model_validator(mode="after")
    def require_changes(self) -> "UpdateObjectTypeChange":
        changed_fields = self.model_fields_set - {"op", "api_name"}
        if not changed_fields or any(getattr(self, field) is None for field in changed_fields):
            raise ValueError("至少提供一个对象类型字段修改")
        return self


class UpdatePropertyChange(BaseModel):
    op: Literal["update_property"]
    object_type_api_name: ApiName
    api_name: ApiName
    display_name: str | None = Field(default=None, min_length=1, max_length=160)
    data_type: Literal["string", "integer", "number", "boolean", "date", "datetime", "enum", "json"] | None = None
    required: bool | None = None
    editable: bool | None = None
    unique_value: bool | None = None
    sensitive: bool | None = None
    options: dict | None = None

    @model_validator(mode="after")
    def require_changes(self) -> "UpdatePropertyChange":
        changed_fields = self.model_fields_set - {"op", "object_type_api_name", "api_name"}
        if not changed_fields or any(getattr(self, field) is None for field in changed_fields):
            raise ValueError("至少提供一个属性字段修改")
        return self


class AddLinkTypeChange(BaseModel):
    op: Literal["add_link_type"]
    api_name: ApiName
    display_name: str = Field(min_length=1, max_length=160)
    description: str = Field(default="", max_length=2000)
    source_type_api_name: ApiName
    target_type_api_name: ApiName
    source_cardinality: Literal["one", "many"] = "many"
    target_cardinality: Literal["one", "many"] = "many"


class UpdateLinkTypeChange(BaseModel):
    op: Literal["update_link_type"]
    api_name: ApiName
    display_name: str | None = Field(default=None, min_length=1, max_length=160)
    description: str | None = Field(default=None, max_length=2000)
    source_cardinality: Literal["one", "many"] | None = None
    target_cardinality: Literal["one", "many"] | None = None

    @model_validator(mode="after")
    def require_changes(self) -> "UpdateLinkTypeChange":
        changed_fields = self.model_fields_set - {"op", "api_name"}
        if not changed_fields or any(getattr(self, field) is None for field in changed_fields):
            raise ValueError("至少提供一个链接类型字段修改")
        return self


class DerivedPathStep(BaseModel):
    link_api_name: ApiName
    direction: Literal["outgoing", "incoming"]


class DerivedPropertyDefinitionInput(BaseModel):
    object_type_api_name: ApiName
    api_name: ApiName
    display_name: str = Field(min_length=1, max_length=160)
    description: str = Field(default="", max_length=2000)
    data_type: Literal["string", "integer", "number", "boolean", "date", "datetime", "enum", "json"]
    path: list[DerivedPathStep] = Field(min_length=1, max_length=3)
    terminal_property_api_name: ApiName
    aggregation: Literal["count", "sum", "average", "minimum", "maximum", "collect_list", "collect_set"] | None = None


class SetDerivedPropertyChange(DerivedPropertyDefinitionInput):
    op: Literal["set_derived_property"]


class RemoveDerivedPropertyChange(BaseModel):
    op: Literal["remove_derived_property"]
    object_type_api_name: ApiName
    api_name: ApiName


class AddActionChange(BaseModel):
    op: Literal["add_action"]
    api_name: ApiName
    display_name: str = Field(min_length=1, max_length=160)
    description: str = Field(default="", max_length=2000)
    object_type_api_name: ApiName
    allowed_properties: list[ApiName] = Field(min_length=1, max_length=100)
    parameters_schema: dict[str, dict] = Field(default_factory=dict)
    submission_criteria: dict = Field(default_factory=dict)
    enabled: bool = True


class UpdateActionChange(BaseModel):
    op: Literal["update_action"]
    api_name: ApiName
    display_name: str | None = Field(default=None, min_length=1, max_length=160)
    description: str | None = Field(default=None, max_length=2000)
    allowed_properties: list[ApiName] | None = Field(default=None, min_length=1, max_length=100)
    parameters_schema: dict[str, dict] | None = None
    submission_criteria: dict | None = None
    enabled: bool | None = None

    @model_validator(mode="after")
    def require_changes(self) -> "UpdateActionChange":
        changed_fields = self.model_fields_set - {"op", "api_name"}
        if not changed_fields or any(getattr(self, field) is None for field in changed_fields):
            raise ValueError("至少提供一个 Action 字段修改")
        return self


SchemaChange = Annotated[
    AddObjectTypeChange
    | AddPropertyChange
    | UpdateObjectTypeChange
    | UpdatePropertyChange
    | AddLinkTypeChange
    | UpdateLinkTypeChange
    | SetDerivedPropertyChange
    | RemoveDerivedPropertyChange
    | AddActionChange
    | UpdateActionChange,
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
    branch_id: UUID | None = None
    reviewer_id: UUID | None
    title: str
    description: str
    base_revision: int
    changes: list[dict]
    status: str
    review_comment: str
    resource_reviews: list["ProposalResourceReviewResponse"] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProposalResourceReviewResponse(BaseModel):
    id: UUID
    proposal_id: UUID
    resource_key: str
    status: str
    reviewer_id: UUID | None
    comment: str
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProposalResourceReviewRequest(BaseModel):
    status: Literal["approved", "rejected"]
    comment: str = Field(default="", max_length=2000)


class ProposalReject(BaseModel):
    reason: str = Field(min_length=1, max_length=2000)


class ProposalMergeResponse(BaseModel):
    proposal: ProposalResponse
    ontology_revision: int
