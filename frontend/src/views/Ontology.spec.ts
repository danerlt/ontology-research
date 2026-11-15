import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

const apiMock = vi.hoisted(() => ({ get: vi.fn() }));
const routeState = vi.hoisted(() => ({ query: { type: "customer", tab: "actions" } }));
const routerMock = vi.hoisted(() => ({ replace: vi.fn() }));

vi.mock("../api/client", () => ({ api: apiMock, readableError: () => "请求失败" }));
vi.mock("vue-router", () => ({ useRoute: () => routeState, useRouter: () => routerMock }));

import Ontology from "./Ontology.vue";

function mountOntology() {
  return mount(Ontology, {
    global: { stubs: { RouterLink: { template: "<a><slot /></a>" } } },
  });
}

const ontology = { id: "ontology-1", api_name: "operations", display_name: "运营本体", revision: 4 };
const customer = {
  id: "type-1",
  ontology_id: "ontology-1",
  api_name: "customer",
  display_name: "客户",
  description: "客户主数据",
  primary_key_property: "id",
  properties: [
    { id: "p-id", api_name: "id", display_name: "客户编号", data_type: "string", required: true, editable: false, unique_value: true, sensitive: false, options: {} },
    { id: "p-name", api_name: "name", display_name: "客户名称", data_type: "string", required: true, editable: true, unique_value: false, sensitive: false, options: {} },
    { id: "p-tax", api_name: "tax_id", display_name: "税号", data_type: "string", required: false, editable: false, unique_value: false, sensitive: true, options: {} },
  ],
};
const action = {
  id: "action-1",
  api_name: "set_customer_tier",
  display_name: "调整客户等级",
  description: "调整客户分层",
  object_type_api_name: "customer",
  allowed_properties: ["tier"],
  parameters_schema: { tier: { type: "string", enum: ["standard", "preferred"] } },
  submission_criteria: { property: "state", operator: "equals", value: "open" },
  enabled: true,
};

describe("Ontology Manager 对象类型详情", () => {
  beforeEach(() => {
    routeState.query = { type: "customer", tab: "actions" };
    routerMock.replace.mockReset();
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/ontology") return Promise.resolve([ontology]);
      if (path === "/api/object-types") return Promise.resolve([customer]);
      if (path === "/api/link-types") return Promise.resolve([]);
      if (path === "/api/actions") return Promise.resolve([action]);
      if (path === "/api/data-sources") return Promise.resolve([]);
      if (path === "/api/objects") return Promise.resolve({ total: 3 });
      if (path === "/api/audit-events") return Promise.resolve({ data: [], total: 0 });
      return Promise.resolve([]);
    });
  });

  it("按路由选择对象类型并呈现 Actions 配置和九个详情视图", async () => {
    const wrapper = mountOntology();
    await flushPromises();

    expect(wrapper.text()).toContain("调整客户等级");
    expect(wrapper.text()).toContain("参数 schema");
    expect(wrapper.text()).toContain("提交条件");
    for (const tab of ["概览", "属性", "链接", "Actions", "数据", "依赖", "使用情况", "安全", "历史"]) {
      expect(wrapper.text()).toContain(tab);
    }
  });

  it("显示对象属性的类型、必填和敏感配置", async () => {
    routeState.query = { type: "customer", tab: "properties" };
    const wrapper = mountOntology();
    await flushPromises();

    expect(wrapper.text()).toContain("客户编号");
    expect(wrapper.text()).toContain("唯一值");
    expect(wrapper.text()).toContain("敏感字段");
  });

  it("切换详情视图时更新深链接 query", async () => {
    const wrapper = mountOntology();
    await flushPromises();
    await wrapper.findAll(".resource-detail-tabs button").find((button) => button.text() === "属性")!.trigger("click");

    expect(routerMock.replace).toHaveBeenCalledWith({ query: { type: "customer", tab: "properties" } });
  });
});
