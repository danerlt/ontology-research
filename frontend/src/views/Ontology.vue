<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { api, readableError } from "../api/client";
import type { LinkType, ObjectType, Ontology as OntologyRecord } from "../types";

const ontologies = ref<OntologyRecord[]>([]);
const selectedOntology = ref("");
const objectTypes = ref<ObjectType[]>([]);
const linkTypes = ref<LinkType[]>([]);
const selectedTypeId = ref("");
const error = ref("");
const loading = ref(false);
const selectedType = computed(() => objectTypes.value.find((item) => item.id === selectedTypeId.value) ?? objectTypes.value[0] ?? null);

async function loadStructure() {
  loading.value = true;
  error.value = "";
  try {
    ontologies.value = await api.get<OntologyRecord[]>("/api/ontology");
    selectedOntology.value ||= ontologies.value[0]?.id ?? "";
    if (!selectedOntology.value) return;
    const [types, links] = await Promise.all([
      api.get<ObjectType[]>("/api/object-types", { ontology_id: selectedOntology.value }),
      api.get<LinkType[]>("/api/link-types", { ontology_id: selectedOntology.value }),
    ]);
    objectTypes.value = types;
    linkTypes.value = links;
    selectedTypeId.value ||= types[0]?.id ?? "";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

onMounted(loadStructure);
</script>

<template>
  <div class="page-content">
    <div class="page-heading"><div><span class="eyebrow">结构目录</span><h1>本体结构</h1><p>定义业务世界里的对象、属性和对象间关系。</p></div><select v-model="selectedOntology" class="select-control" @change="loadStructure"><option v-for="ontology in ontologies" :key="ontology.id" :value="ontology.id">{{ ontology.display_name }} · v{{ ontology.revision }}</option></select></div>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }} <button @click="loadStructure">重新加载</button></div>
    <div class="structure-layout">
      <aside class="structure-index"><div class="index-heading"><span>对象类型</span><b>{{ objectTypes.length }}</b></div><button v-for="item in objectTypes" :key="item.id" class="type-index-button" :class="{ selected: selectedType?.id === item.id }" @click="selectedTypeId = item.id"><span class="type-glyph">{{ item.display_name.slice(0, 1) }}</span><span><strong>{{ item.display_name }}</strong><code>{{ item.api_name }}</code></span><small>{{ item.properties.length }}</small></button><div v-if="!loading && !objectTypes.length" class="quiet-empty">暂无对象类型</div><div class="index-heading link-index-heading"><span>链接类型</span><b>{{ linkTypes.length }}</b></div><div v-for="link in linkTypes" :key="link.id" class="link-index-item"><span class="link-symbol">↗</span><span><strong>{{ link.display_name }}</strong><code>{{ link.api_name }}</code></span></div></aside>
      <section class="structure-detail">
        <div v-if="loading" class="empty-state">正在读取结构…</div>
        <div v-else-if="selectedType" class="detail-pane"><div class="detail-title"><div><span class="eyebrow">对象类型</span><h2>{{ selectedType.display_name }}</h2><p>{{ selectedType.description || "尚未添加类型说明。" }}</p></div><span class="api-tag">{{ selectedType.api_name }}</span></div><div class="detail-meta"><span>主键属性 <strong>{{ selectedType.primary_key_property }}</strong></span><span>属性数 <strong>{{ selectedType.properties.length }}</strong></span></div><div class="table-wrap"><table><thead><tr><th>显示名称</th><th>API 名称</th><th>类型</th><th>约束</th></tr></thead><tbody><tr v-for="property in selectedType.properties" :key="property.id"><td>{{ property.display_name }}</td><td><code>{{ property.api_name }}</code></td><td><span class="type-badge">{{ property.data_type }}</span></td><td><span v-if="property.required" class="constraint-chip">必填</span><span v-if="property.unique_value" class="constraint-chip">唯一</span><span v-if="property.sensitive" class="constraint-chip sensitive-chip">敏感</span><span v-if="!property.editable" class="constraint-chip">只读</span><span v-if="!property.required && !property.unique_value && !property.sensitive && property.editable" class="muted">—</span></td></tr></tbody></table></div><div class="relation-section"><div class="section-heading"><div><h3>此类型上的关系</h3><p>关系方向由链接类型明确规定。</p></div></div><div v-if="linkTypes.length" class="relation-list"><div v-for="link in linkTypes" :key="link.id" class="relation-row"><span class="relation-symbol">⇄</span><strong>{{ link.display_name }}</strong><code>{{ link.api_name }}</code><span>方向由结构定义</span></div></div><p v-else class="quiet-empty">还没有已定义的链接类型。</p></div></div>
        <div v-else class="empty-state"><strong>选择本体开始浏览</strong><span>当前工作区没有对象类型。</span></div>
      </section>
    </div>
  </div>
</template>
