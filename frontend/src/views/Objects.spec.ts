import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";
import Objects from "./Objects.vue";

const apiMock = vi.hoisted(() => ({ get: vi.fn(), post: vi.fn() }));

vi.mock("../api/client", () => ({
  api: apiMock,
  readableError: (error: unknown) => String(error),
}));
const routeState = vi.hoisted(() => ({ query: {} as Record<string, unknown> }));
vi.mock("vue-router", () => ({ useRoute: () => routeState }));

const ontology = { id: "ontology-1", api_name: "operations", display_name: "运营本体", revision: 4 };
const objectType = {
  id: "type-1",
  ontology_id: "ontology-1",
  api_name: "customer",
  display_name: "客户",
  description: "客户资料",
  primary_key_property: "id",
  properties: [
    { id: "p-id", api_name: "id", display_name: "编号", data_type: "string", required: true, editable: false, unique_value: true, options: {} },
    { id: "p-tier", api_name: "tier", display_name: "等级", data_type: "enum", required: false, editable: true, unique_value: false, options: { choices: ["standard", "preferred"] } },
  ],
};
const record = {
  id: "object-1",
  object_type_api_name: "customer",
  object_type_display_name: "客户",
  primary_key_value: "C-100",
  properties: { id: "C-100", tier: "standard" },
  version: 1,
  links: [],
};
const action = {
  id: "action-1",
  api_name: "set_customer_tier",
  display_name: "调整客户等级",
  description: "调整客户分层",
  object_type_api_name: "customer",
  allowed_properties: ["tier"],
  parameters_schema: { tier: { required: true, type: "string", enum: ["standard", "preferred"] } },
  submission_criteria: {},
  enabled: true,
};

describe("对象 Action 预览", () => {
  beforeEach(() => {
    apiMock.get.mockReset();
    apiMock.post.mockReset();
    routeState.query = {};
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/ontology") return Promise.resolve([ontology]);
      if (path === "/api/object-types") return Promise.resolve([objectType]);
      if (path === "/api/actions") return Promise.resolve([action]);
      if (path === "/api/objects") return Promise.resolve({ items: [record], total: 1 });
      if (path === "/api/objects/object-1") return Promise.resolve(record);
      return Promise.resolve([]);
    });
    apiMock.post.mockImplementation((path: string) => {
      if (path.endsWith("/preview")) {
        return Promise.resolve({
          action_api_name: action.api_name,
          object_id: record.id,
          current_version: 1,
          next_version: 2,
          property_changes: [{ property: "tier", before: "standard", after: "preferred", sensitive: false }],
        });
      }
      return Promise.resolve({ ...record, properties: { ...record.properties, tier: "preferred" }, version: 2 });
    });
  });

  it("先向服务端请求影响预览，确认后才提交 Action", async () => {
    const wrapper = mount(Objects);
    await flushPromises();
    await wrapper.get(".object-result").trigger("click");
    await flushPromises();
    await wrapper.get('[aria-label="等级"]').setValue("preferred");
    await wrapper.get('[aria-label="预览 Action"]').trigger("click");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/actions/set_customer_tier/preview", {
      object_id: "object-1",
      expected_version: 1,
      parameters: { tier: "preferred" },
    });
    expect(wrapper.text()).toContain("standard");
    expect(wrapper.text()).toContain("preferred");
    expect(apiMock.post).not.toHaveBeenCalledWith("/api/actions/set_customer_tier/execute", expect.anything());

    await wrapper.get('[aria-label="确认执行 Action"]').trigger("click");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/actions/set_customer_tier/execute", {
      object_id: "object-1",
      expected_version: 1,
      parameters: { tier: "preferred" },
    });
  });

  it("分页查询对象并保留总记录数", async () => {
    apiMock.get.mockImplementation((path: string, query: Record<string, unknown> = {}) => {
      if (path === "/api/ontology") return Promise.resolve([ontology]);
      if (path === "/api/object-types") return Promise.resolve([objectType]);
      if (path === "/api/actions") return Promise.resolve([action]);
      if (path === "/api/objects" && query.page === 2) return Promise.resolve({ items: [{ ...record, id: "object-2", primary_key_value: "C-200", properties: { id: "C-200", tier: "preferred" } }], total: 27, page: 2, page_size: 25 });
      if (path === "/api/objects") return Promise.resolve({ items: [record], total: 27, page: 1, page_size: 25 });
      if (path === "/api/objects/object-1") return Promise.resolve(record);
      return Promise.resolve([]);
    });
    const wrapper = mount(Objects);
    await flushPromises();

    expect(wrapper.text()).toContain("27 条记录");
    expect(wrapper.text()).toContain("第 1 / 2 页");
    await wrapper.get('[data-action="next-object-page"]').trigger("click");
    await flushPromises();

    expect(apiMock.get).toHaveBeenCalledWith("/api/objects", {
      ontology_id: ontology.id,
      object_type_api_name: "customer",
      query: "",
      page: 2,
      page_size: 25,
      sort_by: "created_at",
      sort_order: "desc",
    });
    expect(wrapper.text()).toContain("C-200");
    expect(wrapper.text()).toContain("第 2 / 2 页");
  });

  it("通过 URL 参数恢复对象类型、搜索词和选中的记录", async () => {
    routeState.query = { type: "customer", query: "C-100", record: "object-1" };
    const wrapper = mount(Objects);
    await flushPromises();

    expect(apiMock.get).toHaveBeenCalledWith("/api/objects", {
      ontology_id: ontology.id,
      object_type_api_name: "customer",
      query: "C-100",
      page: 1,
      page_size: 25,
      sort_by: "created_at",
      sort_order: "desc",
    });
    expect(wrapper.text()).toContain("C-100");
    expect(wrapper.findAll(".object-detail-header")).toHaveLength(1);
  });
});
