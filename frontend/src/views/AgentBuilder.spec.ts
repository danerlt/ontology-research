import { beforeEach, describe, expect, it, vi } from "vitest";
import { flushPromises, mount } from "@vue/test-utils";

const apiMock = vi.hoisted(() => ({ get: vi.fn(), post: vi.fn(), put: vi.fn() }));
const routerMock = vi.hoisted(() => ({ push: vi.fn() }));

vi.mock("../api/client", () => ({
  api: apiMock,
  readableError: (error: unknown) => (error instanceof Error ? error.message : "请求失败"),
}));
vi.mock("vue-router", () => ({
  useRoute: () => ({ params: { agentId: "agent-1" } }),
  useRouter: () => routerMock,
}));

import AgentBuilder from "./AgentBuilder.vue";

const draftConfig = {
  model_provider: "local",
  model_name: "确定性本地预览",
  system_prompt: "你是客户运营助理。",
  initial_user_message: "检查客户 {{customer_id}}",
  inputs: [{ name: "customer_id", display_name: "客户编号", type: "string", required: true, sensitive: false }],
  precomputed_variables: [],
  allowed_tools: ["search_objects"],
  allowed_actions: [],
  session_completion: { mode: "stays_open", output_schema: {} },
};

const agent = {
  id: "agent-1",
  api_name: "operations_assistant",
  display_name: "运营助理",
  description: "从本体中读取客户信息",
  allowed_tools: ["search_objects"],
  allowed_actions: [],
  enabled: true,
  draft_config: draftConfig,
  latest_version_number: 2,
};
const version = {
  id: "version-2",
  agent_id: "agent-1",
  version_number: 2,
  config: draftConfig,
  created_by: "admin-1",
  published_at: "2026-11-15T00:00:00Z",
};

describe("Agent Builder", () => {
  beforeEach(() => {
    apiMock.get.mockReset();
    apiMock.post.mockReset();
    apiMock.put.mockReset();
    routerMock.push.mockReset();
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/agents/agent-1/versions") return Promise.resolve([version]);
      if (path === "/api/agent-runtime/capabilities") return Promise.resolve({ providers: [
        { id: "local", display_name: "本地确定性预览", available: true, model_name: "确定性本地预览", credential_source: "无需外部凭据" },
        { id: "openai-compatible", display_name: "OpenAI 兼容接口", available: true, model_name: "gpt-compatible", credential_source: "服务端环境配置" },
      ] });
      return Promise.resolve(agent);
    });
    apiMock.put.mockResolvedValue(agent);
    apiMock.post.mockResolvedValue({
      mode: "deterministic_dry_run",
      model_provider: "local",
      model_name: "确定性本地预览",
      rendered_prompt: "你是客户运营助理。\n\n初始用户消息：检查客户 C-100",
      initial_user_message: "检查客户 C-100",
      variables: [],
      allowed_tools: ["search_objects"],
      allowed_actions: [],
      notices: ["这是确定性本地预览；未调用模型、工具或 Ontology Action。"],
    });
  });

  it("按配置页签展示模型、提示词、输入和已发布版本", async () => {
    const wrapper = mount(AgentBuilder, { global: { stubs: { RouterLink: true } } });
    await flushPromises();

    expect(wrapper.text()).toContain("运营助理");
    expect(wrapper.text()).toContain("模型与提示词");
    expect(wrapper.text()).toContain("输入与变量");
    expect(wrapper.text()).toContain("版本 2");
    expect(wrapper.find('[aria-label="系统提示词"]').exists()).toBe(true);
  });

  it("保存草稿并从用户输入启动无副作用本地预览", async () => {
    const wrapper = mount(AgentBuilder, { global: { stubs: { RouterLink: true } } });
    await flushPromises();
    await wrapper.get('[aria-label="系统提示词"]').setValue("你是客户风险分析助理。{{customer_id}}");
    await wrapper.get('[data-action="save-draft"]').trigger("click");
    await flushPromises();
    await wrapper.get('[aria-label="预览输入：客户编号"]').setValue("C-100");
    await wrapper.get('[data-action="run-preview"]').trigger("click");
    await flushPromises();

    expect(apiMock.put).toHaveBeenCalledWith("/api/agents/agent-1", {
      draft_config: expect.objectContaining({ system_prompt: "你是客户风险分析助理。{{customer_id}}" }),
    }, "/agent-api");
    expect(apiMock.post).toHaveBeenCalledWith("/api/agents/agent-1/preview", {
      inputs: { customer_id: "C-100" },
    }, "/agent-api");
    expect(wrapper.text()).toContain("未调用模型、工具或 Ontology Action");
    expect(wrapper.text()).toContain("检查客户 C-100");
  });

  it("发布前先保存当前草稿并展示服务端返回的版本号", async () => {
    apiMock.post.mockResolvedValueOnce({ id: "version-3", version_number: 3, config: draftConfig });
    const wrapper = mount(AgentBuilder, { global: { stubs: { RouterLink: true } } });
    await flushPromises();
    await wrapper.get('[data-action="publish-agent"]').trigger("click");
    await flushPromises();

    expect(apiMock.put).toHaveBeenCalledWith("/api/agents/agent-1", {
      draft_config: expect.objectContaining({ system_prompt: draftConfig.system_prompt }),
    }, "/agent-api");
    expect(apiMock.post).toHaveBeenCalledWith("/api/agents/agent-1/publish", {}, "/agent-api");
    expect(wrapper.text()).toContain("版本 3 已发布");
  });

  it("按服务端运行时能力开放模型并显示凭据来源", async () => {
    const wrapper = mount(AgentBuilder, { global: { stubs: { RouterLink: true } } });
    await flushPromises();

    const provider = wrapper.get('[aria-label="模型提供方"]');
    expect(provider.find('option[value="openai-compatible"]').element.hasAttribute("disabled")).toBe(false);
    expect(wrapper.text()).toContain("服务端环境配置");

    await provider.setValue("openai-compatible");
    expect((provider.element as HTMLSelectElement).value).toBe("openai-compatible");
  });

  it("运行时未配置时禁用模型并解释原因", async () => {
    apiMock.get.mockImplementation((path: string) => path === "/api/agent-runtime/capabilities"
      ? Promise.resolve({ providers: [
        { id: "local", display_name: "本地确定性预览", available: true, model_name: "确定性本地预览", credential_source: "无需外部凭据" },
        { id: "openai-compatible", display_name: "OpenAI 兼容接口", available: false, model_name: "", credential_source: "尚未配置服务端地址与密钥" },
      ] })
      : path === "/api/agents/agent-1/versions" ? Promise.resolve([version]) : Promise.resolve(agent));
    const wrapper = mount(AgentBuilder, { global: { stubs: { RouterLink: true } } });
    await flushPromises();

    expect(wrapper.get('[aria-label="模型提供方"]').find('option[value="openai-compatible"]').element.hasAttribute("disabled")).toBe(true);
    expect(wrapper.text()).toContain("尚未配置服务端地址与密钥");
  });
});
