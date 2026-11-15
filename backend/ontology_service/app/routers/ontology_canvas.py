from typing import Annotated, Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import (
    ActionDefinition,
    DataSourceConnection,
    DataSourceMapping,
    ObjectType,
    Ontology,
    OntologyBranch,
)
from backend.ontology_service.app.security import Actor, get_current_user
from backend.ontology_service.app.services.branches import create_schema_snapshot

router = APIRouter(prefix="/api/ontology/canvas", tags=["本体画布"])


@router.get("")
def get_ontology_canvas(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID,
    branch_id: UUID | None = None,
) -> dict[str, Any]:
    ontology = session.get(Ontology, ontology_id)
    if ontology is None:
        raise HTTPException(status_code=404, detail="本体不存在")
    branch = None
    snapshot = create_schema_snapshot(session, ontology)
    if branch_id is not None:
        branch = session.get(OntologyBranch, branch_id)
        if branch is None or branch.ontology_id != ontology.id:
            raise HTTPException(status_code=404, detail="本体分支不存在")
        snapshot = branch.snapshot

    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    object_type_by_name = {item["api_name"]: item for item in snapshot.get("object_types", [])}
    for object_type in snapshot.get("object_types", []):
        properties = object_type.get("properties", [])
        nodes.append({
            "id": f"object_type:{object_type['api_name']}",
            "type": "objectType",
            "data": {
                "api_name": object_type["api_name"],
                "display_name": object_type["display_name"],
                "description": object_type.get("description", ""),
                "primary_key_property": object_type.get("primary_key_property"),
                "title_key_property": object_type.get("title_key_property"),
                "icon": object_type.get("icon", "object"),
                "icon_color": object_type.get("icon_color", "#4F8067"),
                "properties": [
                    {
                        **prop,
                        "is_derived": bool(prop.get("options", {}).get("derived_property")),
                        "derived_definition": prop.get("options", {}).get("derived_property"),
                    }
                    for prop in properties
                ],
                "actions": [],
            },
        })

    for link in snapshot.get("link_types", []):
        edges.append({
            "id": f"link:{link['api_name']}",
            "source": f"object_type:{link['source_type_api_name']}",
            "target": f"object_type:{link['target_type_api_name']}",
            "type": "ontologyLink",
            "data": {
                "api_name": link["api_name"],
                "display_name": link["display_name"],
                "description": link.get("description", ""),
                "source_cardinality": link.get("source_cardinality", "many"),
                "target_cardinality": link.get("target_cardinality", "many"),
            },
        })

    for action in snapshot.get("actions", []):
        action_id = f"action:{action['api_name']}"
        nodes.append({
            "id": action_id,
            "type": "action",
            "data": {
                "api_name": action["api_name"],
                "display_name": action["display_name"],
                "enabled": action.get("enabled", True),
                "object_type_api_name": action["object_type_api_name"],
            },
        })
        object_type = object_type_by_name.get(action["object_type_api_name"])
        if object_type is not None:
            object_type.setdefault("actions", []).append(action["api_name"])
            object_node = next((node for node in nodes if node["id"] == f"object_type:{object_type['api_name']}"), None)
            if object_node is not None:
                object_node["data"]["actions"].append(action["api_name"])
            edges.append({
                "id": f"action_on:{action['api_name']}",
                "source": f"object_type:{action['object_type_api_name']}",
                "target": action_id,
                "type": "actionAssociation",
                "data": {"api_name": action["api_name"]},
            })

    sources = session.scalars(
        select(DataSourceConnection)
        .where(DataSourceConnection.ontology_id == ontology.id)
        .options(selectinload(DataSourceConnection.mappings).selectinload(DataSourceMapping.object_type))
        .order_by(DataSourceConnection.name)
    ).all()
    for source in sources:
        source_id = f"source_system:{source.id}"
        nodes.append({
            "id": source_id,
            "type": "sourceSystem",
            "data": {
                "source_id": str(source.id),
                "name": source.name,
                "connector_type": source.connector_type,
                "status": source.status,
                "mapping_count": len(source.mappings),
            },
        })
        for mapping in source.mappings:
            target_name = mapping.object_type.api_name
            if target_name not in object_type_by_name:
                continue
            edges.append({
                "id": f"mapping:{mapping.id}",
                "source": source_id,
                "target": f"object_type:{target_name}",
                "type": "sourceMapping",
                "data": {
                    "mapping_id": str(mapping.id),
                    "object_type_api_name": target_name,
                    "mapped_property_count": len(mapping.field_mappings),
                },
            })

    return {
        "ontology": {
            "id": str(ontology.id),
            "api_name": ontology.api_name,
            "display_name": ontology.display_name,
            "revision": ontology.revision,
        },
        "branch": {"id": str(branch.id), "name": branch.name, "status": branch.status} if branch else None,
        "nodes": nodes,
        "edges": edges,
    }
