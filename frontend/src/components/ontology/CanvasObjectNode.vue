<script setup lang="ts">
import { computed } from "vue";
import { Handle, Position } from "@xyflow/vue";

const props = defineProps<{ data: Record<string, any>; selected: boolean }>();
const nativeProperties = computed(() => (props.data.properties ?? []).filter((item: Record<string, any>) => !item.is_derived));
const derivedProperties = computed(() => (props.data.properties ?? []).filter((item: Record<string, any>) => item.is_derived));
</script>

<template>
  <article class="canvas-object-card" :class="{ selected, 'has-derived': derivedProperties.length }">
    <Handle type="target" :position="Position.Left" />
    <header class="canvas-object-heading">
      <span class="canvas-object-glyph">{{ data.icon === "object" ? "◈" : data.icon?.slice(0, 1).toUpperCase() || "◈" }}</span>
      <span class="canvas-node-title"><strong>{{ data.display_name }}</strong><code>{{ data.api_name }}</code></span>
      <span class="canvas-node-kind">对象类型</span>
    </header>
    <p v-if="data.description" class="canvas-node-description">{{ data.description }}</p>
    <div class="canvas-node-resource-line"><span>原生属性</span><b>{{ nativeProperties.length }}</b><span>推导属性</span><b class="derived-count">{{ derivedProperties.length }}</b></div>
    <div class="canvas-property-list">
      <span v-for="property in nativeProperties.slice(0, 4)" :key="property.api_name" class="canvas-property-chip"><i>◻</i>{{ property.display_name || property.api_name }}<code>{{ property.data_type }}</code></span>
      <span v-for="property in data.showDerived ? derivedProperties.slice(0, 3) : []" :key="property.api_name" class="canvas-property-chip is-derived"><i>ƒ</i>{{ property.display_name || property.api_name }}<code>{{ property.data_type }}</code></span>
      <span v-if="nativeProperties.length > 4" class="canvas-property-more">+{{ nativeProperties.length - 4 }} 个属性</span>
    </div>
    <footer v-if="data.actions?.length" class="canvas-object-footer">可用 Action <span>{{ data.actions.length }}</span></footer>
    <Handle type="source" :position="Position.Right" />
  </article>
</template>
