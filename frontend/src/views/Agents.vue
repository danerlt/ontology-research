<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { api, readableError } from "../api/client";
import AgentTools from "../components/AgentTools.vue";
import { useAuthStore } from "../stores/auth";
import type { AgentDefinition } from "../types";

interface AgentSession {
  id: string;
  agent_id: string;
  status: string;
  created_at: string;
}
interface AgentEvent {
  id: string;
  sequence: number;
  event_type: string;
  tool_name?: string;
  status: string;
  details: Record<string, unknown>;
  created_at: string;
}

const auth = useAuthStore();
const agents = ref<AgentDefinition[]>([]);
const selectedAgentId = ref("");
const currentSession = ref<AgentSession | null>(null);
const events = ref<AgentEvent[]>([]);
const resultText = ref("");
const error = ref("");
const notice = ref("");
const loading = ref(false);
const showCreate = ref(false);
const createForm = ref({ display_name: "", api_name: "", description: "", tools: ["search_objects"], actions: "" });

const selectedAgent = computed(() => agents.value.find((item) => item.id === selectedAgentId.value) ?? null);
const tools = [
  { id: "search_objects", label: "查找对象" },
  { id: "get_object", label: "读取对象" },
  { id: "execute_action", label: "执行 Action" },
];

async function loadAgents() {
  loading.value = true;
  error.value = "";
  try {
    agents.value = await api.get<AgentDefinition[]>("/api/agents", undefined, "/agent-api");
    if (!selectedAgentId.value || !agents.value.some((item) => item.id === selectedAgentId.value)) {
      selectedAgentId.value = agents.value[0]?.id ?? "";
    }
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function createAgent() {
  error.value = "";
  try {
    const agent = await api.post<AgentDefinition>("/api/agents", {
      display_name: createForm.value.display_name,
      api_name: createForm.value.api_name,
      description: createForm.value.description,
      allowed_tools: createForm.value.tools,
      allowed_actions: createForm.value.actions.split(",").map((item) => item.trim()).filter(Boolean),
    }, "/agent-api");
    notice.value = "Agent 已创建，工具权限已保存。";
    showCreate.value = false;
    selectedAgentId.value = agent.id;
    createForm.value = { display_name: "", api_name: "", description: "", tools: ["search_objects"], actions: "" };
    await loadAgents();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function startSession() {
  if (!selectedAgent.value) return;
  error.value = "";
  notice.value = "";
  try {
    currentSession.value = await api.post<AgentSession>(`/api/agents/${selectedAgent.value.id}/sessions`, undefined, "/agent-api");
    resultText.value = "会话已启动。你可以按 Agent 授权范围手动触发工具。";
    await loadEvents();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function callTool(toolName: string, arguments_: Record<string, unknown>) {
  if (!currentSession.value) return;
  error.value = "";
  notice.value = "";
  try {
    const result = await api.post<{ result: unknown }>(`/api/sessions/${currentSession.value.id}/tools/${toolName}`, { arguments: arguments_ }, "/agent-api");
    resultText.value = JSON.stringify(result.result, null, 2);
    notice.value = `工具“${toolName}”已完成。`;
    await loadEvents();
  } catch (cause) {
    error.value = readableError(cause);
    await loadEvents();
  }
}

async function loadEvents() {
  if (!currentSession.value) return;
  try {
    const result = await api.get<{ items: AgentEvent[] }>(`/api/sessions/${currentSession.value.id}/events`, undefined, "/agent-api");
    events.value = result.items;
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function closeSession() {
  if (!currentSession.value) return;
  try {
    await api.post(`/api/sessions/${currentSession.value.id}/close`, {}, "/agent-api");
    currentSession.value = { ...currentSession.value, status: "closed" };
    notice.value = "会话已结束，事件记录已保留。";
    await loadEvents();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

function formatEvent(event: AgentEvent): string {
  if (event.event_type === "session.created") return "会话已创建";
  if (event.event_type === "session.closed") return "会话已结束";
  if (event.status === "denied") return String(event.details.reason || "调用被拒绝");
  if (event.status === "failed") return String(event.details.error || "调用失败");
  return `已运行 ${event.tool_name}`;
}

onMounted(loadAgents);
</script>

<template>
  <div class="page-content">
    <div class="page-heading"><div><span class="eyebrow">授权工具运行时</span><h1>Agent 工作台</h1><p>选择一个 Agent 创建会话，再手动调用已授权的本体工具。</p></div><button v-if="auth.role === 'admin'" class="button button-primary" @click="showCreate = !showCreate">{{ showCreate ? "关闭表单" : "新建 Agent" }}</button></div>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div><div v-if="notice" class="notice notice-success">{{ notice }}</div>
    <section v-if="showCreate && auth.role === 'admin'" class="agent-create-panel"><div class="section-heading"><div><h2>注册 Agent</h2><p>工具权限会在每次调用时由服务端重新检查。</p></div></div><form class="agent-form" @submit.prevent="createAgent"><div class="form-grid"><label>显示名称<input v-model="createForm.display_name" required placeholder="运营助理" /></label><label>API 名称<input v-model="createForm.api_name" required pattern="[a-z][a-z0-9_]*" placeholder="operations_assistant" /></label></div><label>说明<input v-model="createForm.description" placeholder="协助查询客户和订单" /></label><fieldset><legend>工具授权</legend><label v-for="tool in tools" :key="tool.id" class="check-option"><input v-model="createForm.tools" type="checkbox" :value="tool.id" />{{ tool.label }}</label></fieldset><label>可执行 Action（逗号分隔）<input v-model="createForm.actions" placeholder="set_customer_tier" /></label><button class="button button-primary" :disabled="!createForm.display_name || !createForm.api_name || !createForm.tools.length">保存 Agent</button></form></section>
    <div class="agent-layout"><aside class="agent-list-panel"><div class="panel-heading"><div><h2>已注册 Agent</h2><p>工具和 Action 授权</p></div><button class="icon-button" aria-label="重新加载" @click="loadAgents">↻</button></div><div v-if="loading" class="empty-state compact">正在读取…</div><button v-for="agent in agents" :key="agent.id" class="agent-list-item" :class="{ selected: selectedAgentId === agent.id }" @click="selectedAgentId = agent.id; currentSession = null; events = []"><span class="agent-avatar">◉</span><span><strong>{{ agent.display_name }}</strong><code>{{ agent.api_name }}</code><small>{{ agent.allowed_tools.length }} 项工具授权</small></span><i :class="agent.enabled ? 'enabled-dot' : 'disabled-dot'" /></button><div v-if="!loading && !agents.length" class="empty-state compact"><strong>暂无 Agent</strong><span>管理员可以先注册一个 Agent。</span></div></aside>
      <section class="agent-session-panel"><template v-if="selectedAgent"><div class="agent-session-header"><div><span class="eyebrow">运行环境</span><h2>{{ selectedAgent.display_name }}</h2><p>{{ selectedAgent.description || "未填写说明" }}</p></div><button v-if="!currentSession" class="button button-primary" @click="startSession">开始会话</button><div v-else class="session-controls"><span class="session-state" :class="{ closed: currentSession.status !== 'active' }"><i />{{ currentSession.status === "active" ? "会话进行中" : "已结束" }}</span><button v-if="currentSession.status === 'active'" class="button button-quiet" @click="closeSession">结束会话</button></div></div><div class="permission-strip"><span>工具权限</span><code v-for="tool in selectedAgent.allowed_tools" :key="tool">{{ tool }}</code><span v-if="!selectedAgent.allowed_tools.length" class="muted">未授权工具</span><span v-if="selectedAgent.allowed_actions.length" class="action-permission">Action：{{ selectedAgent.allowed_actions.join("、") }}</span></div><div v-if="currentSession" class="agent-session-body"><AgentTools :allowed-tools="selectedAgent.allowed_tools" :session-active="currentSession.status === 'active'" @call-tool="callTool" @invalid-input="(message) => error = message" /><section class="tool-result"><div class="section-heading"><div><h3>最近一次结果</h3><p>工具调用结果会留在会话事件中。</p></div></div><pre v-if="resultText">{{ resultText }}</pre><p v-else class="quiet-empty">运行一个已授权工具后，结果会显示在这里。</p></section><section class="event-panel"><div class="section-heading"><div><h3>会话事件</h3><p>按发生顺序记录授权、调用和结果。</p></div><button class="button button-quiet" @click="loadEvents">刷新</button></div><div v-if="events.length" class="event-list"><div v-for="event in events" :key="event.id" class="event-row"><span class="event-sequence">{{ String(event.sequence).padStart(2, "0") }}</span><span class="event-status" :class="`event-${event.status}`" /><div><strong>{{ formatEvent(event) }}</strong><small>{{ new Date(event.created_at).toLocaleString("zh-CN") }}</small></div></div></div><p v-else class="quiet-empty">本会话暂无事件。</p></section></div><div v-else class="empty-detail"><span class="empty-orbit">◉</span><h2>为 {{ selectedAgent.display_name }} 开始会话</h2><p>当前用户的身份令牌将随每次工具请求传递给本体 API。</p></div></template><div v-else class="empty-detail"><span class="empty-orbit">◇</span><h2>选择一个 Agent</h2><p>查看授权范围，或新建一个 Agent 开始体验。</p></div></section></div>
  </div>
</template>
