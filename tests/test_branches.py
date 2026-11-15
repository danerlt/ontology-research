import unittest
from uuid import UUID

from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine, event, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.main import create_app
from backend.ontology_service.app.models import ActionDefinition, LinkType, ObjectType, Ontology, PropertyDefinition, User
from backend.ontology_service.app.security import Actor, create_access_token, hash_password


class OntologyBranchApiTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )

        @event.listens_for(self.engine, "connect")
        def enable_foreign_keys(connection, _record) -> None:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
        self.settings = Settings(jwt_secret="unit-test-secret-long-enough-for-hmac-sha256")
        self.admin = User(email="admin@example.com", password_hash=hash_password("admin-pass"), role="admin")
        self.editor = User(email="editor@example.com", password_hash=hash_password("editor-pass"), role="editor")
        self.ontology = Ontology(api_name="operations", display_name="运营本体", revision=1)
        with self.session_factory() as session:
            session.add_all([self.admin, self.editor, self.ontology])
            session.commit()
        self.app = create_app(self.settings)

        def override_get_db():
            with self.session_factory() as session:
                yield session

        self.app.dependency_overrides[get_db] = override_get_db
        self.client = AsyncClient(transport=ASGITransport(app=self.app), base_url="http://test")

    async def asyncTearDown(self) -> None:
        await self.client.aclose()
        self.engine.dispose()

    def headers_for(self, user: User) -> dict[str, str]:
        actor = Actor(id=str(user.id), email=user.email, role=user.role)
        token = create_access_token(actor, self.settings)
        return {"Authorization": f"Bearer {token}"}

    async def create_branch(self) -> str:
        response = await self.client.post(
            "/api/branches",
            headers=self.headers_for(self.editor),
            json={"ontology_id": str(self.ontology.id), "name": "customer-work", "description": "客户模型调整"},
        )
        self.assertEqual(response.status_code, 201, response.text)
        return response.json()["id"]

    async def stage(self, branch_id: str, changes: list[dict]) -> None:
        response = await self.client.post(
            f"/api/branches/{branch_id}/changes",
            headers=self.headers_for(self.editor),
            json={"changes": changes},
        )
        self.assertEqual(response.status_code, 200, response.text)

    async def propose(self, branch_id: str) -> str:
        response = await self.client.post(
            f"/api/branches/{branch_id}/propose",
            headers=self.headers_for(self.editor),
            json={"title": "新增站点类型", "description": "建立站点语义"},
        )
        self.assertEqual(response.status_code, 201, response.text)
        return response.json()["id"]

    async def test_branch_changes_do_not_mutate_main_schema(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )

        main_types = await self.client.get(
            "/api/object-types",
            headers=self.headers_for(self.editor),
            params={"ontology_id": str(self.ontology.id)},
        )
        branch = await self.client.get(f"/api/branches/{branch_id}", headers=self.headers_for(self.editor))

        self.assertEqual(main_types.status_code, 200)
        self.assertEqual(main_types.json(), [])
        self.assertEqual(branch.status_code, 200)
        self.assertIn("site", {item["api_name"] for item in branch.json()["snapshot"]["object_types"]})

    async def test_object_type_metadata_and_title_key_survive_review_and_merge(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(branch_id, [
            {
                "op": "add_object_type",
                "api_name": "site",
                "display_name": "站点",
                "plural_display_name": "站点",
                "description": "履约站点",
                "primary_key_property": "site_id",
                "title_key_property": "site_name",
                "aliases": ["仓库", "门店"],
                "groups": ["履约", "基础设施"],
                "icon": "warehouse",
                "icon_color": "#2E6658",
            },
            {
                "op": "add_property",
                "object_type_api_name": "site",
                "api_name": "site_name",
                "display_name": "站点名称",
                "data_type": "string",
                "required": True,
            },
        ])
        branch = await self.client.get(f"/api/branches/{branch_id}", headers=self.headers_for(self.editor))
        proposal_id = await self.propose(branch_id)
        for key in ("object_type:site", "property:site.site_name"):
            review = await self.client.post(
                f"/api/proposals/{proposal_id}/resources/{key}/review",
                headers=self.headers_for(self.admin),
                json={"status": "approved", "comment": "元数据完整"},
            )
            self.assertEqual(review.status_code, 200, review.text)
        merged = await self.client.post(f"/api/proposals/{proposal_id}/merge", headers=self.headers_for(self.admin))
        main_types = await self.client.get("/api/object-types", headers=self.headers_for(self.editor), params={"ontology_id": str(self.ontology.id)})

        self.assertEqual(branch.status_code, 200, branch.text)
        self.assertTrue(branch.json()["validation"]["valid"], branch.json()["validation"])
        self.assertEqual(merged.status_code, 200, merged.text)
        site = next(item for item in main_types.json() if item["api_name"] == "site")
        self.assertEqual(site["plural_display_name"], "站点")
        self.assertEqual(site["title_key_property"], "site_name")
        self.assertEqual(site["aliases"], ["仓库", "门店"])
        self.assertEqual(site["groups"], ["履约", "基础设施"])
        self.assertEqual(site["icon"], "warehouse")
        self.assertEqual(site["icon_color"], "#2E6658")

    async def test_branch_validation_requires_an_existing_title_key(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(branch_id, [{
            "op": "add_object_type",
            "api_name": "site",
            "display_name": "站点",
            "primary_key_property": "site_id",
            "title_key_property": "missing_name",
        }])
        branch = await self.client.get(f"/api/branches/{branch_id}", headers=self.headers_for(self.editor))

        self.assertFalse(branch.json()["validation"]["valid"])
        self.assertTrue(any("标题键" in item["message"] for item in branch.json()["validation"]["errors"]))

    async def test_existing_object_and_property_metadata_can_be_updated_through_review(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(branch_id, [
            {
                "op": "add_object_type",
                "api_name": "customer",
                "display_name": "客户",
                "primary_key_property": "customer_id",
            },
            {
                "op": "add_property",
                "object_type_api_name": "customer",
                "api_name": "name",
                "display_name": "姓名",
                "data_type": "string",
            },
        ])
        await self.stage(branch_id, [
            {
                "op": "update_object_type",
                "api_name": "customer",
                "display_name": "企业客户",
                "plural_display_name": "企业客户",
                "title_key_property": "name",
                "aliases": ["账户"],
                "groups": ["销售"],
            },
            {
                "op": "update_property",
                "object_type_api_name": "customer",
                "api_name": "name",
                "display_name": "客户名称",
                "sensitive": True,
            },
        ])
        branch = await self.client.get(f"/api/branches/{branch_id}", headers=self.headers_for(self.editor))
        proposal_id = await self.propose(branch_id)
        for key in ("object_type:customer", "property:customer.name"):
            review = await self.client.post(
                f"/api/proposals/{proposal_id}/resources/{key}/review",
                headers=self.headers_for(self.admin),
                json={"status": "approved", "comment": "已复核结构变更"},
            )
            self.assertEqual(review.status_code, 200, review.text)
        merged = await self.client.post(f"/api/proposals/{proposal_id}/merge", headers=self.headers_for(self.admin))
        types = await self.client.get(
            "/api/object-types", headers=self.headers_for(self.editor), params={"ontology_id": str(self.ontology.id)}
        )

        self.assertTrue(branch.json()["validation"]["valid"], branch.json()["validation"])
        self.assertEqual(merged.status_code, 200, merged.text)
        customer = types.json()[0]
        self.assertEqual(customer["display_name"], "企业客户")
        self.assertEqual(customer["title_key_property"], "name")
        self.assertEqual(customer["aliases"], ["账户"])
        self.assertEqual(customer["properties"][1]["display_name"], "客户名称")
        self.assertTrue(customer["properties"][1]["sensitive"])

    async def test_existing_link_and_action_can_be_updated_through_review(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(branch_id, [
            {"op": "add_object_type", "api_name": "customer", "display_name": "客户"},
            {"op": "add_property", "object_type_api_name": "customer", "api_name": "name", "display_name": "姓名", "data_type": "string"},
            {"op": "add_object_type", "api_name": "site", "display_name": "站点"},
            {"op": "add_link_type", "api_name": "customer_site", "display_name": "关联站点", "source_type_api_name": "customer", "target_type_api_name": "site"},
            {"op": "add_action", "api_name": "rename_customer", "display_name": "重命名客户", "object_type_api_name": "customer", "allowed_properties": ["name"], "parameters_schema": {"name": {"type": "string"}}},
        ])
        await self.stage(branch_id, [
            {"op": "update_link_type", "api_name": "customer_site", "display_name": "客户服务站点", "description": "客户可使用的履约站点"},
            {"op": "update_action", "api_name": "rename_customer", "display_name": "更新客户名称", "enabled": False},
        ])
        proposal_id = await self.propose(branch_id)
        for key in (
            "object_type:customer",
            "property:customer.name",
            "object_type:site",
            "link_type:customer_site",
            "action:rename_customer",
        ):
            review = await self.client.post(
                f"/api/proposals/{proposal_id}/resources/{key}/review",
                headers=self.headers_for(self.admin),
                json={"status": "approved", "comment": "已复核资源更新"},
            )
            self.assertEqual(review.status_code, 200, review.text)
        merged = await self.client.post(f"/api/proposals/{proposal_id}/merge", headers=self.headers_for(self.admin))

        self.assertEqual(merged.status_code, 200, merged.text)
        with self.session_factory() as session:
            link = session.scalar(select(LinkType).where(LinkType.api_name == "customer_site"))
            action = session.scalar(select(ActionDefinition).where(ActionDefinition.api_name == "rename_customer"))
        self.assertEqual(link.display_name, "客户服务站点")
        self.assertEqual(link.description, "客户可使用的履约站点")
        self.assertEqual(action.display_name, "更新客户名称")
        self.assertFalse(action.enabled)

    async def test_branch_can_define_action_and_merge_it_after_resource_review(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [
                {"op": "add_object_type", "api_name": "customer", "display_name": "客户"},
                {
                    "op": "add_property",
                    "object_type_api_name": "customer",
                    "api_name": "state",
                    "display_name": "状态",
                    "data_type": "string",
                },
                {
                    "op": "add_action",
                    "api_name": "close_customer",
                    "display_name": "关闭客户",
                    "object_type_api_name": "customer",
                    "allowed_properties": ["state"],
                    "parameters_schema": {"state": {"required": True, "type": "string", "enum": ["closed"]}},
                    "submission_criteria": {"property": "state", "operator": "not_equals", "value": "closed"},
                },
            ],
        )
        branch = await self.client.get(f"/api/branches/{branch_id}", headers=self.headers_for(self.editor))
        proposal_id = await self.propose(branch_id)

        for resource_key in ("object_type:customer", "property:customer.state", "action:close_customer"):
            review = await self.client.post(
                f"/api/proposals/{proposal_id}/resources/{resource_key}/review",
                headers=self.headers_for(self.admin),
                json={"status": "approved", "comment": "已检查定义"},
            )
            self.assertEqual(review.status_code, 200, review.text)
        merged = await self.client.post(
            f"/api/proposals/{proposal_id}/merge", headers=self.headers_for(self.admin)
        )
        actions = await self.client.get(
            "/api/actions", headers=self.headers_for(self.editor), params={"ontology_id": str(self.ontology.id)}
        )

        self.assertEqual(merged.status_code, 200, merged.text)
        self.assertEqual(branch.json()["snapshot"]["actions"][0]["submission_criteria"]["operator"], "not_equals")
        self.assertEqual(actions.json()[0]["api_name"], "close_customer")
        with self.session_factory() as session:
            action = session.scalar(select(ActionDefinition).where(ActionDefinition.api_name == "close_customer"))
        self.assertIsNotNone(action)

    async def test_branch_action_cannot_target_an_undefined_property(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [
                {"op": "add_object_type", "api_name": "customer", "display_name": "客户"},
                {
                    "op": "add_action",
                    "api_name": "close_customer",
                    "display_name": "关闭客户",
                    "object_type_api_name": "customer",
                    "allowed_properties": ["missing"],
                    "parameters_schema": {"missing": {"required": True, "type": "string"}},
                },
            ],
        )

        response = await self.client.post(
            f"/api/branches/{branch_id}/validate", headers=self.headers_for(self.editor)
        )

        self.assertFalse(response.json()["valid"])
        self.assertTrue(any("missing" in issue["message"] for issue in response.json()["errors"]))

    async def test_branch_validation_rejects_action_criteria_with_unknown_property(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [
                {"op": "add_object_type", "api_name": "customer", "display_name": "客户"},
                {
                    "op": "add_action",
                    "api_name": "close_customer",
                    "display_name": "关闭客户",
                    "object_type_api_name": "customer",
                    "allowed_properties": ["id"],
                    "parameters_schema": {"id": {"type": "string"}},
                    "submission_criteria": {
                        "property": "missing",
                        "operator": "equals",
                        "value": None,
                    },
                },
            ],
        )

        response = await self.client.post(
            f"/api/branches/{branch_id}/validate", headers=self.headers_for(self.editor)
        )

        self.assertFalse(response.json()["valid"])
        self.assertTrue(any("missing" in issue["message"] for issue in response.json()["errors"]))

    async def test_branch_validation_reports_duplicate_api_name(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [
                {"op": "add_object_type", "api_name": "site", "display_name": "站点"},
                {"op": "add_object_type", "api_name": "site", "display_name": "重复站点"},
            ],
        )

        response = await self.client.post(
            f"/api/branches/{branch_id}/validate",
            headers=self.headers_for(self.editor),
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertTrue(any("site" in issue["path"] for issue in response.json()["errors"]))

    async def test_merge_rejects_stale_branch_without_partial_writes(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )
        proposal_id = await self.propose(branch_id)
        with self.session_factory() as session:
            ontology = session.get(Ontology, self.ontology.id)
            ontology.revision += 1
            session.commit()

        response = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )

        self.assertEqual(response.status_code, 409)
        with self.session_factory() as session:
            ontology = session.get(Ontology, self.ontology.id)
            site = session.scalar(select(ObjectType).where(ObjectType.api_name == "site"))
        self.assertEqual(ontology.revision, 2)
        self.assertIsNone(site)

    async def test_resource_review_required_before_merge(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )
        proposal_id = await self.propose(branch_id)
        merge_before_review = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )
        self.assertEqual(merge_before_review.status_code, 409)

        review = await self.client.post(
            f"/api/proposals/{proposal_id}/resources/object_type:site/review",
            headers=self.headers_for(self.admin),
            json={"status": "approved", "comment": "字段定义符合约定"},
        )
        merge_after_review = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )

        self.assertEqual(review.status_code, 200, review.text)
        self.assertEqual(merge_after_review.status_code, 200, merge_after_review.text)
        with self.session_factory() as session:
            site = session.scalar(select(ObjectType).where(ObjectType.api_name == "site"))
        self.assertIsNotNone(site)

    async def test_rebase_preserves_branch_changes_and_updates_base_revision(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )
        with self.session_factory() as session:
            customer = ObjectType(ontology_id=self.ontology.id, api_name="customer", display_name="客户")
            session.add(customer)
            session.flush()
            session.add(PropertyDefinition(
                object_type_id=customer.id,
                api_name="id",
                display_name="客户编号",
                data_type="string",
                required=True,
                editable=False,
                unique_value=True,
            ))
            session.get(Ontology, self.ontology.id).revision = 2
            session.commit()

        response = await self.client.post(
            f"/api/branches/{branch_id}/rebase",
            headers=self.headers_for(self.editor),
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["base_revision"], 2)
        self.assertEqual(
            {item["api_name"] for item in response.json()["snapshot"]["object_types"]},
            {"customer", "site"},
        )

    async def test_rebase_reports_resource_conflict_without_changing_branch(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )
        with self.session_factory() as session:
            session.add(ObjectType(ontology_id=self.ontology.id, api_name="site", display_name="已占用站点"))
            session.get(Ontology, self.ontology.id).revision = 2
            session.commit()

        response = await self.client.post(
            f"/api/branches/{branch_id}/rebase",
            headers=self.headers_for(self.editor),
        )

        self.assertEqual(response.status_code, 409)
        self.assertIn("object_type:site", response.json()["detail"]["conflicts"][0]["path"])
        branch = await self.client.get(f"/api/branches/{branch_id}", headers=self.headers_for(self.editor))
        self.assertEqual(branch.json()["base_revision"], 1)


if __name__ == "__main__":
    unittest.main()
