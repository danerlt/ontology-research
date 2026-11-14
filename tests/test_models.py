from datetime import datetime
import unittest
from uuid import uuid4

from sqlalchemy import create_engine, event, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.ontology_service.app.database import Base
from backend.ontology_service.app.models import (
    ActionDefinition,
    AuditEvent,
    ChangeProposal,
    LinkType,
    ObjectLink,
    ObjectRecord,
    ObjectType,
    Ontology,
    PropertyDefinition,
    User,
)


class DomainModelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = create_engine("sqlite://")

        @event.listens_for(self.engine, "connect")
        def enable_foreign_keys(connection, _record) -> None:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)
        self.user = User(
            email="admin@example.com",
            password_hash="test-hash",
            role="admin",
        )
        self.ontology = Ontology(api_name="operations", display_name="运营本体", revision=1)
        self.session.add_all([self.user, self.ontology])
        self.session.commit()

    def tearDown(self) -> None:
        self.session.close()
        self.engine.dispose()

    def test_property_api_names_are_unique_per_type(self) -> None:
        object_type = ObjectType(
            ontology_id=self.ontology.id,
            api_name="customer",
            display_name="客户",
        )
        self.session.add(object_type)
        self.session.flush()
        self.session.add_all(
            [
                PropertyDefinition(
                    object_type_id=object_type.id,
                    api_name="customer_id",
                    display_name="客户编号",
                    data_type="string",
                ),
                PropertyDefinition(
                    object_type_id=object_type.id,
                    api_name="customer_id",
                    display_name="重复编号",
                    data_type="string",
                ),
            ]
        )

        with self.assertRaises(IntegrityError):
            self.session.flush()

    def test_object_record_references_type(self) -> None:
        object_type = ObjectType(
            ontology_id=self.ontology.id,
            api_name="customer",
            display_name="客户",
        )
        self.session.add(object_type)
        self.session.flush()
        record = ObjectRecord(
            object_type_id=object_type.id,
            primary_key_value="C-100",
            properties={"name": "北辰制造"},
        )
        self.session.add(record)
        self.session.commit()

        saved_record = self.session.scalar(select(ObjectRecord).where(ObjectRecord.id == record.id))

        self.assertEqual(saved_record.object_type_id, object_type.id)

    def test_object_version_is_an_integer(self) -> None:
        object_type = ObjectType(
            ontology_id=self.ontology.id,
            api_name="customer",
            display_name="客户",
        )
        self.session.add(object_type)
        self.session.flush()
        record = ObjectRecord(
            object_type_id=object_type.id,
            primary_key_value="C-100",
            properties={},
        )
        self.session.add(record)
        self.session.commit()

        self.assertEqual(record.version, 1)

    def test_audit_event_has_actor_and_timestamp(self) -> None:
        event = AuditEvent(
            actor_id=self.user.id,
            event_type="schema.proposal.created",
            resource_type="proposal",
            resource_id=str(uuid4()),
            details={"title": "新增客户类型"},
        )
        self.session.add(event)
        self.session.commit()

        self.assertIsInstance(event.created_at, datetime)

    def test_proposal_status_rejects_unknown_value(self) -> None:
        proposal = ChangeProposal(
            ontology_id=self.ontology.id,
            author_id=self.user.id,
            title="未定义状态",
            base_revision=1,
            changes=[],
            status="waiting",
        )
        self.session.add(proposal)

        with self.assertRaises(IntegrityError):
            self.session.flush()

    def test_link_type_connects_two_object_types(self) -> None:
        customer_type = ObjectType(
            ontology_id=self.ontology.id,
            api_name="customer",
            display_name="客户",
        )
        order_type = ObjectType(
            ontology_id=self.ontology.id,
            api_name="order",
            display_name="订单",
        )
        self.session.add_all([customer_type, order_type])
        self.session.flush()
        link_type = LinkType(
            ontology_id=self.ontology.id,
            api_name="customer_orders",
            display_name="客户订单",
            source_type_id=customer_type.id,
            target_type_id=order_type.id,
        )
        self.session.add(link_type)
        self.session.commit()

        self.assertEqual(link_type.target_type_id, order_type.id)

    def test_action_definition_keeps_allowlist_as_json(self) -> None:
        object_type = ObjectType(
            ontology_id=self.ontology.id,
            api_name="customer",
            display_name="客户",
        )
        self.session.add(object_type)
        self.session.flush()
        action = ActionDefinition(
            ontology_id=self.ontology.id,
            object_type_id=object_type.id,
            api_name="update_tier",
            display_name="更新等级",
            allowed_properties=["tier"],
            parameters_schema={"tier": {"type": "string"}},
        )
        self.session.add(action)
        self.session.commit()

        self.assertEqual(action.allowed_properties, ["tier"])

    def test_action_api_names_are_unique_per_ontology(self) -> None:
        object_type = ObjectType(
            ontology_id=self.ontology.id,
            api_name="customer",
            display_name="客户",
        )
        self.session.add(object_type)
        self.session.flush()
        self.session.add_all(
            [
                ActionDefinition(
                    ontology_id=self.ontology.id,
                    object_type_id=object_type.id,
                    api_name="update_tier",
                    display_name="更新等级",
                    allowed_properties=["tier"],
                    parameters_schema={},
                ),
                ActionDefinition(
                    ontology_id=self.ontology.id,
                    object_type_id=object_type.id,
                    api_name="update_tier",
                    display_name="重复更新等级",
                    allowed_properties=["tier"],
                    parameters_schema={},
                ),
            ]
        )

        with self.assertRaises(IntegrityError):
            self.session.flush()


if __name__ == "__main__":
    unittest.main()
