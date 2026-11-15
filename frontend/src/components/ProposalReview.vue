<script setup lang="ts">
import { computed, ref } from "vue";

const props = defineProps<{
  role: string;
  proposal: {
    id: string;
    title: string;
    status: string;
    author?: string;
    resource_reviews?: Array<{
      id: string;
      resource_key: string;
      status: string;
      reviewer_id: string | null;
      comment: string;
    }>;
  };
}>();
const emit = defineEmits<{
  merge: [id: string];
  reject: [id: string];
  submit: [id: string];
  review: [input: { proposal_id: string; resource_key: string; status: "approved" | "rejected"; comment: string }];
}>();
const comments = ref<Record<string, string>>({});
const canMerge = computed(() => !props.proposal.resource_reviews?.length || props.proposal.resource_reviews.every((item) => item.status === "approved"));
const reviewStatusLabels: Record<string, string> = { pending: "待评审", approved: "已通过", rejected: "需修改" };

function submitResourceReview(resourceKey: string, status: "approved" | "rejected") {
  emit("review", {
    proposal_id: props.proposal.id,
    resource_key: resourceKey,
    status,
    comment: comments.value[resourceKey] ?? "",
  });
}
</script>

<template>
  <article class="proposal-row">
    <div class="proposal-copy">
      <strong>{{ proposal.title }}</strong>
      <span>{{ proposal.author || "本体结构变更" }}</span>
    </div>
    <div class="proposal-actions">
      <button
        v-if="role === 'admin' && proposal.status === 'submitted'"
        data-action="merge"
        class="button button-primary"
        :disabled="!canMerge"
        @click="emit('merge', proposal.id)"
      >批准合并</button>
      <button
        v-if="role === 'admin' && proposal.status === 'submitted'"
        data-action="reject"
        class="button button-quiet"
        @click="emit('reject', proposal.id)"
      >驳回</button>
      <button
        v-if="(role === 'admin' || role === 'editor') && proposal.status === 'draft'"
        data-action="submit"
        class="button button-quiet"
        @click="emit('submit', proposal.id)"
      >提交审阅</button>
      <span v-if="proposal.status !== 'draft' && proposal.status !== 'submitted'" class="status-note">{{ proposal.status }}</span>
    </div>
  </article>
  <section v-if="proposal.resource_reviews?.length" class="resource-review-list" aria-label="逐资源评审">
    <h3>逐资源评审</h3>
    <article v-for="review in proposal.resource_reviews" :key="review.id" class="resource-review-row" data-action="resource-review">
      <div class="resource-review-heading">
        <code>{{ review.resource_key }}</code>
        <span class="status-badge" :class="`status-${review.status}`">{{ reviewStatusLabels[review.status] || review.status }}</span>
      </div>
      <p v-if="review.comment" class="resource-review-comment">{{ review.comment }}</p>
      <template v-if="role === 'admin' && proposal.status === 'submitted'">
        <label class="resource-review-comment-field">评审意见<input v-model="comments[review.resource_key]" :aria-label="`评审意见 ${review.resource_key}`" placeholder="可选，记录判断依据" maxlength="2000" /></label>
        <div class="resource-review-actions">
          <button class="button button-primary" data-action="approve-resource" @click="submitResourceReview(review.resource_key, 'approved')">通过此资源</button>
          <button class="button button-quiet" data-action="reject-resource" @click="submitResourceReview(review.resource_key, 'rejected')">退回此资源</button>
        </div>
      </template>
    </article>
  </section>
</template>
