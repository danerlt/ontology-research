from uuid import UUID

from pydantic import BaseModel, ConfigDict


class OntologyResponse(BaseModel):
    id: UUID
    api_name: str
    display_name: str
    description: str
    revision: int
    object_type_count: int = 0
    link_type_count: int = 0


class PropertyResponse(BaseModel):
    id: UUID
    api_name: str
    display_name: str
    data_type: str
    required: bool
    editable: bool
    unique_value: bool
    sensitive: bool
    options: dict

    model_config = ConfigDict(from_attributes=True)


class ObjectTypeResponse(BaseModel):
    id: UUID
    ontology_id: UUID
    api_name: str
    display_name: str
    plural_display_name: str
    description: str
    primary_key_property: str
    title_key_property: str
    aliases: list[str]
    groups: list[str]
    icon: str
    icon_color: str
    properties: list[PropertyResponse]

    model_config = ConfigDict(from_attributes=True)


class LinkTypeResponse(BaseModel):
    id: UUID
    api_name: str
    display_name: str
    description: str
    source_type_id: UUID
    target_type_id: UUID

    model_config = ConfigDict(from_attributes=True)
