<script setup lang="ts">
import { computed, onMounted, reactive, ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { api, readableError } from "../api/client";
import type { AgentDefinition, AgentSession, AgentVersion } from "../types";

const route = useRoute();
const router = useRouter();
const agents = ref<AgentDefinition[]>([]);
const sessions = ref<AgentSession[]>([]);
const versions = ref<AgentVersion[]>([]);
const selectedAgentId = ref("");
const selectedVersionNumber = ref<number | null>(null);
const activeTab = ref(route.path === "/sessions" ? "sessions" : "agents");
const sessionStatus = ref("active");
const sessionOrigin = ref("");
const sessionSearch = ref("");
const startOpen = ref(false);
const sessionInputs = reactive<Record<string, unknown>>({});
const loading = ref(false);
const error = ref("");
const notice = ref("");
const busy = ref(false);

const selectedAgent = computed(() => agents.value.find((agent) => agent.id === selectedAgentId.value) ?? null);
const selectedVersion = computed(() => versions.value.find((version) => version.version_number === selectedVersionNumber.value) ?? null);

const toolNames: Record<string, string> = {
  search_objects: "查询对象",
  get_object: "读取对象",
  execute_action: "执行 Action",
};

async function loadAgents() {
  loading.value = true;
  error.value = "";
  try {
    agents.value = await api.get<AgentDefinition[]>("/api/agents", undefined, "/agent-api");
    if (!agents.value.some((agent) => agent.id === selectedAgentId.value)) {
      selectedAgentId.value = agents.value[0]?.id ?? "";
    }
    if (selectedAgentId.value) await loadVersions(selectedAgentId.value);
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function loadVersions(agentId: string) {
  try {
    versions.value = await api.get<AgentVersion[]>(`/api/agents/${agentId}/versions`, undefined, "/agent-api");
    const latest = versions.value[0]?.version_number ?? selectedAgent.value?.latest_version_number ?? null;
    selectedVersionNumber.value = versions.value.some((version) => version.version_number === selectedVersionNumber.value)
      ? selectedVersionNumber.value
      : latest;
    resetSessionInputs();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function selectAgent(agentId: string) {
  selectedAgentId.value = agentId;
  startOpen.value = false;
  await loadVersions(agentId);
}

function resetSessionInputs() {
  for (const key of Object.keys(sessionInputs)) delete sessionInputs[key];
  for (const input of selectedVersion.value?.config.inputs ?? selectedAgent.value?.draft_config.inputs ?? []) {
    sessionInputs[input.name] = input.type === "boolean" ? false : "";
  }
}

function openSessionForm() {
  resetSessionInputs();
  startOpen.value = true;
}

async function startSession() {
  if (!selectedAgent.value) return;
  const inputDefinitions = selectedVersion.value?.config.inputs ?? [];
  const values: Record<string, unknown> = {};
  for (const input of inputDefinitions) {
    const value = sessionInputs[input.name];
    if (input.type === "boolean") values[input.name] = Boolean(value);
    else if (value !== "" && value !== undefined) values[input.name] = input.type === "number" || input.type === "integer" ? Number(value) : value;
  }
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const created = await api.post<AgentSession>(`/api/agents/${selectedAgent.value.id}/sessions`, {
      inputs: values,
      version_number: selectedVersionNumber.value,
      origin_resource: "本体工作台",
    }, "/agent-api");
    notice.value = `会话已固定到版本 ${created.version_number}。`;
    startOpen.value = false;
    await router.push(`/sessions/${created.id}`);
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

async function loadSessions() {
  loading.value = true;
  error.value = "";
  const params = new URLSearchParams({ page: "1", page_size: "50", status: sessionStatus.value });
  if (sessionOrigin.value.trim()) params.set("origin_resource", sessionOrigin.value.trim());
  if (sessionSearch.value.trim()) params.set("query", sessionSearch.value.trim());
  try {
    const response = await api.get<{ items: AgentSession[]; total: number }>(`/api/sessions?${params.toString()}`, undefined, "/agent-api");
    sessions.value = response.items;
    sessionTotal.value = response.total;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

const sessionTotal = ref(0);

async function changeTab(tab: "agents" | "sessions") {
  activeTab.value = tab;
  if (tab === "sessions") {
    await router.push("/sessions");
    await loadSessions();
  } else {
    await router.push("/agents");
    await loadAgents();
  }
}

function openSession(session: AgentSession) {
  router.push(`/sessions/${session.id}`);
}

function formatDate(value: string): string {
  return new Date(value).toLocaleString("zh-CN", { hour12: false });
}

watch(() => route.path, (path) => {
  activeTab.value = path === "/sessions" ? "sessions" : "agents";
  if (activeTab.value === "sessions") loadSessions();
});

onMounted(() => {
  loadAgents();
  if (activeTab.value === "sessions") loadSessions();
});
</script>

<template>
  <main class="agent-manager page-content">
    <header class="manager-header">
      <div><h1>{{ activeTab === "sessions" ? "运行会话" : "智能体管理" }}</h1><p>{{ activeTab === "sessions" ? "跨智能体筛选会话，查看来源、版本与执行状态。" : "管理已发布智能体、权限范围和可启动版本。" }}</p></div>
      <RouterLink data-action="create-agent" class="button button-primary" to="/agent-builder/new">新建智能体</RouterLink>
    </header>
    <nav class="manager-tabs" aria-label="智能体管理页面">
      <button :class="{ active: activeTab === 'agents' }" @click="changeTab('agents')">已发布智能体 <span>{{ agents.length }}</span></button>
      <button :class="{ active: activeTab === 'sessions' }" @click="changeTab('sessions')">运行会话 <span>{{ sessionTotal }}</span></button>
    </nav>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div><div v-if="notice" class="notice notice-success" role="status">{{ notice }}</div>

    <template v-if="activeTab === 'agents'">
      <div class="agent-manager-layout">
        <section class="manager-agent-index">
          <header class="manager-panel-header"><div><h2>可访问的智能体</h2><p>{{ agents.length }} 个已注册资源</p></div><button class="text-button" @click="loadAgents">刷新</button></header>
          <div v-if="loading" class="manager-empty">正在读取智能体目录…</div>
          <button v-for="agent in agents" :key="agent.id" class="manager-agent-row" :class="{ selected: selectedAgentId === agent.id }" @click="selectAgent(agent.id)">
            <span class="manager-agent-mark">◉</span><span class="manager-agent-name"><strong>{{ agent.display_name }}</strong><code>{{ agent.api_name }}</code></span><span class="manager-agent-version">{{ agent.latest_version_number ? `v${agent.latest_version_number}` : "草稿" }}</span>
          </button>
          <div v-if="!loading && !agents.length" class="manager-empty"><strong>还没有智能体</strong><span>新建配置、预览并发布第一个版本。</span><RouterLink to="/agent-builder/new">创建智能体</RouterLink></div>
        </section>

        <section v-if="selectedAgent" class="manager-agent-detail">
          <header class="manager-detail-header"><div><span class="manager-resource-kind">已发布资源</span><h2>{{ selectedAgent.display_name }}</h2><p>{{ selectedAgent.description || "未填写说明" }}</p><code>{{ selectedAgent.api_name }}</code></div><div class="manager-detail-actions"><RouterLink class="button button-quiet" :to="`/agent-builder/${selectedAgent.id}`">编辑草稿</RouterLink><button class="button button-primary" data-action="start-session" :disabled="!selectedVersion" @click="openSessionForm">开始会话</button></div></header>
          <div class="manager-scope-row"><strong>工具范围</strong><span v-for="tool in selectedAgent.allowed_tools" :key="tool">{{ toolNames[tool] || tool }}</span><em v-if="selectedAgent.allowed_actions.length">Action：{{ selectedAgent.allowed_actions.join("、") }}</em></div>
          <div class="manager-version-section"><header class="manager-panel-header"><div><h3>发布版本</h3><p>新会话将固定到所选版本，已有会话不随草稿变化。</p></div><label>启动版本<select v-model.number="selectedVersionNumber" aria-label="启动版本"><option v-for="version in versions" :key="version.id" :value="version.version_number">版本 {{ version.version_number }}</option></select></label></header>
            <div v-if="versions.length" class="manager-version-list"><article v-for="version in versions" :key="version.id" :class="{ chosen: version.version_number === selectedVersionNumber }"><span class="version-marker" /><div><strong>版本 {{ version.version_number }}</strong><small>{{ version.config.model_provider }} / {{ version.config.model_name }}</small></div><time>{{ formatDate(version.published_at) }}</time><button class="text-button" @click="selectedVersionNumber = version.version_number">使用此版本</button></article></div>
            <p v-else class="manager-empty">尚无发布版本。先在构建器保存草稿并发布。</p>
          </div>
          <div v-if="startOpen && selectedVersion" class="manager-session-form"><header class="manager-panel-header"><div><h3>启动新会话</h3><p>将使用版本 {{ selectedVersion.version_number }}，会话事件会记录来源与配置快照。</p></div><button class="text-button" @click="startOpen = false">关闭</button></header>
            <div v-if="selectedVersion.config.inputs.length" class="manager-input-grid"><label v-for="input in selectedVersion.config.inputs" :key="input.name">{{ input.display_name }}<input v-if="input.type !== 'boolean'" v-model="sessionInputs[input.name]" :type="input.sensitive ? 'password' : input.type === 'string' ? 'text' : 'number'" :aria-label="`会话输入：${input.display_name}`" :required="input.required" /><input v-else v-model="sessionInputs[input.name]" type="checkbox" :aria-label="`会话输入：${input.display_name}`" /><small>{{ input.required ? "必填" : "可选" }}{{ input.sensitive ? " · 敏感值将遮蔽" : "" }}</small></label></div>
            <p v-else class="manager-empty">此版本无需启动输入。</p>
            <footer><span>来源应用：本体工作台</span><button class="button button-primary" data-action="confirm-start-session" :disabled="busy" @click="startSession">{{ busy ? "启动中…" : "创建会话" }}</button></footer>
          </div>
        </section>
        <section v-else class="manager-agent-detail manager-empty-detail"><span>◉</span><h2>选择一个智能体</h2><p>检查发布版本和工具授权，再启动固定版本的会话。</p></section>
      </div>
    </template>

    <template v-else>
      <section class="manager-sessions-panel">
        <form class="session-filter-bar" @submit.prevent="loadSessions"><label>状态<select v-model="sessionStatus" aria-label="会话状态筛选" @change="loadSessions"><option value="active">运行中</option><option value="closed">已结束</option><option value="cancelled">已取消</option><option value="">全部状态</option></select></label><label>来源应用<input v-model="sessionOrigin" aria-label="来源应用筛选" placeholder="Workshop、Automate 或工作台" /></label><label>智能体或应用<input v-model="sessionSearch" aria-label="会话搜索" placeholder="名称、API 名或来源" /></label><button type="button" class="button button-quiet" data-action="apply-session-filters" @click="loadSessions">应用筛选</button><span class="filter-result-count">{{ sessionTotal }} 条记录</span></form>
        <div class="manager-table-wrap"><table class="manager-session-table"><thead><tr><th>智能体</th><th>发布版本</th><th>来源</th><th>发起人输入</th><th>状态</th><th>开始时间</th><th /></tr></thead><tbody><tr v-for="session in sessions" :key="session.id" @click="openSession(session)"><td><strong>{{ agents.find((agent) => agent.id === session.agent_id)?.display_name || "智能体" }}</strong><code>{{ session.agent_id.slice(0, 8) }}</code></td><td><span class="manager-table-version">版本 {{ session.version_number }}</span></td><td>{{ session.origin_resource }}</td><td>{{ Object.keys(session.inputs).length }} 项</td><td><span class="manager-table-status" :class="`status-${session.status}`">{{ session.status === "active" ? "运行中" : session.status === "cancelled" ? "已取消" : "已结束" }}</span></td><td>{{ formatDate(session.created_at) }}</td><td><button class="text-button" @click.stop="openSession(session)">检查</button></td></tr><tr v-if="!loading && !sessions.length"><td colspan="7" class="manager-empty">没有符合筛选条件的会话。</td></tr></tbody></table></div>
      </section>
    </template>
  </main>
</template>

<style scoped>
.agent-manager { gap: 14px; }
.manager-header { display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; }
.manager-header h1 { margin-bottom: 5px; }
.manager-header p { margin: 0; color: #6e7e76; font-size: 11px; }
.manager-tabs { display: flex; gap: 17px; border-bottom: 1px solid #d9e1dc; }
.manager-tabs button { display: flex; align-items: center; gap: 7px; min-height: 36px; padding: 0 2px; color: #728079; background: transparent; border: 0; border-bottom: 2px solid transparent; font-size: 10px; cursor: pointer; }
.manager-tabs button.active { color: #2c5b4a; border-bottom-color: #37735a; }
.manager-tabs button span { min-width: 17px; padding: 2px 4px; color: #77877e; background: #edf2ee; border-radius: 8px; font-size: 8px; text-align: center; }
.agent-manager-layout { display: grid; grid-template-columns: minmax(230px, .7fr) minmax(430px, 1.5fr); align-items: stretch; gap: 11px; min-height: 430px; }
.manager-agent-index, .manager-agent-detail, .manager-sessions-panel { min-width: 0; background: #fff; border: 1px solid #d8e0db; border-radius: 4px; }
.manager-agent-index { padding: 0 11px 10px; }
.manager-panel-header { display: flex; justify-content: space-between; align-items: center; gap: 12px; padding: 12px 1px 10px; border-bottom: 1px solid #e5eae7; }
.manager-panel-header h2, .manager-panel-header h3 { margin: 0 0 3px; color: #34483e; font-size: 11px; }
.manager-panel-header p { margin: 0; color: #7d8983; font-size: 9px; }
.manager-panel-header label { display: flex; align-items: center; gap: 6px; color: #748179; font-size: 9px; white-space: nowrap; }
.manager-panel-header select { min-height: 29px; padding: 4px 6px; background: #fafcfb; border: 1px solid #d8e0db; border-radius: 3px; color: #43554b; font-size: 9px; }
.manager-agent-row { display: grid; grid-template-columns: 22px minmax(0, 1fr) auto; align-items: center; gap: 8px; width: 100%; padding: 10px 6px; color: #405148; background: transparent; border: 0; border-bottom: 1px solid #edf0ee; text-align: left; cursor: pointer; }
.manager-agent-row:hover { background: #f7f9f7; }
.manager-agent-row.selected { background: #edf4ef; box-shadow: inset 2px 0 #3c765c; }
.manager-agent-mark { color: #548068; font-size: 13px; }
.manager-agent-name { min-width: 0; }
.manager-agent-name strong, .manager-agent-name code { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.manager-agent-name strong { font-size: 10px; }
.manager-agent-name code { margin-top: 3px; color: #89958f; font-size: 8px; }
.manager-agent-version { padding: 3px 5px; color: #5b7567; background: #e4eee7; border-radius: 2px; font-size: 8px; }
.manager-agent-detail { padding: 0 15px 15px; }
.manager-detail-header { display: flex; justify-content: space-between; align-items: flex-start; gap: 14px; padding: 16px 0 13px; border-bottom: 1px solid #e3e9e5; }
.manager-resource-kind { display: inline-block; margin-bottom: 5px; color: #6d8377; font-size: 9px; }
.manager-detail-header h2 { margin: 0 0 4px; color: #2f4339; font-size: 17px; }
.manager-detail-header p { margin: 0 0 5px; color: #748179; font-size: 10px; }
.manager-detail-header code { color: #88958e; font-size: 8px; }
.manager-detail-actions { display: flex; align-items: center; gap: 7px; }
.manager-scope-row { display: flex; align-items: center; flex-wrap: wrap; gap: 6px; padding: 11px 0; border-bottom: 1px solid #e5eae7; }
.manager-scope-row > strong { margin-right: 4px; color: #66766d; font-size: 9px; }
.manager-scope-row > span { padding: 4px 6px; color: #557161; background: #eef4ef; border-radius: 2px; font-size: 8px; }
.manager-scope-row em { color: #8c6b43; font-size: 8px; font-style: normal; }
.manager-version-section { margin-top: 4px; }
.manager-version-list article { display: grid; grid-template-columns: 9px minmax(100px, 1fr) auto auto; align-items: center; gap: 8px; padding: 9px 3px; border-bottom: 1px solid #edf0ee; }
.manager-version-list article.chosen { background: #f6f9f7; }
.version-marker { width: 6px; height: 6px; border-radius: 50%; background: #a8b4ae; }
.chosen .version-marker { background: #4f8a66; }
.manager-version-list strong, .manager-version-list small { display: block; }
.manager-version-list strong { color: #43574c; font-size: 9px; }
.manager-version-list small { margin-top: 3px; color: #859189; font-size: 8px; }
.manager-version-list time { color: #849189; font-size: 8px; white-space: nowrap; }
.manager-session-form { margin-top: 12px; padding: 0 10px 10px; background: #f7faf8; border: 1px solid #dfe8e2; border-radius: 3px; }
.manager-session-form .manager-panel-header { padding-top: 10px; }
.manager-input-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px; padding: 11px 0; }
.manager-input-grid label { color: #56675d; font-size: 9px; }
.manager-input-grid input { min-height: 31px; padding: 6px 8px; color: #34453b; background: #fff; border: 1px solid #d5ded8; border-radius: 3px; font-size: 9px; }
.manager-input-grid input[type="checkbox"] { width: 14px; }
.manager-input-grid small { color: #8a958e; font-size: 8px; }
.manager-session-form footer { display: flex; justify-content: space-between; align-items: center; gap: 8px; padding-top: 9px; border-top: 1px solid #e2e9e4; }
.manager-session-form footer span { color: #829087; font-size: 8px; }
.manager-empty { display: flex; flex-direction: column; align-items: center; gap: 5px; padding: 27px 12px; color: #87938c; font-size: 9px; text-align: center; }
.manager-empty strong { color: #53635a; font-size: 10px; }
.manager-empty a { color: #37735a; font-size: 9px; }
.manager-empty-detail { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
.manager-empty-detail > span { display: grid; place-items: center; width: 40px; height: 40px; margin-bottom: 8px; color: #4e7d62; background: #e8f0ea; border-radius: 50%; font-size: 18px; }
.manager-empty-detail h2 { margin: 0 0 5px; font-size: 13px; }
.manager-empty-detail p { max-width: 260px; margin: 0; color: #849088; font-size: 9px; line-height: 1.5; }
.manager-sessions-panel { overflow: hidden; }
.session-filter-bar { display: flex; align-items: flex-end; flex-wrap: wrap; gap: 8px; padding: 11px; border-bottom: 1px solid #e2e8e4; }
.session-filter-bar label { display: grid; gap: 4px; color: #6d7b73; font-size: 8px; }
.session-filter-bar input, .session-filter-bar select { min-width: 145px; min-height: 31px; padding: 5px 8px; color: #405249; background: #fcfdfc; border: 1px solid #d6dfd9; border-radius: 3px; font-size: 9px; }
.filter-result-count { margin-left: auto; padding-bottom: 8px; color: #87938c; font-size: 8px; }
.manager-table-wrap { overflow-x: auto; }
.manager-session-table { width: 100%; border-collapse: collapse; white-space: nowrap; }
.manager-session-table th { padding: 9px 10px; color: #78857e; background: #f4f7f5; border-bottom: 1px solid #dfe6e1; text-align: left; font-size: 8px; font-weight: 500; }
.manager-session-table td { padding: 10px; color: #5a6961; border-bottom: 1px solid #edf0ee; font-size: 9px; }
.manager-session-table tbody tr:not(:last-child) { cursor: pointer; }
.manager-session-table tbody tr:hover td { background: #f8faf8; }
.manager-session-table td strong, .manager-session-table td code { display: block; }
.manager-session-table td strong { color: #405248; font-size: 9px; }
.manager-session-table td code { margin-top: 3px; color: #89958e; font-size: 8px; }
.manager-table-version { color: #587463; }
.manager-table-status { display: inline-block; padding: 3px 6px; color: #4a7559; background: #e8f1e9; border-radius: 2px; font-size: 8px; }
.manager-table-status.status-closed, .manager-table-status.status-cancelled { color: #747f78; background: #eef1ef; }
@media (max-width: 900px) { .agent-manager-layout { grid-template-columns: 1fr; }.manager-agent-index { padding-bottom: 2px; }.manager-agent-detail { min-height: 300px; } }
@media (max-width: 600px) { .manager-header { align-items: flex-start; flex-direction: column; }.manager-detail-header { flex-direction: column; }.manager-detail-actions { width: 100%; }.manager-input-grid { grid-template-columns: 1fr; }.manager-version-list article { grid-template-columns: 9px 1fr auto; }.manager-version-list .text-button { grid-column: 2 / -1; justify-self: start; }.session-filter-bar { align-items: stretch; flex-direction: column; }.session-filter-bar label, .session-filter-bar input, .session-filter-bar select { width: 100%; }.filter-result-count { margin-left: 0; }.manager-table-wrap { border-top: 1px solid #edf0ee; } }
</style>
