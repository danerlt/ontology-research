import { beforeEach, describe, expect, it, vi } from "vitest";
import { flushPromises, mount } from "@vue/test-utils";
import { createPinia, setActivePinia } from "pinia";

const apiMock = vi.hoisted(() => ({ get: vi.fn(), post: vi.fn() }));
const routerMock = vi.hoisted(() => ({ push: vi.fn() }));
const routeMock = vi.hoisted(() => ({ path: "/agents", query: {} as Record<string, unknown> }));

vi.mock("../api/client", () => ({
  api: apiMock,
  readableError: (error: unknown) => (error instanceof Error ? error.message : "请求失败"),
}));
vi.mock("vue-router", () => ({
  useRoute: () => routeMock,
  useRouter: () => routerMock,
}));

import Agents from "./Agents.vue";

const agent = {
  id: "agent-1",
  api_name: "operations_assistant",
  display_name: "运营助理",
  description: "协助查询客户和订单",
  allowed_tools: ["search_objects"],
  allowed_actions: [],
  enabled: true,
  latest_version_number: 2,
  draft_config: {
    model_provider: "local",
    model_name: "确定性本地预览",
    system_prompt: "读取客户和订单事实。",
    initial_user_message: "检查客户 {{customer_id}}",
    inputs: [{ name: "customer_id", display_name: "客户编号", type: "string", required: true, sensitive: false }],
    precomputed_variables: [],
    allowed_tools: ["search_objects"],
    allowed_actions: [],
    session_completion: { mode: "stays_open", output_schema: {} },
  },
};

describe("Agent Manager", () => {
  beforeEach(() => {
    setActivePinia(createPinia());
    apiMock.get.mockReset();
    apiMock.post.mockReset();
    routerMock.push.mockReset();
    routeMock.path = "/agents";
    routeMock.query = {};
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/agents") return Promise.resolve([agent]);
      if (path.includes("/versions")) return Promise.resolve([{ id: "version-2", version_number: 2, config: agent.draft_config, published_at: "2026-11-15T00:00:00Z" }]);
      if (path.startsWith("/api/sessions")) return Promise.resolve({ items: [], total: 0, page: 1, page_size: 50 });
      return Promise.resolve([]);
    });
  });

  it("列出已发布智能体、版本和进入构建器的入口", async () => {
    const wrapper = mount(Agents, { global: { stubs: { RouterLink: true } } });
    await flushPromises();

    expect(wrapper.text()).toContain("运营助理");
    expect(wrapper.text()).toContain("版本 2");
    expect(wrapper.text()).toContain("查询对象");
    expect(wrapper.get('[data-action="create-agent"]').attributes("to")).toBe("/agent-builder/new");
  });

  it("在会话目录按来源与状态筛选，并保留固定版本信息", async () => {
    routeMock.path = "/sessions";
    apiMock.get.mockImplementation((path: string) => path === "/api/sessions?page=1&page_size=50&status=active&origin_resource=Workshop"
      ? Promise.resolve({
        items: [{ id: "session-1", agent_id: "agent-1", agent_version_id: "version-2", version_number: 2, status: "active", inputs: {}, origin_resource: "Workshop", created_at: "2026-11-15T00:00:00Z", closed_at: null }],
        total: 1,
        page: 1,
        page_size: 50,
      })
      : path === "/api/agents" ? Promise.resolve([agent])
        : path.startsWith("/api/sessions") ? Promise.resolve({ items: [], total: 0, page: 1, page_size: 50 })
          : Promise.resolve([]));
    const wrapper = mount(Agents, { global: { stubs: { RouterLink: true } } });
    await flushPromises();
    await wrapper.get('[aria-label="来源应用筛选"]').setValue("Workshop");
    await wrapper.get('[data-action="apply-session-filters"]').trigger("click");
    await flushPromises();

    expect(apiMock.get).toHaveBeenCalledWith("/api/sessions?page=1&page_size=50&status=active&origin_resource=Workshop", undefined, "/agent-api");
    expect(wrapper.text()).toContain("Workshop");
    expect(wrapper.text()).toContain("版本 2");
  });

  it("创建会话时提交选定的发布版本、必填输入和来源", async () => {
    apiMock.post.mockResolvedValue({ id: "session-1" });
    const wrapper = mount(Agents, { global: { stubs: { RouterLink: true } } });
    await flushPromises();
    await wrapper.get('[data-action="start-session"]').trigger("click");
    await wrapper.get('[aria-label="会话输入：客户编号"]').setValue("C-100");
    await wrapper.get('[data-action="confirm-start-session"]').trigger("click");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/agents/agent-1/sessions", {
      inputs: { customer_id: "C-100" },
      version_number: 2,
      origin_resource: "本体工作台",
    }, "/agent-api");
    expect(routerMock.push).toHaveBeenCalledWith("/sessions/session-1");
  });
});
