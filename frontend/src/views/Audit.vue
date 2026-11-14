<script setup lang="ts">
import { onMounted, ref } from "vue";
import { api, readableError } from "../api/client";

interface AuditEvent {
  id: string;
  actor_email?: string;
  event_type: string;
  resource_type: string;
  resource_id: string;
  details: Record<string, unknown>;
  created_at: string;
}
const events = ref<AuditEvent[]>([]);
const total = ref(0);
const page = ref(1);
const error = ref("");
const loading = ref(false);
const filters = ref({ event_type: "", resource_type: "" });

async function loadEvents() {
  loading.value = true;
  error.value = "";
  try {
    const result = await api.get<{ data: AuditEvent[]; total: number }>("/api/audit-events", {
      event_type: filters.value.event_type,
      resource_type: filters.value.resource_type,
      page: page.value,
      page_size: 25,
    });
    events.value = result.data;
    total.value = result.total;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

function describe(event: AuditEvent): string {
  const names: Record<string, string> = {
    "object.created": "创建了对象",
    "object.linked": "建立了对象关系",
    "action.executed": "执行了 Action",
    "schema.proposal.created": "创建了结构提案",
    "schema.proposal.submitted": "提交了结构提案",
    "schema.proposal.merged": "合并了结构提案",
    "schema.proposal.rejected": "驳回了结构提案",
  };
  return names[event.event_type] || event.event_type;
}

onMounted(loadEvents);
</script>

<template>
  <div class="page-content">
    <div class="page-heading"><div><span class="eyebrow">操作追踪</span><h1>审计记录</h1><p>查看对象写入、Action 执行和本体结构审阅历史。</p></div><button class="button button-quiet" @click="loadEvents">重新加载</button></div>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div>
    <section class="audit-panel"><div class="audit-toolbar"><label>事件类型<input v-model="filters.event_type" placeholder="例如 action.executed" @keyup.enter="loadEvents" /></label><label>资源类型<input v-model="filters.resource_type" placeholder="object / proposal" @keyup.enter="loadEvents" /></label><button class="button button-primary" @click="page = 1; loadEvents()">筛选</button><span class="audit-total">共 {{ total }} 条</span></div><div v-if="loading" class="empty-state compact">正在读取审计记录…</div><div v-else-if="events.length" class="table-wrap"><table><thead><tr><th>时间</th><th>操作</th><th>操作者</th><th>资源</th><th>详情</th></tr></thead><tbody><tr v-for="event in events" :key="event.id"><td>{{ new Date(event.created_at).toLocaleString("zh-CN") }}</td><td><span class="event-type-chip">{{ describe(event) }}</span><code>{{ event.event_type }}</code></td><td>{{ event.actor_email || "系统" }}</td><td><span>{{ event.resource_type }}</span><code>{{ event.resource_id }}</code></td><td><details><summary>查看</summary><pre>{{ JSON.stringify(event.details, null, 2) }}</pre></details></td></tr></tbody></table></div><div v-else class="empty-state"><strong>没有审计记录</strong><span>执行对象操作、Action 或结构审阅后，记录会出现在这里。</span></div><div class="pagination"><button class="button button-quiet" :disabled="page <= 1" @click="page--; loadEvents()">上一页</button><span>第 {{ page }} 页</span><button class="button button-quiet" :disabled="page * 25 >= total" @click="page++; loadEvents()">下一页</button></div></section>
  </div>
</template>
