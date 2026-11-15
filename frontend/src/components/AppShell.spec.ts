import { beforeEach, describe, expect, it, vi } from "vitest";
import { flushPromises, mount } from "@vue/test-utils";
import { createPinia, setActivePinia } from "pinia";

const apiMock = vi.hoisted(() => ({ get: vi.fn() }));
const routerMock = vi.hoisted(() => ({ push: vi.fn() }));
const routeState = vi.hoisted(() => ({ path: "/" }));

vi.mock("../api/client", () => ({ api: apiMock }));
vi.mock("vue-router", () => ({
  useRoute: () => routeState,
  useRouter: () => routerMock,
}));

import AppShell from "./AppShell.vue";

const ontology = { id: "ontology-1", api_name: "operations", display_name: "运营本体", revision: 12, object_type_count: 1, link_type_count: 0 };
const customerType = {
  id: "type-1", ontology_id: "ontology-1", api_name: "customer", display_name: "客户", description: "客户档案", primary_key_property: "customer_id",
  properties: [{ id: "prop-1", api_name: "customer_id", display_name: "客户编号", data_type: "string", required: true, editable: false, unique_value: true, options: {} }],
};

describe("工作台全局搜索", () => {
  beforeEach(() => {
    setActivePinia(createPinia());
    apiMock.get.mockReset();
    routerMock.push.mockReset();
    routeState.path = "/";
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/ontology") return Promise.resolve([ontology]);
      if (path === "/api/object-types") return Promise.resolve([customerType]);
      if (path === "/api/link-types" || path === "/api/actions" || path === "/api/data-sources" || path === "/api/proposals") return Promise.resolve([]);
      if (path === "/api/objects") return Promise.resolve({ items: [], total: 0, page: 1, page_size: 8 });
      if (path === "/agent-api/api/agents") return Promise.resolve([]);
      if (path === "/api/sessions") return Promise.resolve({ items: [], total: 0, page: 1, page_size: 8 });
      return Promise.resolve([]);
    });
  });

  it("从全局命令面板搜索本体资源并打开对象类型", async () => {
    const wrapper = mount(AppShell, { global: { stubs: { RouterLink: true, RouterView: true } } });
    await flushPromises();
    await wrapper.get('[data-action="open-global-search"]').trigger("click");
    await wrapper.get('[aria-label="全局搜索"]').setValue("客户");
    await wrapper.get('[data-action="run-global-search"]').trigger("click");
    await flushPromises();

    expect(apiMock.get).toHaveBeenCalledWith("/api/object-types", { ontology_id: "ontology-1" });
    expect(wrapper.get('[data-result="object_type:customer"]').text()).toContain("客户");
    await wrapper.get('[data-result="object_type:customer"]').trigger("click");

    expect(routerMock.push).toHaveBeenCalledWith("/ontology?type=customer");
  });

  it("支持 Ctrl+K 打开搜索并用 Escape 关闭", async () => {
    const wrapper = mount(AppShell, { global: { stubs: { RouterLink: true, RouterView: true } } });
    await flushPromises();
    await wrapper.trigger("keydown", { key: "k", ctrlKey: true });

    expect(wrapper.findAll('[aria-label="全局搜索"]')).toHaveLength(1);
    await wrapper.get('[aria-label="全局搜索"]').trigger("keydown", { key: "Escape" });
    expect(wrapper.findAll('[aria-label="全局搜索"]')).toHaveLength(0);
  });
});
