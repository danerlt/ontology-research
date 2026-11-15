<script setup lang="ts">
import { Handle, Position } from "@xyflow/vue";

defineProps<{ data: Record<string, any>; selected: boolean }>();
</script>

<template>
  <article class="canvas-system-card" :class="{ selected }">
    <Handle type="target" :position="Position.Left" />
    <header><span class="canvas-system-glyph">⇢</span><span><strong>{{ data.name }}</strong><code>{{ data.connector_type }}</code></span></header>
    <div class="canvas-system-meta"><span class="source-state-dot" :class="data.status" />{{ data.status === "ready" ? "连接可用" : data.status }}<b>{{ data.mapping_count }} 个映射</b></div>
    <Handle type="source" :position="Position.Right" />
  </article>
</template>
