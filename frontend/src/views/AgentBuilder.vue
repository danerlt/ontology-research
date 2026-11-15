<script setup lang="ts">
import { computed, onMounted, reactive, ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { api, readableError } from "../api/client";
import type { AgentConfiguration, AgentDefinition, AgentInputDefinition, AgentVariableDefinition, AgentVersion } from "../types";

const route = useRoute();
const router = useRouter();
const routeAgentId = computed(() => String(route.params.agentId || "new"));
const agentId = ref("");
const displayName = ref("");
const apiName = ref("");
const description = ref("");
const config = ref<AgentConfiguration>(newConfiguration());
const activePanel = ref("model");
const versions = ref<AgentVersion[]>([]);
const previewValues = reactive<Record<string, unknown>>({});
const previewResult = ref<PreviewResult | null>(null);
const outputSchemaText = ref("{}");
const savedOutputSchemaText = ref("{}");
const savedSnapshot = ref("");
const error = ref("");
const notice = ref("");
const busy = ref(false);
const runtimeProviders = ref<Array<{ id: string; display_name: string; available: boolean; model_name: string; credential_source: string }>>([]);
const runtimeNotice = ref("");

interface PreviewResult {
  mode: string;
  model_provider: string;
  model_name: string;
  rendered_prompt: string;
  initial_user_message: string;
  variables: Array<{ name: string; expression: string; status: string; value: string }>;
  allowed_tools: string[];
  allowed_actions: string[];
  notices: string[];
}

const panels = [
  { id: "model", label: "模型与提示词", index: "配置" },
  { id: "inputs", label: "输入与变量", index: "输入" },
  { id: "tools", label: "工具与权限", index: "工具" },
  { id: "completion", label: "完成与输出", index: "输出" },
];
const toolOptions = [
  { id: "search_objects", name: "查询对象", description: "按类型和条件查找本体对象" },
  { id: "get_object", name: "读取对象", description: "读取单个对象及允许显示的属性" },
  { id: "execute_action", name: "执行 Action", description: "仅执行此 Agent 明确获准的 Action" },
];
const isDirty = computed(() => JSON.stringify(config.value) !== savedSnapshot.value || outputSchemaText.value !== savedOutputSchemaText.value);
const isNew = computed(() => !agentId.value);

function newConfiguration(): AgentConfiguration {
  return {
    model_provider: "local",
    model_name: "确定性本地预览",
    system_prompt: "",
    initial_user_message: "",
    inputs: [],
    precomputed_variables: [],
    allowed_tools: ["search_objects"],
    allowed_actions: [],
    session_completion: { mode: "stays_open", output_schema: {} },
  };
}

function cloneConfiguration(value: AgentConfiguration): AgentConfiguration {
  return JSON.parse(JSON.stringify(value)) as AgentConfiguration;
}

async function loadAgent() {
  error.value = "";
  await loadRuntimeCapabilities();
  if (routeAgentId.value === "new") {
    agentId.value = "";
    displayName.value = "";
    apiName.value = "";
    description.value = "";
    config.value = newConfiguration();
    savedSnapshot.value = JSON.stringify(config.value);
    savedOutputSchemaText.value = outputSchemaText.value;
    return;
  }
  try {
    const [agent, versionRows] = await Promise.all([
      api.get<AgentDefinition>(`/api/agents/${routeAgentId.value}`, undefined, "/agent-api"),
      api.get<AgentVersion[]>(`/api/agents/${routeAgentId.value}/versions`, undefined, "/agent-api"),
    ]);
    agentId.value = agent.id;
    displayName.value = agent.display_name;
    apiName.value = agent.api_name;
    description.value = agent.description;
    config.value = cloneConfiguration(agent.draft_config);
    outputSchemaText.value = JSON.stringify(config.value.session_completion.output_schema ?? {}, null, 2);
    savedOutputSchemaText.value = outputSchemaText.value;
    versions.value = versionRows;
    for (const key of Object.keys(previewValues)) delete previewValues[key];
    for (const input of config.value.inputs) previewValues[input.name] = input.type === "boolean" ? false : "";
    savedSnapshot.value = JSON.stringify(config.value);
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function loadRuntimeCapabilities() {
  runtimeNotice.value = "";
  try {
    const response = await api.get<{ providers: Array<{ id: string; display_name: string; available: boolean; model_name: string; credential_source: string }> }>(
      "/api/agent-runtime/capabilities",
      undefined,
      "/agent-api",
    );
    runtimeProviders.value = response.providers;
  } catch (cause) {
    runtimeProviders.value = [
      { id: "local", display_name: "本地确定性预览", available: true, model_name: "确定性本地预览", credential_source: "无需外部凭据" },
      { id: "openai-compatible", display_name: "OpenAI 兼容接口", available: false, model_name: "", credential_source: "无法读取服务端运行时能力" },
    ];
    runtimeNotice.value = readableError(cause);
  }
}

function selectProvider(event: Event) {
  const target = event.target;
  if (!(target instanceof HTMLSelectElement)) return;
  const provider = runtimeProviders.value.find((item) => item.id === target.value && item.available);
  if (!provider) return;
  config.value.model_provider = provider.id;
  if (!config.value.model_name || config.value.model_name === "确定性本地预览") {
    config.value.model_name = provider.model_name;
  }
}

function applyOutputSchema() {
  try {
    const parsed = JSON.parse(outputSchemaText.value) as unknown;
    if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
      throw new Error("输出结构必须是 JSON 对象。");
    }
    config.value.session_completion.output_schema = parsed as Record<string, unknown>;
    return true;
  } catch (cause) {
    error.value = cause instanceof Error ? cause.message : "输出结构 JSON 无效。";
    return false;
  }
}

async function saveDraft(showNotice = true): Promise<boolean> {
  if (busy.value) return false;
  error.value = "";
  if (!applyOutputSchema()) return false;
  busy.value = true;
  try {
    if (isNew.value) {
      const created = await api.post<AgentDefinition>("/api/agents", {
        api_name: apiName.value,
        display_name: displayName.value,
        description: description.value,
        allowed_tools: config.value.allowed_tools,
        allowed_actions: config.value.allowed_actions,
        draft_config: config.value,
      }, "/agent-api");
      agentId.value = created.id;
      savedSnapshot.value = JSON.stringify(config.value);
      savedOutputSchemaText.value = outputSchemaText.value;
      await router.push(`/agent-builder/${created.id}`);
    } else {
      await api.put<AgentDefinition>(`/api/agents/${agentId.value}`, { draft_config: config.value }, "/agent-api");
      savedSnapshot.value = JSON.stringify(config.value);
      savedOutputSchemaText.value = outputSchemaText.value;
    }
    if (showNotice) notice.value = "草稿已保存。发布前可以继续调整配置。";
    return true;
  } catch (cause) {
    error.value = readableError(cause);
    return false;
  } finally {
    busy.value = false;
  }
}

async function loadVersions() {
  if (!agentId.value) return;
  try {
    versions.value = await api.get<AgentVersion[]>(`/api/agents/${agentId.value}/versions`, undefined, "/agent-api");
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function publishAgent() {
  if (!(await saveDraft(false)) || !agentId.value) return;
  busy.value = true;
  error.value = "";
  try {
    const version = await api.post<AgentVersion>(`/api/agents/${agentId.value}/publish`, {}, "/agent-api");
    notice.value = `版本 ${version.version_number} 已发布。新会话将固定到此版本。`;
    versions.value = [version, ...versions.value];
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

function addInput() {
  const name = `input_${config.value.inputs.length + 1}`;
  const input: AgentInputDefinition = {
    name,
    display_name: `输入 ${config.value.inputs.length + 1}`,
    type: "string",
    required: true,
    sensitive: false,
  };
  config.value.inputs.push(input);
  previewValues[name] = "";
  activePanel.value = "inputs";
}

function removeInput(name: string) {
  config.value.inputs = config.value.inputs.filter((item) => item.name !== name);
  delete previewValues[name];
}

function addVariable() {
  const index = config.value.precomputed_variables.length + 1;
  const variable: AgentVariableDefinition = { name: `context_${index}`, expression: "input.customer_id" };
  config.value.precomputed_variables.push(variable);
  activePanel.value = "inputs";
}

function toggleTool(toolName: string) {
  const tools = new Set(config.value.allowed_tools);
  if (tools.has(toolName)) tools.delete(toolName);
  else tools.add(toolName);
  config.value.allowed_tools = [...tools];
}

function setActionScopeFromEvent(event: Event) {
  const target = event.target;
  if (!(target instanceof HTMLInputElement)) return;
  config.value.allowed_actions = target.value.split(",").map((name) => name.trim()).filter(Boolean);
}

async function runPreview() {
  if (!(await saveDraft(false)) || !agentId.value) return;
  busy.value = true;
  error.value = "";
  previewResult.value = null;
  try {
    previewResult.value = await api.post<PreviewResult>(`/api/agents/${agentId.value}/preview`, {
      inputs: { ...previewValues },
    }, "/agent-api");
    notice.value = "本地预览完成；没有写入本体对象。";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

watch(routeAgentId, () => loadAgent());
onMounted(loadAgent);
</script>

<template>
  <main class="agent-builder page-content">
    <header class="builder-header">
      <div class="builder-title-group">
        <RouterLink class="builder-back-link" to="/agents">← 返回 Agent 管理</RouterLink>
        <div class="builder-title-line">
          <div>
            <h1>{{ displayName || "新建 Agent" }}</h1>
            <p>{{ description || "配置 Agent 指令、输入、预计算变量和可执行工具。" }}</p>
            <code v-if="!isNew" class="builder-api-name">{{ apiName }}</code>
          </div>
          <span v-if="!isNew" class="builder-version-badge">最新发布 {{ versions[0] ? `v${versions[0].version_number}` : "尚未发布" }}</span>
        </div>
      </div>
      <div class="builder-header-actions">
        <span v-if="isDirty" class="builder-draft-state">有未保存的配置</span>
        <button class="button button-quiet" data-action="save-draft" :disabled="busy || !displayName || !apiName" @click="saveDraft()">保存草稿</button>
        <button class="button button-primary" data-action="publish-agent" :disabled="busy || !agentId && (!displayName || !apiName)" @click="publishAgent">发布版本</button>
      </div>
    </header>

    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div>
    <div v-if="notice" class="notice notice-success" role="status">{{ notice }}</div>

    <div class="builder-layout">
      <aside class="builder-outline">
        <div class="builder-outline-heading"><strong>配置目录</strong><span>{{ panels.length }} 个区域</span></div>
        <nav aria-label="Agent 配置目录">
          <button v-for="(panel, index) in panels" :key="panel.id" :class="{ active: activePanel === panel.id }" @click="activePanel = panel.id">
            <span>{{ String(index + 1).padStart(2, "0") }}</span>{{ panel.label }}
          </button>
        </nav>
        <section class="builder-version-list">
          <div class="builder-outline-heading"><strong>已发布版本</strong><button class="text-button" @click="loadVersions">刷新</button></div>
          <p v-if="!versions.length" class="builder-empty-note">保存草稿并发布后，版本会显示在这里。</p>
          <article v-for="version in versions" :key="version.id" class="builder-version-row">
            <strong>版本 {{ version.version_number }}</strong>
            <time>{{ new Date(version.published_at).toLocaleString("zh-CN") }}</time>
            <small>{{ version.config.model_provider }} / {{ version.config.model_name }}</small>
          </article>
        </section>
      </aside>

      <section class="builder-editor" aria-label="Agent 配置编辑器">
        <template v-if="isNew">
          <div class="builder-section-heading"><div><h2>Agent 基本信息</h2><p>为这个工作流设置稳定的名称和 API 标识。</p></div></div>
          <div class="builder-form-grid">
            <label>显示名称<input v-model="displayName" aria-label="Agent 显示名称" placeholder="客户运营助理" /></label>
            <label>API 名称<input v-model="apiName" aria-label="Agent API 名称" pattern="[a-z][a-z0-9_]*" placeholder="customer_operations" /></label>
          </div>
          <label class="builder-wide-field">说明<input v-model="description" aria-label="Agent 说明" placeholder="说明此 Agent 的工作范围" /></label>
        </template>

        <template v-if="activePanel === 'model'">
          <div class="builder-section-heading"><div><h2>模型与提示词</h2><p>明确模型来源、系统约束和启动时的任务说明。</p></div><span class="builder-config-count">{{ config.model_provider === "local" ? "本地模式" : config.model_provider }}</span></div>
          <div class="builder-form-grid">
            <label>模型提供方<select :value="config.model_provider" aria-label="模型提供方" @change="selectProvider"><option v-for="provider in runtimeProviders" :key="provider.id" :value="provider.id" :disabled="!provider.available">{{ provider.display_name }}{{ provider.available ? "" : "（不可用）" }}</option></select></label>
            <label>模型名称<input v-model="config.model_name" aria-label="模型名称" placeholder="由部署环境配置" /></label>
          </div>
          <div v-if="runtimeProviders.length" class="builder-runtime-capabilities" aria-label="模型运行时状态">
            <div v-for="provider in runtimeProviders" :key="provider.id"><strong>{{ provider.display_name }}</strong><span :class="provider.available ? 'runtime-available' : 'runtime-unavailable'">{{ provider.available ? "可用" : "不可用" }}</span><small>{{ provider.credential_source }}</small></div>
          </div>
          <div v-if="runtimeNotice" class="notice notice-error" role="alert">运行时能力读取失败：{{ runtimeNotice }}</div>
          <label class="builder-wide-field">系统提示词<textarea v-model="config.system_prompt" aria-label="系统提示词" rows="10" placeholder="描述 Agent 的职责、规则、可用上下文和拒答边界。使用 {{input_name}} 插入输入或变量。" /></label>
          <label class="builder-wide-field">初始用户消息<textarea v-model="config.initial_user_message" aria-label="初始用户消息" rows="5" placeholder="为每次会话提供第一条任务指令。可以插入配置的输入和变量。" /></label>
          <div class="builder-note"><strong>预览边界</strong><span>当前环境使用确定性本地预览，不会伪装成模型推理。模型服务凭据由部署环境管理，不写入此配置。</span></div>
        </template>

        <template v-else-if="activePanel === 'inputs'">
          <div class="builder-section-heading"><div><h2>输入与预计算变量</h2><p>声明会话启动参数，并把确定性的上下文步骤接入提示词。</p></div><div class="builder-inline-actions"><button class="button button-quiet" @click="addVariable">添加变量</button><button class="button button-primary" @click="addInput">添加输入</button></div></div>
          <div class="builder-subheading"><strong>会话输入</strong><span>{{ config.inputs.length }} 个输入</span></div>
          <div v-if="config.inputs.length" class="builder-definition-table">
            <div class="builder-definition-head"><span>显示名称 / API 名称</span><span>类型</span><span>会话约束</span><span /></div>
            <div v-for="input in config.inputs" :key="input.name" class="builder-input-row">
              <div class="builder-input-identity"><input v-model="input.display_name" :aria-label="`输入显示名称 ${input.name}`" /><input v-model="input.name" :aria-label="`输入 API 名称 ${input.name}`" class="builder-api-input" pattern="[a-z][a-z0-9_]*" /></div>
              <select v-model="input.type" :aria-label="`输入类型 ${input.name}`"><option value="string">文本</option><option value="number">数字</option><option value="integer">整数</option><option value="boolean">布尔值</option></select>
              <div class="builder-check-stack"><label><input v-model="input.required" type="checkbox" />必填</label><label><input v-model="input.sensitive" type="checkbox" />敏感值</label></div>
              <button class="text-button danger-text" :aria-label="`删除输入 ${input.name}`" @click="removeInput(input.name)">删除</button>
            </div>
          </div>
          <p v-else class="builder-empty-note">尚未声明会话输入。Agent Manager 会按这里的定义收集启动参数。</p>
          <div class="builder-subheading builder-variable-heading"><strong>预计算变量</strong><span>{{ config.precomputed_variables.length }} 个步骤</span></div>
          <div v-if="config.precomputed_variables.length" class="builder-definition-table builder-variable-table">
            <div class="builder-definition-head"><span>变量名称</span><span>本地可验证的表达式</span><span>状态</span><span /></div>
            <div v-for="(variable, index) in config.precomputed_variables" :key="`${index}-${variable.name}`" class="builder-input-row">
              <input v-model="variable.name" :aria-label="`变量名称 ${index + 1}`" />
              <input v-model="variable.expression" :aria-label="`变量表达式 ${index + 1}`" placeholder="input.customer_id / variable.previous / literal:text" />
              <span class="builder-variable-state">顺序解析</span>
              <button class="text-button danger-text" @click="config.precomputed_variables.splice(index, 1)">删除</button>
            </div>
          </div>
          <p class="builder-help">本地预览支持引用输入、前序变量和 literal: 常量；连接 Foundry Functions、对象集和其他专有变量运行时仍需对应连接器。</p>
        </template>

        <template v-else-if="activePanel === 'tools'">
          <div class="builder-section-heading"><div><h2>工具与权限</h2><p>选择 Agent 可请求的工具。执行时仍会由服务端检查当前用户权限。</p></div></div>
          <div class="builder-tool-table">
            <div class="builder-definition-head"><span>工具</span><span>能力范围</span><span>允许调用</span></div>
            <label v-for="tool in toolOptions" :key="tool.id" class="builder-tool-row">
              <span><strong>{{ tool.name }}</strong><code>{{ tool.id }}</code></span><span>{{ tool.description }}</span><input type="checkbox" :checked="config.allowed_tools.includes(tool.id)" :aria-label="`允许工具 ${tool.id}`" @change="toggleTool(tool.id)" />
            </label>
          </div>
          <label class="builder-wide-field builder-action-scope">Action API 白名单<input :value="config.allowed_actions.join(', ')" aria-label="Action API 白名单" placeholder="set_customer_tier, mark_order_review" @input="setActionScopeFromEvent" /><small>工具配置与用户的本体 Action 权限共同生效；变更后先预览，再由运行者确认写入。</small></label>
          <div class="builder-note warning"><strong>写入控制</strong><span>只有已发布版本可以创建会话。Preview 不调用工具或应用本体变更。</span></div>
        </template>

        <template v-else-if="activePanel === 'completion'">
          <div class="builder-section-heading"><div><h2>完成与输出</h2><p>选择会话保持开放，或在首个有效结构化输出后结束。</p></div></div>
          <label class="builder-wide-field">会话完成方式<select v-model="config.session_completion.mode" aria-label="会话完成方式"><option value="stays_open">保持开放，可继续交互</option><option value="ends_after_first_valid_output">首个有效结构化结果后结束</option></select></label>
          <label class="builder-wide-field">结构化输出 Schema<textarea v-model="outputSchemaText" aria-label="结构化输出 Schema" rows="12" spellcheck="false" /></label>
          <div class="builder-note"><strong>结构校验</strong><span>结束模式要求填写初始用户消息和非空输出结构。Schema 在发布时由服务端再次校验。</span></div>
        </template>
      </section>

      <aside class="builder-preview">
        <header class="builder-preview-heading"><div><span>预览</span><h2>调试当前草稿</h2></div><span class="preview-mode">本地 dry-run</span></header>
        <p class="builder-preview-copy">输入样例值后检查模板、变量顺序和工具范围。此面板不会调用模型或修改本体。</p>
        <div v-if="config.inputs.length" class="preview-input-list">
          <label v-for="input in config.inputs" :key="input.name">{{ input.display_name }}<input v-if="input.type !== 'boolean'" v-model="previewValues[input.name]" :type="input.sensitive ? 'password' : input.type === 'string' ? 'text' : 'number'" :aria-label="`预览输入：${input.display_name}`" :placeholder="input.required ? '必填' : '可选'" /><input v-else v-model="previewValues[input.name]" type="checkbox" :aria-label="`预览输入：${input.display_name}`" /></label>
        </div>
        <p v-else class="builder-empty-note preview-empty">没有输入项。添加输入后可在这里传入样例值。</p>
        <button class="button button-primary preview-run-button" data-action="run-preview" :disabled="busy || isNew" @click="runPreview">{{ busy ? "处理中…" : "运行本地预览" }}</button>
        <section v-if="previewResult" class="preview-debug-output" aria-label="Preview Debug 结果">
          <div class="preview-run-meta"><span>确定性本地运行</span><span>{{ previewResult.model_provider }} / {{ previewResult.model_name }}</span></div>
          <div v-if="previewResult.variables.length" class="preview-variable-list"><strong>预计算步骤</strong><div v-for="variable in previewResult.variables" :key="variable.name"><span>{{ variable.name }}</span><code>{{ variable.value }}</code><small>{{ variable.status }}</small></div></div>
          <strong>展开后的提示词</strong><pre>{{ previewResult.rendered_prompt }}</pre>
          <div class="preview-scope"><strong>允许工具</strong><code v-for="tool in previewResult.allowed_tools" :key="tool">{{ tool }}</code><span v-if="!previewResult.allowed_tools.length">未开放工具</span></div>
          <p v-for="message in previewResult.notices" :key="message" class="preview-boundary-note">{{ message }}</p>
        </section>
        <section v-else class="preview-placeholder"><span class="preview-terminal-mark">›_</span><p>预览结果与调试上下文会显示在这里。</p></section>
      </aside>
    </div>
  </main>
</template>

<style scoped>
.agent-builder { gap: 15px; color: #25312f; }
.builder-header { display: flex; justify-content: space-between; align-items: flex-end; gap: 20px; padding-bottom: 13px; border-bottom: 1px solid #d7dfdb; }
.builder-title-group { min-width: 0; }
.builder-back-link { display: inline-block; margin-bottom: 8px; color: #66746f; font-size: 11px; }
.builder-title-line { display: flex; align-items: center; gap: 16px; }
.builder-title-line p { margin: 0; color: #66746f; font-size: 12px; }
.builder-api-name { display: inline-block; margin-top: 5px; color: #87948d; font-size: 9px; }
.builder-title-line h1 { margin-bottom: 5px; }
.builder-version-badge, .builder-draft-state { padding: 6px 9px; color: #506c61; background: #e5eee9; border: 1px solid #d1dfd7; border-radius: 4px; font-size: 10px; white-space: nowrap; }
.builder-draft-state { color: #916432; background: #f8f0df; border-color: #ecdfbe; }
.builder-header-actions { display: flex; align-items: center; gap: 8px; flex: 0 0 auto; }
.builder-layout { display: grid; grid-template-columns: 205px minmax(370px, 1fr) minmax(290px, 350px); align-items: start; gap: 12px; }
.builder-outline, .builder-editor, .builder-preview { min-width: 0; background: #fff; border: 1px solid #d7dfdb; border-radius: 5px; }
.builder-outline { position: sticky; top: 12px; padding: 13px 0 0; }
.builder-outline-heading { display: flex; justify-content: space-between; align-items: center; padding: 0 12px 9px; color: #35453f; font-size: 11px; }
.builder-outline-heading span { color: #84918c; font-size: 9px; }
.builder-outline nav { display: flex; flex-direction: column; padding: 0 7px 11px; border-bottom: 1px solid #e4e9e6; }
.builder-outline nav button { display: flex; align-items: center; gap: 10px; min-height: 33px; padding: 0 7px; color: #52615b; background: transparent; border: 0; border-radius: 3px; text-align: left; font-size: 10px; cursor: pointer; }
.builder-outline nav button:hover { background: #f1f5f2; }
.builder-outline nav button.active { color: #245a4b; background: #e6f0eb; box-shadow: inset 2px 0 #2e6658; }
.builder-outline nav button span { color: #83908a; font-family: "Cascadia Code", Consolas, monospace; font-size: 9px; }
.builder-version-list { padding: 12px 0; }
.builder-version-row { display: grid; grid-template-columns: auto 1fr; gap: 5px 8px; padding: 8px 12px; border-top: 1px solid #eef1ef; }
.builder-version-row strong { color: #34463e; font-size: 10px; }
.builder-version-row time { color: #82908a; text-align: right; font-size: 9px; }
.builder-version-row small { grid-column: 1 / -1; color: #7a8982; font-size: 9px; }
.builder-editor { padding: 17px 18px 20px; }
.builder-section-heading { display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; margin-bottom: 15px; padding-bottom: 12px; border-bottom: 1px solid #e5eae7; }
.builder-section-heading h2 { margin: 0 0 4px; font-size: 15px; }
.builder-section-heading p { margin: 0; color: #728079; font-size: 10px; line-height: 1.5; }
.builder-config-count { padding: 4px 7px; color: #587367; background: #edf3ef; font-size: 9px; }
.builder-form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 13px; }
.builder-wide-field { margin-bottom: 13px; }
.builder-editor label { gap: 5px; color: #53615b; font-size: 10px; }
.builder-editor input, .builder-editor textarea, .builder-editor select, .builder-preview input { width: 100%; min-width: 0; min-height: 34px; padding: 7px 9px; color: #2b3833; background: #fcfdfc; border: 1px solid #d4ddd8; border-radius: 3px; font-size: 10px; }
.builder-editor textarea { line-height: 1.6; resize: vertical; }
.builder-editor input:focus, .builder-editor textarea:focus, .builder-editor select:focus, .builder-preview input:focus { outline: 2px solid rgba(46, 102, 88, .2); border-color: #7ca697; }
.builder-note { display: flex; gap: 11px; padding: 10px 11px; color: #5e7068; background: #f0f5f2; border-left: 2px solid #7da792; font-size: 9px; line-height: 1.55; }
.builder-note strong { flex: 0 0 auto; color: #385a4d; }
.builder-note.warning { color: #7d6744; background: #faf5ea; border-color: #c49651; }
.builder-note.warning strong { color: #805c2e; }
.builder-runtime-capabilities { display: grid; gap: 5px; margin: -2px 0 12px; }
.builder-runtime-capabilities > div { display: grid; grid-template-columns: minmax(140px, 1fr) auto minmax(180px, 1.2fr); align-items: center; gap: 8px; padding: 7px 9px; background: #f6f9f7; border: 1px solid #e3eae5; border-radius: 3px; }
.builder-runtime-capabilities strong { color: #4c6054; font-size: 9px; font-weight: 550; }
.builder-runtime-capabilities span { font-size: 8px; }
.builder-runtime-capabilities .runtime-available { color: #4b805c; }
.builder-runtime-capabilities .runtime-unavailable { color: #a06e45; }
.builder-runtime-capabilities small { color: #89948d; font-size: 8px; text-align: right; }
.builder-subheading { display: flex; justify-content: space-between; align-items: center; margin: 16px 0 7px; color: #46554e; font-size: 10px; }
.builder-subheading span { color: #87938d; font-size: 9px; }
.builder-variable-heading { margin-top: 23px; }
.builder-inline-actions { display: flex; gap: 7px; flex-wrap: wrap; }
.builder-definition-table, .builder-tool-table { border: 1px solid #e0e6e2; border-radius: 3px; overflow: hidden; }
.builder-definition-head { display: grid; grid-template-columns: minmax(140px, 1.3fr) minmax(90px, .8fr) minmax(100px, 1fr) 44px; gap: 8px; padding: 8px 9px; color: #77847e; background: #f4f7f5; border-bottom: 1px solid #e0e6e2; font-size: 9px; }
.builder-input-row { display: grid; grid-template-columns: minmax(140px, 1.3fr) minmax(90px, .8fr) minmax(100px, 1fr) 44px; align-items: center; gap: 8px; padding: 8px 9px; border-bottom: 1px solid #edf0ee; }
.builder-input-row:last-child { border-bottom: 0; }
.builder-input-identity { display: grid; gap: 5px; }
.builder-editor .builder-input-row input, .builder-editor .builder-input-row select { min-height: 29px; padding: 5px 7px; font-size: 9px; }
.builder-editor .builder-input-row .builder-api-input { color: #72817a; font-family: "Cascadia Code", Consolas, monospace; }
.builder-check-stack { display: flex; gap: 9px; }
.builder-check-stack label { display: flex; align-items: center; gap: 4px; white-space: nowrap; }
.builder-check-stack input, .builder-tool-row input { width: 13px; min-height: 13px; margin: 0; accent-color: #2e6658; }
.text-button { padding: 3px 4px; color: #456c5a; background: transparent; border: 0; font-size: 9px; cursor: pointer; }
.danger-text { color: #9a5746; }
.builder-variable-table .builder-definition-head, .builder-variable-table .builder-input-row { grid-template-columns: minmax(100px, .8fr) minmax(160px, 1.5fr) minmax(80px, .7fr) 44px; }
.builder-variable-state { color: #70837a; font-size: 9px; }
.builder-help, .builder-empty-note { margin: 8px 0 0; color: #819089; font-size: 9px; line-height: 1.55; }
.builder-empty-note { padding: 15px 10px; background: #f7f9f7; border: 1px dashed #d8e0db; text-align: center; }
.builder-tool-table .builder-definition-head { grid-template-columns: minmax(120px, .8fr) minmax(160px, 1.4fr) 64px; }
.builder-tool-row { display: grid; grid-template-columns: minmax(120px, .8fr) minmax(160px, 1.4fr) 64px; align-items: center; gap: 8px; padding: 10px 9px; border-bottom: 1px solid #edf0ee; }
.builder-tool-row:last-child { border-bottom: 0; }
.builder-tool-row > span:first-child strong, .builder-tool-row code { display: block; }
.builder-tool-row strong { color: #405149; font-size: 10px; }
.builder-tool-row code { margin-top: 3px; color: #809088; font-size: 8px; }
.builder-tool-row > span:nth-child(2) { color: #76837d; font-size: 9px; line-height: 1.45; }
.builder-tool-row > input { justify-self: center; }
.builder-action-scope { margin-top: 16px; }
.builder-action-scope small { color: #839089; font-size: 9px; }
.builder-preview { position: sticky; top: 12px; padding: 14px 14px 16px; background: #f9fbfa; }
.builder-preview-heading { display: flex; justify-content: space-between; align-items: center; gap: 8px; padding-bottom: 10px; border-bottom: 1px solid #dfe6e2; }
.builder-preview-heading > div > span { color: #60756b; font-size: 9px; }
.builder-preview-heading h2 { margin: 4px 0 0; font-size: 14px; }
.preview-mode { padding: 4px 6px; color: #536f61; background: #e6efe9; border-radius: 3px; font-size: 8px; white-space: nowrap; }
.builder-preview-copy { margin: 10px 0 12px; color: #788680; font-size: 9px; line-height: 1.55; }
.preview-input-list { display: grid; gap: 8px; }
.builder-preview label { color: #53615b; font-size: 9px; }
.builder-preview input[type="checkbox"] { width: 14px; min-height: 14px; }
.preview-run-button { width: 100%; margin-top: 10px; }
.preview-placeholder { min-height: 190px; display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 9px; color: #8b9791; border-top: 1px solid #e3e9e5; margin-top: 13px; text-align: center; }
.preview-placeholder p { max-width: 180px; margin: 0; font-size: 9px; line-height: 1.6; }
.preview-terminal-mark { display: grid; place-items: center; width: 37px; height: 31px; color: #4e7460; background: #e7f0ea; border: 1px solid #d5e3da; border-radius: 3px; font-family: "Cascadia Code", Consolas, monospace; font-size: 12px; }
.preview-debug-output { display: grid; gap: 8px; margin-top: 13px; padding-top: 11px; border-top: 1px solid #e1e7e3; }
.preview-run-meta { display: flex; justify-content: space-between; gap: 8px; color: #64796e; font-size: 8px; }
.preview-debug-output > strong, .preview-variable-list > strong { color: #52645a; font-size: 9px; }
.preview-debug-output pre { max-height: 200px; margin: 0; padding: 9px; overflow: auto; color: #d8e5dd; background: #273732; border-radius: 3px; font-size: 9px; line-height: 1.55; white-space: pre-wrap; overflow-wrap: anywhere; }
.preview-variable-list { display: grid; gap: 5px; }
.preview-variable-list > div { display: grid; grid-template-columns: 1fr auto; gap: 3px 7px; padding: 6px 7px; background: #edf3ef; }
.preview-variable-list span { color: #465b50; font-size: 9px; }
.preview-variable-list code { color: #62756a; font-size: 8px; }
.preview-variable-list small { grid-column: 1 / -1; color: #829087; font-size: 8px; }
.preview-scope { display: flex; align-items: center; flex-wrap: wrap; gap: 5px; color: #718078; font-size: 8px; }
.preview-scope strong { margin-right: 3px; }
.preview-scope code { padding: 3px 5px; color: #4a6a58; background: #e9f0eb; border-radius: 2px; }
.preview-scope span { color: #89958f; }
.preview-boundary-note { margin: 0; color: #897044; font-size: 8px; line-height: 1.45; }
@media (max-width: 1120px) { .builder-layout { grid-template-columns: 175px minmax(0, 1fr); }.builder-preview { position: static; grid-column: 2; }.builder-outline { grid-row: span 2; } }
@media (max-width: 720px) { .builder-header { align-items: stretch; flex-direction: column; }.builder-header-actions { justify-content: flex-end; flex-wrap: wrap; }.builder-layout { grid-template-columns: 1fr; }.builder-outline, .builder-preview { position: static; grid-column: auto; grid-row: auto; }.builder-outline nav { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); }.builder-editor { padding: 14px 12px; }.builder-form-grid { grid-template-columns: 1fr; }.builder-definition-head { display: none; }.builder-input-row { grid-template-columns: minmax(0, 1fr) 90px; }.builder-check-stack { grid-column: 1; }.builder-variable-table .builder-input-row { grid-template-columns: 1fr; }.builder-tool-table .builder-definition-head { display: none; }.builder-tool-row { grid-template-columns: minmax(0, 1fr) auto; }.builder-tool-row > span:nth-child(2) { grid-column: 1; grid-row: 2; }.builder-tool-row > input { grid-column: 2; grid-row: 1 / span 2; }.builder-title-line { align-items: flex-start; flex-direction: column; gap: 8px; } }
@media (prefers-reduced-motion: reduce) { .agent-builder *, .agent-builder *::before, .agent-builder *::after { scroll-behavior: auto !important; transition-duration: .01ms !important; animation-duration: .01ms !important; } }
</style>
