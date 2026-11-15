import { beforeEach, describe, expect, it, vi } from "vitest";
import { flushPromises, mount } from "@vue/test-utils";
import { createPinia, setActivePinia } from "pinia";
import { useAuthStore } from "../stores/auth";

const apiMock = vi.hoisted(() => ({ get: vi.fn(), post: vi.fn(), put: vi.fn() }));
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
const projects = [
  { id: "project-a", api_name: "operations", display_name: "运营项目", description: "", role: "admin" as const },
  { id: "project-b", api_name: "supply", display_name: "供应链项目", description: "", role: "editor" as const },
];
let projectList = [...projects];

describe("工作台全局搜索", () => {
  beforeEach(() => {
    setActivePinia(createPinia());
    apiMock.get.mockReset();
    apiMock.post.mockReset();
    apiMock.put.mockReset();
    routerMock.push.mockReset();
    routeState.path = "/";
    projectList = [...projects];
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/projects") return Promise.resolve(projectList);
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

  it("切换项目后更新活动上下文并重载本体版本", async () => {
    const pinia = createPinia();
    const auth = useAuthStore(pinia);
    auth.setSession("token", { id: "user-1", email: "admin@example.com", role: "admin" }, "project-a");
    const wrapper = mount(AppShell, { global: { plugins: [pinia], stubs: { RouterLink: true, RouterView: true } } });
    await flushPromises();
    apiMock.get.mockClear();

    await wrapper.get('[aria-label="切换项目"]').setValue("project-b");
    await flushPromises();

    expect(auth.activeProjectId).toBe("project-b");
    expect(auth.role).toBe("editor");
    expect(apiMock.get).toHaveBeenCalledWith("/api/ontology");
  });

  it("管理员新建项目后自动切换到新项目", async () => {
    const created = {
      id: "project-new",
      api_name: "new_project",
      display_name: "新项目",
      description: "新建工作区",
      role: "admin" as const,
    };
    apiMock.post.mockImplementation(async () => {
      projectList.push(created);
      return created;
    });
    const pinia = createPinia();
    const auth = useAuthStore(pinia);
    auth.setSession("token", { id: "user-1", email: "admin@example.com", role: "admin" }, "project-a");
    const wrapper = mount(AppShell, { global: { plugins: [pinia], stubs: { RouterLink: true, RouterView: true } } });
    await flushPromises();

    await wrapper.get('[data-action="create-project"]').trigger("click");
    await wrapper.get('[aria-label="项目显示名称"]').setValue("新项目");
    await wrapper.get('[aria-label="项目 API 名称"]').setValue("new_project");
    await wrapper.get(".project-create-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/projects", {
      api_name: "new_project",
      display_name: "新项目",
      description: "",
    });
    expect(auth.activeProjectId).toBe("project-new");
  });

  it("项目管理员可以维护成员角色", async () => {
    const member = { id: "membership-1", user_id: "user-2", email: "editor@example.com", role: "editor" as const };
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/projects") return Promise.resolve(projectList);
      if (path === "/api/projects/project-a/members") return Promise.resolve([member]);
      return Promise.resolve([]);
    });
    apiMock.put.mockResolvedValue({ ...member, role: "viewer" });
    const pinia = createPinia();
    const auth = useAuthStore(pinia);
    auth.setSession("token", { id: "user-1", email: "admin@example.com", role: "admin" }, "project-a");
    const wrapper = mount(AppShell, { global: { plugins: [pinia], stubs: { RouterLink: true, RouterView: true } } });
    await flushPromises();

    await wrapper.get('[data-action="manage-project-members"]').trigger("click");
    await flushPromises();
    await wrapper.get('[aria-label="项目成员邮箱"]').setValue("editor@example.com");
    await wrapper.get('[aria-label="项目成员角色"]').setValue("viewer");
    await wrapper.get(".member-form").trigger("submit");
    await flushPromises();

    expect(apiMock.get).toHaveBeenCalledWith("/api/projects/project-a/members");
    expect(apiMock.put).toHaveBeenCalledWith("/api/projects/project-a/members", {
      email: "editor@example.com",
      role: "viewer",
    });
    expect(wrapper.get('[role="status"]').text()).toContain("角色已保存");
  });
});
