<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { api, readableError } from "../api/client";
import AgentTools from "../components/AgentTools.vue";
import type { AgentConfiguration, AgentSession } from "../types";

interface AgentEvent {
  id: string;
  sequence: number;
  event_type: string;
  tool_name: string | null;
  status: string;
  details: Record<string, unknown>;
  created_at: string;
}

interface SessionDetail extends AgentSession {
  config: AgentConfiguration;
  events: AgentEvent[];
}

const route = useRoute();
const sessionId = computed(() => String(route.params.sessionId));
const detail = ref<SessionDetail | null>(null);
const error = ref("");
const notice = ref("");
const recentResult = ref<unknown>(null);
const busy = ref(false);
const messageDraft = ref("");
const transcript = computed(() => (detail.value?.events ?? [])
  .filter((event) => ["message.initial", "message.user", "message.assistant"].includes(event.event_type))
  .map((event) => ({
    id: event.id,
    role: event.event_type === "message.assistant" ? "智能体" : event.event_type === "message.initial" ? "初始任务" : "你",
    content: typeof event.details.content === "string" ? event.details.content : "",
    created_at: event.created_at,
  })));
const canRunInitialTask = computed(() => Boolean(
  detail.value?.config.model_provider === "openai-compatible"
  && detail.value.status === "active"
  && detail.value.config.initial_user_message.trim()
  && transcript.value.length === 0,
));

const statusText = computed(() => {
  if (!detail.value) return "读取中";
  if (detail.value.status === "active") return "运行中";
  if (detail.value.status === "cancelled") return "已取消";
  return "已结束";
});

