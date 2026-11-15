<script setup lang="ts">
import { Handle, Position } from "@xyflow/vue";

defineProps<{ data: Record<string, any>; selected: boolean }>();
</script>

<template>
  <article class="canvas-action-card" :class="{ selected, disabled: !data.enabled }">
    <Handle type="target" :position="Position.Left" />
    <header><span class="canvas-action-glyph">↗</span><span><small>Action</small><strong>{{ data.display_name }}</strong><code>{{ data.api_name }}</code></span></header>
    <footer><span>{{ data.enabled ? "已启用" : "已停用" }}</span><b>{{ data.object_type_api_name }}</b></footer>
  </article>
</template>
