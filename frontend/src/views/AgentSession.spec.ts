import { beforeEach, describe, expect, it, vi } from "vitest";
import { flushPromises, mount } from "@vue/test-utils";
import type { AgentConfiguration } from "../types";

const apiMock = vi.hoisted(() => ({ get: vi.fn(), post: vi.fn() }));
const routerMock = vi.hoisted(() => ({ push: vi.fn() }));

vi.mock("../api/client", () => ({
  api: apiMock,
  readableError: (error: unknown) => (error instanceof Error ? error.message : "请求失败"),
}));
vi.mock("vue-router", () => ({
  useRoute: () => ({ params: { sessionId: "session-1" } }),
  useRouter: () => routerMock,
}));

import AgentSession from "./AgentSession.vue";

const detail: {
  id: string;
  agent_id: string;
  agent_version_id: string;
  version_number: number;
  status: string;
  inputs: Record<string, unknown>;
  origin_resource: string;
  created_at: string;
  closed_at: string | null;
  config: AgentConfiguration;
  events: Array<{ id: string; sequence: number; event_type: string; tool_name: string | null; status: string; details: Record<string, unknown>; created_at: string }>;
} = {
  id: "session-1",
  agent_id: "agent-1",
  agent_version_id: "version-2",
  version_number: 2,
  status: "active",
  inputs: { customer_id: "C-100" },
  origin_resource: "Workshop",
  created_at: "2026-11-15T02:30:00Z",
  closed_at: null,
  config: {
    model_provider: "local",
    model_name: "确定性本地预览",
    system_prompt: "你是运营助理。",
    initial_user_message: "检查客户 {{customer_id}}",
    inputs: [{ name: "customer_id", display_name: "客户编号", type: "string", required: true, sensitive: false }],
    precomputed_variables: [],
    allowed_tools: ["search_objects"],
    allowed_actions: [],
    session_completion: { mode: "stays_open", output_schema: {} },
  },
  events: [
    { id: "event-1", sequence: 1, event_type: "session.created", tool_name: null, status: "succeeded", details: { version_number: 2 }, created_at: "2026-11-15T02:30:00Z" },
    { id: "event-2", sequence: 2, event_type: "tool.called", tool_name: "search_objects", status: "succeeded", details: { result: { total: 1 } }, created_at: "2026-11-15T02:31:00Z" },
  ],
};

describe("Agent Manager 会话检查器", () => {
  beforeEach(() => {
    apiMock.get.mockReset();
    apiMock.post.mockReset();
    routerMock.push.mockReset();
    apiMock.get.mockResolvedValue(detail);
    apiMock.post.mockResolvedValue({ ...detail, status: "cancelled", closed_at: "2026-11-15T02:32:00Z" });
  });

  it("固定显示运行版本、来源、输入和按序排列的工具事件", async () => {
    const wrapper = mount(AgentSession, { global: { stubs: { RouterLink: true } } });
    await flushPromises();

    expect(apiMock.get).toHaveBeenCalledWith("/api/sessions/session-1", undefined, "/agent-api");
    expect(wrapper.text()).toContain("版本 2");
    expect(wrapper.text()).toContain("Workshop");
    expect(wrapper.text()).toContain("C-100");
    expect(wrapper.text()).toContain("search_objects");
    expect(wrapper.text()).toContain("事件 02");
  });

  it("由运行管理员取消活动会话并刷新服务状态", async () => {
    const wrapper = mount(AgentSession, { global: { stubs: { RouterLink: true } } });
    await flushPromises();
    await wrapper.get('[data-action="cancel-session"]').trigger("click");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/sessions/session-1/cancel", {}, "/agent-api");
    expect(wrapper.text()).toContain("已取消");
  });

  it("为已配置模型的会话显示对话记录并提交新消息", async () => {
    const modelDetail = structuredClone(detail);
    modelDetail.config.model_provider = "openai-compatible";
    modelDetail.events.push(
      { id: "event-3", sequence: 3, event_type: "message.initial", tool_name: null, status: "succeeded", details: { content: "检查客户 C-100" } as (typeof modelDetail.events)[number]["details"], created_at: "2026-11-15T02:32:00Z" },
      { id: "event-4", sequence: 4, event_type: "message.assistant", tool_name: null, status: "succeeded", details: { content: "客户状态正常。" } as (typeof modelDetail.events)[number]["details"], created_at: "2026-11-15T02:33:00Z" },
    );
    apiMock.get.mockResolvedValue(modelDetail);
    apiMock.post.mockResolvedValue({ session_id: "session-1", assistant_message: "最近一周没有新增订单。", tool_calls: ["search_objects"], status: "active" });
    const wrapper = mount(AgentSession, { global: { stubs: { RouterLink: true } } });
    await flushPromises();

    expect(wrapper.text()).toContain("检查客户 C-100");
    expect(wrapper.text()).toContain("客户状态正常。");
    expect(wrapper.find('[aria-label="发送会话消息"]').exists()).toBe(true);

    await wrapper.get('[aria-label="会话消息"]').setValue("订单情况如何？");
    await wrapper.get('[aria-label="发送会话消息"]').trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/sessions/session-1/messages", { content: "订单情况如何？" }, "/agent-api");
    expect(apiMock.get).toHaveBeenCalledTimes(2);
  });

  it("本地预览版本明确说明不会生成模型回复", async () => {
    const wrapper = mount(AgentSession, { global: { stubs: { RouterLink: true } } });
    await flushPromises();

    expect(wrapper.text()).toContain("本地确定性预览模式");
    expect(wrapper.text()).toContain("当前版本不会生成模型回复");
    expect(wrapper.find('[aria-label="发送会话消息"]').exists()).toBe(false);
  });
});
