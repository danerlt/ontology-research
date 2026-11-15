<script setup lang="ts">
import { onMounted, ref } from "vue";
import { api, readableError } from "../api/client";
import ProposalReview from "../components/ProposalReview.vue";
import { useAuthStore } from "../stores/auth";
import type { Ontology, Proposal } from "../types";

const auth = useAuthStore();
const ontology = ref<Ontology | null>(null);
const proposals = ref<Proposal[]>([]);
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

async function submitProposal(id: string) {
  await mutate(`/api/proposals/${id}/submit`, {}, "提案已提交审阅。");
}

async function reviewResource(input: { proposal_id: string; resource_key: string; status: "approved" | "rejected"; comment: string }) {
  const statusLabel = input.status === "approved" ? "已通过" : "已退回修改";
  await mutate(
    `/api/proposals/${input.proposal_id}/resources/${encodeURIComponent(input.resource_key)}/review`,
    { status: input.status, comment: input.comment },
    `资源 ${input.resource_key} ${statusLabel}。`,
  );
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
    <section v-if="auth.role === 'admin' || auth.role === 'editor'" class="proposal-create-panel proposal-entry-panel"><div class="section-heading"><div><h2>从分支提交本体变更</h2><p>对象类型、属性、链接与 Action 先在隔离分支中编辑，再提交逐资源评审。</p></div><span class="step-mark">草稿 → 校验 → 评审 → 合并</span></div><RouterLink class="button button-primary" to="/branches">打开分支工作区</RouterLink></section>
    <section class="proposal-list-panel"><div class="section-heading"><div><h2>提案记录</h2><p>按最新创建时间排列，所有状态转换均会写入审计。</p></div><button class="button button-quiet" @click="loadProposals">重新加载</button></div><div v-if="loading" class="empty-state compact">正在读取提案…</div><div v-else-if="proposals.length" class="proposal-list"><div v-for="proposal in proposals" :key="proposal.id" class="proposal-card"><div class="proposal-card-meta"><span class="status-badge" :class="`status-${proposal.status}`">{{ statusLabels[proposal.status] || proposal.status }}</span><code>基于 v{{ proposal.base_revision }}</code><time>{{ new Date(proposal.created_at).toLocaleString("zh-CN") }}</time></div><ProposalReview :proposal="{ id: proposal.id, title: proposal.title, status: proposal.status, resource_reviews: proposal.resource_reviews }" :role="auth.role" @submit="submitProposal" @merge="mergeProposal" @reject="rejectProposal" @review="reviewResource" /><p v-if="proposal.description" class="proposal-description">{{ proposal.description }}</p><div class="change-chips"><span v-for="(change, index) in proposal.changes" :key="index">{{ change.op === "add_object_type" ? `新增对象类型 · ${change.display_name}` : change.op }}</span></div></div></div><div v-else class="empty-state"><strong>还没有结构提案</strong><span>从上方创建一份草稿，邀请管理员审阅本体变化。</span></div></section>
  </div>
</template>
