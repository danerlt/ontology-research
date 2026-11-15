from datetime import datetime
from typing import Annotated, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from backend.ontology_service.app.schemas.proposals import SchemaChange

BranchName = Annotated[
    str,
    StringConstraints(min_length=2, max_length=120, pattern=r"^[a-zA-Z0-9][a-zA-Z0-9._-]*$"),
]


class OntologyBranchCreate(BaseModel):
    ontology_id: UUID
    name: BranchName
    description: str = Field(default="", max_length=2000)


class BranchChanges(BaseModel):
    changes: list[SchemaChange] = Field(min_length=1, max_length=100)


class BranchProposalCreate(BaseModel):
    title: str = Field(min_length=1, max_length=240)
    description: str = Field(default="", max_length=4000)


class BranchValidationIssue(BaseModel):
    path: str
    message: str


class BranchValidationResponse(BaseModel):
    errors: list[BranchValidationIssue]
    warnings: list[BranchValidationIssue]
    valid: bool


class OntologyBranchResponse(BaseModel):
    id: UUID
    ontology_id: UUID
    author_id: UUID
    name: str
    description: str
    base_revision: int
    snapshot: dict
    changes: list[dict]
    validation: BranchValidationResponse
    status: Literal["active", "proposed", "merged", "closed"]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
