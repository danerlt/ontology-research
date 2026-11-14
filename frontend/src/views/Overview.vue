<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { RouterLink } from "vue-router";
import { api, readableError } from "../api/client";
import type { LinkType, ObjectType, Ontology } from "../types";

const ontology = ref<Ontology | null>(null);
const objectTypes = ref<ObjectType[]>([]);
const linkTypes = ref<LinkType[]>([]);
const objectCount = ref(0);
const loading = ref(true);
const error = ref("");

const graphNodes = computed(() => objectTypes.value.slice(0, 5));

async function loadWorkspace() {
  loading.value = true;
  error.value = "";
  try {
    const ontologies = await api.get<Ontology[]>("/api/ontology");
    ontology.value = ontologies[0] ?? null;
    if (!ontology.value) return;
    const [types, links, records] = await Promise.all([
      api.get<ObjectType[]>("/api/object-types", { ontology_id: ontology.value.id }),
      api.get<LinkType[]>("/api/link-types", { ontology_id: ontology.value.id }),
      api.get<{ total: number }>("/api/objects", { ontology_id: ontology.value.id, page_size: 1 }),
    ]);
    objectTypes.value = types;
    linkTypes.value = links;
    objectCount.value = records.total;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

onMounted(loadWorkspace);
</script>

<template>
  <div class="overview-page">
    <div class="page-heading overview-heading">
      <div><span class="eyebrow">工作区 / 运营知识图谱</span><h1>{{ ontology?.display_name || "本体工作区" }}</h1><p>{{ ontology?.description || "用统一的业务对象、关系与操作组织运营数据。" }}</p></div>
      <RouterLink class="button button-primary" to="/ontology">查看本体结构</RouterLink>
    </div>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }} <button @click="loadWorkspace">重新加载</button></div>
    <div class="overview-layout">
      <section class="graph-panel">
        <header class="panel-heading"><div><h2>对象关系图</h2><p>当前结构中的业务对象与连接</p></div><span class="live-indicator">结构 v{{ ontology?.revision || 1 }}</span></header>
        <div v-if="loading" class="empty-state">正在读取本体结构…</div>
        <div v-else-if="objectTypes.length === 0" class="empty-state"><strong>本体结构还是空的</strong><span>提交一份对象类型提案，开始搭建你的业务图谱。</span><RouterLink to="/proposals">创建第一个提案</RouterLink></div>
        <div v-else class="relation-canvas">
          <svg class="relation-lines" viewBox="0 0 680 280" preserveAspectRatio="none" aria-hidden="true">
            <path v-for="(_, index) in linkTypes.slice(0, 5)" :key="index" :d="`M ${110 + (index % 3) * 205} ${70 + Math.floor(index / 3) * 130} C 225 ${20 + index * 22}, 430 ${245 - index * 16}, ${570 - (index % 2) * 185} ${70 + (index % 2) * 130}`" />
          </svg>
          <div v-for="(item, index) in graphNodes" :key="item.id" class="graph-node" :class="`graph-node-${index + 1}`">
            <span class="graph-node-icon">{{ item.display_name.slice(0, 1) }}</span><strong>{{ item.display_name }}</strong><code>{{ item.api_name }}</code><small>{{ item.properties.length }} 个属性</small>
          </div>
          <div v-if="linkTypes.length" class="relation-label">{{ linkTypes[0].display_name }}</div>
          <span v-else class="graph-hint">提案合并后，对象之间的链接会显示在这里</span>
        </div>
        <footer class="graph-footer"><span><i class="legend-dot object-dot" />对象类型</span><span><i class="legend-line" />本体链接</span><RouterLink to="/ontology">打开结构目录</RouterLink></footer>
      </section>
      <aside class="overview-rail">
        <section class="rail-section"><h2>结构摘要</h2><div class="summary-row"><span>对象类型</span><strong>{{ objectTypes.length }}</strong></div><div class="summary-row"><span>链接类型</span><strong>{{ linkTypes.length }}</strong></div><div class="summary-row"><span>对象记录</span><strong>{{ objectCount }}</strong></div><div class="summary-row"><span>当前版本</span><strong>v{{ ontology?.revision || 1 }}</strong></div></section>
        <section class="rail-section quick-actions"><h2>常用入口</h2><RouterLink to="/objects"><span>⌕</span>搜索业务对象</RouterLink><RouterLink to="/proposals"><span>＋</span>提交结构变更</RouterLink><RouterLink to="/agents"><span>◉</span>打开 Agent 会话</RouterLink></section>
        <section class="system-note"><span class="connection-dot" /><div><strong>系统运行正常</strong><small>本体 API 与 Agent 服务已连接</small></div></section>
      </aside>
    </div>
    <section class="recent-types"><div class="section-heading"><div><h2>对象类型目录</h2><p>从对象模型进入数据、关系与可执行操作。</p></div><RouterLink to="/ontology">查看全部</RouterLink></div>
      <div v-if="!loading && objectTypes.length" class="type-strip"><RouterLink v-for="item in objectTypes.slice(0, 4)" :key="item.id" :to="{ path: '/objects', query: { type: item.api_name } }" class="type-strip-item"><span class="type-glyph">{{ item.display_name.slice(0, 1) }}</span><span><strong>{{ item.display_name }}</strong><code>{{ item.api_name }}</code></span><small>{{ item.properties.length }} 属性</small></RouterLink></div>
      <div v-else-if="!loading" class="quiet-empty">尚未定义对象类型。</div>
    </section>
  </div>
</template>
