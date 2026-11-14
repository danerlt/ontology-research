<script setup lang="ts">
import { onMounted, ref } from "vue";
import { api, readableError } from "../api/client";
import ProposalReview from "../components/ProposalReview.vue";
import { useAuthStore } from "../stores/auth";
import type { Ontology, Proposal } from "../types";

const auth = useAuthStore();
const ontology = ref<Ontology | null>(null);
const proposals = ref<Proposal[]>([]);
const title = ref("");
const objectTypeName = ref("");
const objectTypeLabel = ref("");
const description = ref("");
const error = ref("");
const notice = ref("");
const loading = ref(false);

async function loadProposals() {
  loading.value = true;
  error.value = "";
  try {
    const ontologies = await api.get<Ontology[]>("/api/ontology");
    ontology.value = ontologies[0] ?? null;
    proposals.value = await api.get<Proposal[]>("/api/proposals", { ontology_id: ontology.value?.id });
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function createProposal() {
  if (!ontology.value) return;
  error.value = "";
  notice.value = "";
  try {
    await api.post<Proposal>("/api/proposals", {
      ontology_id: ontology.value.id,
      title: title.value,
      description: description.value,
      base_revision: ontology.value.revision,
      changes: [{ op: "add_object_type", api_name: objectTypeName.value, display_name: objectTypeLabel.value }],
    });
    title.value = "";
    objectTypeName.value = "";
    objectTypeLabel.value = "";
    description.value = "";
    notice.value = "提案草稿已创建。提交审阅后，管理员可以批准合并。";
    await loadProposals();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function submitProposal(id: string) {
  await mutate(`/api/proposals/${id}/submit`, {}, "提案已提交审阅。");
}

async function mergeProposal(id: string) {
  await mutate(`/api/proposals/${id}/merge`, {}, "提案已合并，本体版本已更新。");
}

async function rejectProposal(id: string) {
  await mutate(`/api/proposals/${id}/reject`, { reason: "请根据审阅意见修订后重新提交。" }, "提案已驳回并记录原因。");
}

async function mutate(path: string, body: unknown, success: string) {
  error.value = "";
  try {
    await api.post(path, body);
    notice.value = success;
    await loadProposals();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

const statusLabels: Record<string, string> = { draft: "草稿", submitted: "待审阅", merged: "已合并", rejected: "已驳回" };
onMounted(loadProposals);
</script>

<template>
  <div class="page-content">
    <div class="page-heading"><div><span class="eyebrow">结构治理</span><h1>变更提案</h1><p>结构修改先进入审阅流程，批准后才会写入当前本体版本。</p></div><span class="revision-pill">当前版本 <b>v{{ ontology?.revision || 1 }}</b></span></div>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div><div v-if="notice" class="notice notice-success">{{ notice }}</div>
    <section v-if="auth.role === 'admin' || auth.role === 'editor'" class="proposal-create-panel"><div class="section-heading"><div><h2>创建结构提案</h2><p>当前表单创建一个新对象类型；属性和链接可后续作为单独变更扩展。</p></div><span class="step-mark">草稿 → 审阅 → 合并</span></div><form class="proposal-form" @submit.prevent="createProposal"><label>提案标题<input v-model="title" required maxlength="240" placeholder="例如：新增供应商对象" /></label><div class="form-grid"><label>对象显示名称<input v-model="objectTypeLabel" required placeholder="供应商" /></label><label>对象 API 名称<input v-model="objectTypeName" required pattern="[a-z][a-z0-9_]*" placeholder="supplier" /></label></div><label>变更说明<textarea v-model="description" rows="2" placeholder="描述新增对象类型的业务用途" /></label><button class="button button-primary" :disabled="!title || !objectTypeName || !objectTypeLabel">保存提案草稿</button></form></section>
    <section class="proposal-list-panel"><div class="section-heading"><div><h2>提案记录</h2><p>按最新创建时间排列，所有状态转换均会写入审计。</p></div><button class="button button-quiet" @click="loadProposals">重新加载</button></div><div v-if="loading" class="empty-state compact">正在读取提案…</div><div v-else-if="proposals.length" class="proposal-list"><div v-for="proposal in proposals" :key="proposal.id" class="proposal-card"><div class="proposal-card-meta"><span class="status-badge" :class="`status-${proposal.status}`">{{ statusLabels[proposal.status] || proposal.status }}</span><code>基于 v{{ proposal.base_revision }}</code><time>{{ new Date(proposal.created_at).toLocaleString("zh-CN") }}</time></div><ProposalReview :proposal="{ id: proposal.id, title: proposal.title, status: proposal.status }" :role="auth.role" @submit="submitProposal" @merge="mergeProposal" @reject="rejectProposal" /><p v-if="proposal.description" class="proposal-description">{{ proposal.description }}</p><div class="change-chips"><span v-for="(change, index) in proposal.changes" :key="index">{{ change.op === "add_object_type" ? `新增对象类型 · ${change.display_name}` : change.op }}</span></div></div></div><div v-else class="empty-state"><strong>还没有结构提案</strong><span>从上方创建一份草稿，邀请管理员审阅本体变化。</span></div></section>
  </div>
</template>