async function loadSession() {
  error.value = "";
  try {
    detail.value = await api.get<SessionDetail>(`/api/sessions/${sessionId.value}`, undefined, "/agent-api");
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function endSession(action: "cancel" | "close") {
  if (!detail.value || detail.value.status !== "active") return;
  busy.value = true;
  error.value = "";
  try {
    const updated = await api.post<AgentSession>(`/api/sessions/${sessionId.value}/${action}`, {}, "/agent-api");
    detail.value = { ...detail.value, ...updated };
    notice.value = action === "cancel" ? "会话已取消，运行事件已保留。" : "会话已结束，运行事件已保留。";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

async function callTool(toolName: string, arguments_: Record<string, unknown>) {
  if (!detail.value) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const response = await api.post<{ result: unknown }>(
      `/api/sessions/${sessionId.value}/tools/${toolName}`,
      { arguments: arguments_ },
      "/agent-api",
    );
    recentResult.value = response.result;
    notice.value = `工具“${toolName}”已运行，结果和授权记录已写入事件时间线。`;
    await loadSession();
  } catch (cause) {
    error.value = readableError(cause);
    await loadSession();
  } finally {
    busy.value = false;
  }
}

async function sendMessage(useInitialTask = false) {
  if (!detail.value || detail.value.status !== "active" || busy.value) return;
  const content = messageDraft.value.trim();
  if (!content && !useInitialTask) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const response = await api.post<{ assistant_message: string; tool_calls: string[] }>(
      `/api/sessions/${sessionId.value}/messages`,
      { content },
      "/agent-api",
    );
    messageDraft.value = "";
    notice.value = response.tool_calls.length
      ? `智能体已回复，并运行 ${response.tool_calls.length} 次获准工具；完整 trace 已记录。`
      : "智能体已回复；本轮模型与令牌用量已写入时间线。";
    await loadSession();
  } catch (cause) {
    error.value = readableError(cause);
    await loadSession();
  } finally {
    busy.value = false;
  }
}

function eventName(event: AgentEvent): string {
  if (event.event_type === "session.created") return "会话已创建";
  if (event.event_type === "session.cancelled") return "会话已取消";
  if (event.event_type === "session.closed") return "会话已结束";
  if (event.event_type === "tool.denied") return "工具调用被拒绝";
  if (event.event_type === "tool.called") return `运行工具 ${event.tool_name || "未知工具"}`;
  return event.event_type;
}

function formatTimestamp(value: string): string {
  return new Date(value).toLocaleString("zh-CN", { hour12: false });
}

onMounted(loadSession);
</script>

<template>
  <main class="session-inspector page-content">
    <header class="session-inspector-header">
      <div>
        <RouterLink to="/sessions" class="session-back-link">← 返回运行会话</RouterLink>
        <h1>{{ detail ? `${detail.config.model_name} · 会话检查器` : "会话检查器" }}</h1>
        <p>检查固定版本的输入、上下文快照、工具结果和运行事件。</p>
      </div>
      <div class="session-header-actions">
        <span class="run-status" :class="`status-${detail?.status || 'loading'}`"><i />{{ statusText }}</span>
        <button class="button button-quiet" @click="loadSession">刷新事件</button>
        <button v-if="detail?.status === 'active'" class="button button-danger" data-action="cancel-session" :disabled="busy" @click="endSession('cancel')">取消会话</button>
      </div>
    </header>

    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div>
    <div v-if="notice" class="notice notice-success" role="status">{{ notice }}</div>

    <div v-if="detail" class="session-inspector-layout">
      <aside class="session-context-panel">
        <div class="session-panel-heading"><span>会话上下文</span><span>v{{ detail.version_number }}</span></div>
        <dl class="session-context-list">
          <div><dt>智能体</dt><dd>{{ detail.agent_id }}</dd></div>
          <div><dt>固定版本</dt><dd>版本 {{ detail.version_number }}</dd></div>
          <div><dt>来源应用</dt><dd>{{ detail.origin_resource }}</dd></div>
          <div><dt>启动时间</dt><dd>{{ formatTimestamp(detail.created_at) }}</dd></div>
          <div><dt>模型配置</dt><dd>{{ detail.config.model_provider }} / {{ detail.config.model_name }}</dd></div>
          <div><dt>完成策略</dt><dd>{{ detail.config.session_completion.mode === "stays_open" ? "保持开放" : "有效输出后结束" }}</dd></div>
        </dl>
        <section class="session-input-snapshot"><h2>初始输入</h2><dl v-if="Object.keys(detail.inputs).length"><div v-for="(value, name) in detail.inputs" :key="name"><dt>{{ name }}</dt><dd>{{ value }}</dd></div></dl><p v-else class="session-empty">此会话未配置输入。</p></section>
        <section class="session-prompt-snapshot"><h2>发布时系统提示词</h2><pre>{{ detail.config.system_prompt }}</pre></section>
      </aside>

      <section class="session-timeline-panel">
        <header class="session-panel-heading"><div><span>运行时间线</span><small>{{ detail.events.length }} 条持久化事件</small></div><button class="text-button" @click="loadSession">重新读取</button></header>
        <div v-if="detail.events.length" class="session-event-list">
          <article v-for="event in detail.events" :key="event.id" class="session-event-row">
            <div class="session-event-marker"><span :class="`event-mark-${event.status}`" /></div>
            <div class="session-event-content">
              <header><strong>事件 {{ String(event.sequence).padStart(2, "0") }} · {{ eventName(event) }}</strong><time>{{ formatTimestamp(event.created_at) }}</time></header>
              <div class="session-event-meta"><span>{{ event.status === "succeeded" ? "成功" : event.status === "denied" ? "拒绝" : event.status === "failed" ? "失败" : event.status }}</span><code v-if="event.tool_name">{{ event.tool_name }}</code></div>
              <details v-if="Object.keys(event.details).length"><summary>查看事件载荷</summary><pre>{{ JSON.stringify(event.details, null, 2) }}</pre></details>
            </div>
          </article>
        </div>
        <div v-else class="session-empty">尚无运行事件。</div>
      </section>

      <aside class="session-runtime-panel">
        <template v-if="detail.config.model_provider === 'openai-compatible'">
          <header class="session-panel-heading"><span>Agent 对话</span><span>{{ detail.config.model_name }}</span></header>
          <div class="session-chat-history" aria-label="会话对话记录">
            <article v-for="message in transcript" :key="message.id" class="session-chat-message" :class="message.role === '智能体' ? 'message-agent' : 'message-user'">
              <header><strong>{{ message.role }}</strong><time>{{ formatTimestamp(message.created_at) }}</time></header><p>{{ message.content }}</p>
            </article>
            <div v-if="!transcript.length" class="session-empty">尚无对话。可运行已配置的初始任务，或直接发送消息。</div>
          </div>
          <button v-if="canRunInitialTask" class="button button-quiet session-initial-run" data-action="run-initial-task" :disabled="busy" @click="sendMessage(true)">运行初始任务</button>
          <form v-if="detail.status === 'active'" class="session-composer" aria-label="发送会话消息" @submit.prevent="sendMessage()">
            <textarea v-model="messageDraft" aria-label="会话消息" rows="3" placeholder="向此版本的 Agent 发送消息…" @keydown.ctrl.enter.prevent="sendMessage()" />
            <footer><span>模型密钥仅由服务端环境读取</span><button class="button button-primary" data-action="send-agent-message" :disabled="busy || !messageDraft.trim()">{{ busy ? "运行中…" : "发送" }}</button></footer>
          </form>
          <p v-else class="session-empty">会话已停止；对话为只读检查。</p>
          <details class="session-manual-tools"><summary>手动调试获准工具</summary><AgentTools :allowed-tools="detail.config.allowed_tools" :session-active="detail.status === 'active' && !busy" @call-tool="callTool" @invalid-input="(message) => error = message" /></details>
        </template>
        <template v-else>
          <header class="session-panel-heading"><span>本地确定性预览模式</span><span>{{ detail.status === "active" ? "工具可调试" : "只读检查" }}</span></header>
          <p class="session-runtime-note">当前版本不会生成模型回复。运行者可以显式调用已授权工具，并检查服务端记录的结果与拒绝原因。</p>
          <AgentTools v-if="detail.status === 'active'" :allowed-tools="detail.config.allowed_tools" :session-active="!busy" @call-tool="callTool" @invalid-input="(message) => error = message" />
          <p v-else class="session-empty">会话已停止；工具调用入口已锁定。</p>
        </template>
        <section class="session-recent-result"><h2>最近结果</h2><pre v-if="recentResult !== null">{{ JSON.stringify(recentResult, null, 2) }}</pre><p v-else class="session-empty">本页尚无新工具调用。可从事件载荷检查历史结果。</p></section>
      </aside>
    </div>
    <div v-else-if="!error" class="session-loading">正在读取会话上下文…</div>
  </main>
</template>

<style scoped>
.session-inspector { gap: 15px; }
.session-inspector-header { display: flex; justify-content: space-between; align-items: flex-end; gap: 18px; padding-bottom: 13px; border-bottom: 1px solid #d7dfdb; }
.session-back-link { display: inline-block; margin-bottom: 8px; color: #66746f; font-size: 11px; }
.session-inspector-header h1 { margin-bottom: 5px; }
.session-inspector-header p { margin: 0; color: #66746f; font-size: 11px; }
.session-header-actions { display: flex; align-items: center; gap: 8px; }
.run-status { display: inline-flex; align-items: center; gap: 6px; padding: 5px 8px; color: #456b56; background: #e7f0e9; border-radius: 3px; font-size: 9px; white-space: nowrap; }
.run-status i { width: 6px; height: 6px; border-radius: 50%; background: #5c9b70; }
.run-status.status-cancelled, .run-status.status-closed { color: #6f7974; background: #edf0ee; }
.run-status.status-cancelled i, .run-status.status-closed i { background: #89948e; }
.button-danger { display: inline-flex; align-items: center; min-height: 35px; padding: 0 12px; color: #9e4f43; background: #fff; border: 1px solid #e4c9c3; border-radius: 4px; font-size: 10px; cursor: pointer; }
.button-danger:disabled { opacity: .55; cursor: wait; }
.session-inspector-layout { display: grid; grid-template-columns: minmax(220px, .72fr) minmax(300px, 1fr) minmax(300px, 1fr); align-items: start; gap: 11px; }
.session-context-panel, .session-timeline-panel, .session-runtime-panel { min-width: 0; background: #fff; border: 1px solid #d7dfdb; border-radius: 4px; }
.session-context-panel { padding: 12px; }
.session-panel-heading { display: flex; justify-content: space-between; align-items: center; gap: 10px; min-height: 34px; padding: 0 11px; color: #3c5046; background: #f3f6f4; border-bottom: 1px solid #e1e7e3; font-size: 10px; font-weight: 650; }
.session-context-panel > .session-panel-heading { margin: -12px -12px 7px; }
.session-panel-heading > span:last-child { color: #728178; font-size: 9px; font-weight: 400; }
.session-panel-heading small { margin-left: 8px; color: #829088; font-size: 8px; font-weight: 400; }
.session-context-list, .session-input-snapshot dl { margin: 0; }
.session-context-list > div, .session-input-snapshot dl > div { display: grid; grid-template-columns: 74px minmax(0, 1fr); gap: 7px; padding: 7px 0; border-bottom: 1px solid #edf0ee; }
.session-context-list dt, .session-input-snapshot dt { color: #87928d; font-size: 8px; }
.session-context-list dd, .session-input-snapshot dd { margin: 0; color: #405149; overflow-wrap: anywhere; font-size: 9px; }
.session-input-snapshot, .session-prompt-snapshot { margin-top: 16px; }
.session-input-snapshot h2, .session-prompt-snapshot h2, .session-recent-result h2 { margin: 0 0 7px; color: #52635a; font-size: 10px; }
.session-prompt-snapshot pre, .session-recent-result pre { max-height: 200px; margin: 0; padding: 9px; overflow: auto; color: #4e6056; background: #f4f7f5; border: 1px solid #e3e9e5; border-radius: 3px; font-size: 8px; line-height: 1.55; white-space: pre-wrap; overflow-wrap: anywhere; }
.session-timeline-panel, .session-runtime-panel { overflow: hidden; }
.session-event-list { padding: 6px 10px 12px; }
.session-event-row { display: grid; grid-template-columns: 15px minmax(0, 1fr); gap: 8px; }
.session-event-marker { position: relative; display: flex; justify-content: center; padding-top: 13px; }
.session-event-marker::after { position: absolute; top: 21px; bottom: -4px; width: 1px; content: ""; background: #d9e2dc; }
.session-event-row:last-child .session-event-marker::after { display: none; }
.session-event-marker > span { position: relative; z-index: 1; width: 7px; height: 7px; border: 1px solid #91ad9d; border-radius: 50%; background: #e7f1ea; }
.session-event-marker > .event-mark-denied, .session-event-marker > .event-mark-failed { border-color: #ba7665; background: #fbefec; }
.session-event-content { min-width: 0; padding: 11px 0; border-bottom: 1px solid #edf0ee; }
.session-event-row:last-child .session-event-content { border-bottom: 0; }
.session-event-content > header { display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; }
.session-event-content > header strong { color: #3d5147; font-size: 9px; }
.session-event-content time { color: #85918b; font-size: 8px; white-space: nowrap; }
.session-event-meta { display: flex; align-items: center; gap: 8px; margin-top: 5px; color: #7b8a82; font-size: 8px; }
.session-event-meta code { color: #577763; }
.session-event-content details { margin-top: 8px; }
.session-event-content summary { color: #547362; font-size: 8px; cursor: pointer; }
.session-event-content details pre { max-height: 180px; margin: 6px 0 0; padding: 8px; overflow: auto; color: #d8e5dd; background: #273732; border-radius: 3px; font-size: 8px; white-space: pre-wrap; overflow-wrap: anywhere; }
.session-runtime-note { margin: 10px 11px; color: #738079; font-size: 8px; line-height: 1.55; }
.session-chat-history { display: grid; gap: 8px; max-height: 380px; min-height: 160px; padding: 9px; overflow: auto; }
.session-chat-message { padding: 9px 10px; border: 1px solid #e2e9e4; border-radius: 4px; background: #f8faf8; }
.session-chat-message.message-user { background: #edf4ef; border-color: #dce9df; }
.session-chat-message > header, .session-composer footer { display: flex; justify-content: space-between; align-items: center; gap: 8px; }
.session-chat-message strong { color: #4c6958; font-size: 9px; }
.session-chat-message time { color: #87938c; font-size: 8px; }
.session-chat-message p { margin: 6px 0 0; color: #43544a; font-size: 9px; line-height: 1.6; white-space: pre-wrap; overflow-wrap: anywhere; }
.session-composer { display: grid; gap: 7px; padding: 10px; border-top: 1px solid #e3eae5; }
.session-composer textarea { width: 100%; resize: vertical; min-height: 65px; padding: 8px; color: #3e5046; background: #fff; border: 1px solid #d5dfd9; border-radius: 3px; font: inherit; font-size: 9px; }
.session-composer footer > span { color: #849188; font-size: 8px; }
.session-composer .button { min-height: 30px; padding: 0 12px; font-size: 9px; }
.session-initial-run { width: calc(100% - 20px); margin: 0 10px; }
.session-manual-tools { margin: 10px; border-top: 1px solid #e3eae5; padding-top: 9px; }
.session-manual-tools summary { color: #587463; font-size: 9px; cursor: pointer; }
.session-runtime-panel :deep(.tool-list) { padding: 0 10px 10px; }
.session-runtime-panel :deep(.tool-card) { margin-top: 7px; padding: 9px; background: #f9fbfa; border: 1px solid #e4eae6; border-radius: 3px; }
.session-runtime-panel :deep(.tool-card h3) { margin-bottom: 3px; font-size: 10px; }
.session-runtime-panel :deep(.tool-card p) { margin-bottom: 6px; color: #829087; font-size: 8px; }
.session-runtime-panel :deep(.tool-controls), .session-runtime-panel :deep(.action-inputs) { display: grid; grid-template-columns: 1fr auto; gap: 6px; }
.session-runtime-panel :deep(input), .session-runtime-panel :deep(textarea) { width: 100%; min-height: 30px; padding: 6px 7px; font-size: 9px; }
.session-runtime-panel :deep(.button) { min-height: 30px; padding: 0 8px; font-size: 8px; }
.session-runtime-panel :deep(.action-inputs textarea), .session-runtime-panel :deep(.action-inputs button) { grid-column: 1 / -1; }
.session-recent-result { margin: 0 10px 12px; padding-top: 10px; border-top: 1px solid #e5eae7; }
.session-empty, .session-loading { padding: 13px; color: #87928c; font-size: 9px; line-height: 1.5; }
.session-loading { min-height: 240px; display: grid; place-items: center; }
@media (max-width: 1180px) { .session-inspector-layout { grid-template-columns: minmax(230px, .8fr) minmax(300px, 1.2fr); }.session-runtime-panel { grid-column: 2; } }
@media (max-width: 760px) { .session-inspector-header { align-items: flex-start; flex-direction: column; }.session-header-actions { justify-content: flex-start; flex-wrap: wrap; }.session-inspector-layout { grid-template-columns: 1fr; }.session-runtime-panel { grid-column: auto; } }
</style>
