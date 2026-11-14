import logging

from sqlalchemy import select

from backend.ontology_service.app.config import get_settings
from backend.ontology_service.app.database import SessionLocal
from backend.ontology_service.app.models import (
    ActionDefinition,
    AgentDefinition,
    LinkType,
    ObjectLink,
    ObjectRecord,
    ObjectType,
    Ontology,
    PropertyDefinition,
    User,
)
from backend.ontology_service.app.security import hash_password

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def seed_demo_data() -> None:
    settings = get_settings()
    with SessionLocal() as session:
        _seed_user(session, settings.admin_email, "admin", settings.admin_password)
        _seed_user(session, "editor@example.com", "editor", "local-editor-password")
        _seed_user(session, "viewer@example.com", "viewer", "local-viewer-password")

        ontology = session.scalar(select(Ontology).where(Ontology.api_name == "operations"))
        if ontology is None:
            ontology = Ontology(
                api_name="operations",
                display_name="运营知识图谱",
                description="围绕客户、订单与运营 Action 建立的演示本体。",
            )
            session.add(ontology)
            session.flush()

        customer_type = _get_or_create_type(session, ontology.id, "customer", "客户")
        order_type = _get_or_create_type(session, ontology.id, "order", "订单")
        _get_or_create_property(session, customer_type.id, "id", "客户编号", "string", required=True, editable=False, unique=True)
        _get_or_create_property(session, customer_type.id, "name", "客户名称", "string", required=True)
        _get_or_create_property(
            session,
            customer_type.id,
            "tier",
            "客户等级",
            "enum",
            options={"choices": ["standard", "preferred"]},
        )
        _get_or_create_property(session, customer_type.id, "region", "所属区域", "string")
        _get_or_create_property(session, customer_type.id, "tax_id", "税号", "string", sensitive=True)
        _get_or_create_property(session, order_type.id, "id", "订单编号", "string", required=True, editable=False, unique=True)
        _get_or_create_property(session, order_type.id, "amount", "订单金额", "number", required=True)
        _get_or_create_property(session, order_type.id, "state", "订单状态", "string", required=True)
        session.flush()

        link_type = session.scalar(
            select(LinkType).where(LinkType.ontology_id == ontology.id, LinkType.api_name == "customer_orders")
        )
        if link_type is None:
            link_type = LinkType(
                ontology_id=ontology.id,
                api_name="customer_orders",
                display_name="客户订单",
                description="客户与其订单之间的业务关系。",
                source_type_id=customer_type.id,
                target_type_id=order_type.id,
            )
            session.add(link_type)

        customer = _get_or_create_object(
            session,
            customer_type,
            "C-100",
            {"id": "C-100", "name": "北辰制造", "tier": "preferred", "region": "华东", "tax_id": "91310000DEMO01"},
        )
        order = _get_or_create_object(
            session,
            order_type,
            "O-100",
            {"id": "O-100", "amount": 128000.0, "state": "processing"},
        )
        session.flush()

        action = session.scalar(
            select(ActionDefinition).where(
                ActionDefinition.ontology_id == ontology.id,
                ActionDefinition.api_name == "set_customer_tier",
            )
        )
        if action is None:
            session.add(
                ActionDefinition(
                    ontology_id=ontology.id,
                    object_type_id=customer_type.id,
                    api_name="set_customer_tier",
                    display_name="调整客户等级",
                    description="更新客户分层，用于后续运营策略。",
                    allowed_properties=["tier"],
                    parameters_schema={"tier": {"required": True}},
                )
            )
        if session.scalar(
            select(ObjectLink.id).where(
                ObjectLink.link_type_id == link_type.id,
                ObjectLink.source_object_id == customer.id,
                ObjectLink.target_object_id == order.id,
            )
        ) is None:
            session.add(
                ObjectLink(
                    link_type_id=link_type.id,
                    source_object_id=customer.id,
                    target_object_id=order.id,
                )
            )
        if session.scalar(
            select(AgentDefinition.id).where(AgentDefinition.api_name == "operations_assistant")
        ) is None:
            session.add(
                AgentDefinition(
                    api_name="operations_assistant",
                    display_name="运营助理",
                    description="可查找和读取本体对象，并在授权下调整客户等级。",
                    allowed_tools=["search_objects", "get_object", "execute_action"],
                    allowed_actions=["set_customer_tier"],
                )
            )
        session.commit()
    logger.info("演示数据已就绪：运营知识图谱、客户/订单对象、Action 和运营助理。")


def _seed_user(session, email: str, role: str, password: str) -> None:
    user = session.scalar(select(User).where(User.email == email.lower()))
    if user is None:
        session.add(User(email=email.lower(), password_hash=hash_password(password), role=role))


def _get_or_create_type(session, ontology_id, api_name: str, display_name: str) -> ObjectType:
    object_type = session.scalar(
        select(ObjectType).where(ObjectType.ontology_id == ontology_id, ObjectType.api_name == api_name)
    )
    if object_type is None:
        object_type = ObjectType(
            ontology_id=ontology_id,
            api_name=api_name,
            display_name=display_name,
            primary_key_property="id",
        )
        session.add(object_type)
        session.flush()
    return object_type


def _get_or_create_property(
    session,
    object_type_id,
    api_name: str,
    display_name: str,
    data_type: str,
    *,
    required: bool = False,
    editable: bool = True,
    unique: bool = False,
    sensitive: bool = False,
    options: dict | None = None,
) -> None:
    prop = session.scalar(
        select(PropertyDefinition).where(
            PropertyDefinition.object_type_id == object_type_id,
            PropertyDefinition.api_name == api_name,
        )
    )
    if prop is None:
        session.add(
            PropertyDefinition(
                object_type_id=object_type_id,
                api_name=api_name,
                display_name=display_name,
                data_type=data_type,
                required=required,
                editable=editable,
                unique_value=unique,
                sensitive=sensitive,
                options=options or {},
            )
        )


def _get_or_create_object(session, object_type: ObjectType, primary_key_value: str, properties: dict) -> ObjectRecord:
    record = session.scalar(
        select(ObjectRecord).where(
            ObjectRecord.object_type_id == object_type.id,
            ObjectRecord.primary_key_value == primary_key_value,
        )
    )
    if record is None:
        record = ObjectRecord(
            object_type_id=object_type.id,
            primary_key_value=primary_key_value,
            properties=properties,
        )
        session.add(record)
        session.flush()
    return record


if __name__ == "__main__":
    seed_demo_data()
