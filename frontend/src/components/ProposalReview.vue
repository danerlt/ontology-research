<script setup lang="ts">
defineProps<{
  role: string;
  proposal: { id: string; title: string; status: string; author?: string };
}>();
const emit = defineEmits<{ merge: [id: string]; reject: [id: string]; submit: [id: string] }>();
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
</template>
