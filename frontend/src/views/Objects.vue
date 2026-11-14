<script setup lang="ts">
import { computed, onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";
import { api, readableError } from "../api/client";
import type { ActionDefinition, ObjectRecord, ObjectType, Ontology } from "../types";

const route = useRoute();
const ontologies = ref<Ontology[]>([]);
const types = ref<ObjectType[]>([]);
const selectedType = ref("");
const query = ref("");
const records = ref<ObjectRecord[]>([]);
const selectedRecord = ref<ObjectRecord | null>(null);
const actions = ref<ActionDefinition[]>([]);
const selectedAction = ref("");
const actionValues = ref<Record<string, string>>({});
const loading = ref(false);
const error = ref("");
const notice = ref("");
const matchingActions = computed(() => actions.value.filter((item) => item.object_type_api_name === selectedRecord.value?.object_type_api_name && item.enabled));
const actionFields = computed(() => matchingActions.value.find((item) => item.api_name === selectedAction.value)?.parameters_schema ?? {});

async function loadInitial() {
  try {
    ontologies.value = await api.get<Ontology[]>("/api/ontology");
    const ontology = ontologies.value[0];
    if (!ontology) return;
    types.value = await api.get<ObjectType[]>("/api/object-types", { ontology_id: ontology.id });
    actions.value = await api.get<ActionDefinition[]>("/api/actions", { ontology_id: ontology.id });
    selectedType.value = String(route.query.type || types.value[0]?.api_name || "");
    await loadRecords();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function loadRecords() {
  if (!selectedType.value) {
    records.value = [];
    return;
  }
  loading.value = true;
  error.value = "";
  try {
    const result = await api.get<{ items: ObjectRecord[]; total: number }>("/api/objects", {
      ontology_id: ontologies.value[0]?.id,
      object_type_api_name: selectedType.value,
      query: query.value,
      page: 1,
      page_size: 50,
    });
    records.value = result.items;
    selectedRecord.value = null;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function selectRecord(record: ObjectRecord) {
  error.value = "";
  try {
    selectedRecord.value = await api.get<ObjectRecord>(`/api/objects/${record.id}`);
    selectedAction.value = matchingActions.value[0]?.api_name ?? "";
    actionValues.value = {};
  } catch (cause) {
    error.value = readableError(cause);
  }
}

function typedValue(propertyName: string, value: string): unknown {
  const property = types.value.find((type) => type.api_name === selectedType.value)?.properties.find((item) => item.api_name === propertyName);
  if (property?.data_type === "integer") return Number.parseInt(value, 10);
  if (property?.data_type === "number") return Number(value);
  if (property?.data_type === "boolean") return value === "true";
  if (property?.data_type === "json") return JSON.parse(value);
  return value;
}

async function runAction() {
  if (!selectedRecord.value || !selectedAction.value) return;
  notice.value = "";
  error.value = "";
  const parameters: Record<string, unknown> = {};
  try {
    Object.keys(actionFields.value).forEach((name) => {
      if (actionValues.value[name] !== undefined && actionValues.value[name] !== "") {
        parameters[name] = typedValue(name, actionValues.value[name]);
      }
    });
    const result = await api.post<ObjectRecord>(`/api/actions/${selectedAction.value}/execute`, {
      object_id: selectedRecord.value.id,
      expected_version: selectedRecord.value.version,
      parameters,
    });
    selectedRecord.value = result;
    records.value = records.value.map((item) => (item.id === result.id ? result : item));
    notice.value = "Action 已执行，对象版本已更新。";
  } catch (cause) {
    error.value = readableError(cause);
  }
}

watch(selectedType, loadRecords);
onMounted(loadInitial);
</script>

<template>
  <div class="page-content">
    <div class="page-heading"><div><span class="eyebrow">数据浏览器</span><h1>对象数据</h1><p>搜索对象记录，查看关联关系并执行本体 Action。</p></div><div class="heading-tools"><select v-model="selectedType" class="select-control"><option v-for="type in types" :key="type.id" :value="type.api_name">{{ type.display_name }}</option></select></div></div>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div><div v-if="notice" class="notice notice-success">{{ notice }}</div>
    <section class="object-browser">
      <div class="object-list-panel"><div class="browser-toolbar"><label class="search-field"><span>⌕</span><input v-model="query" placeholder="搜索对象属性" @keyup.enter="loadRecords" /><button @click="loadRecords">搜索</button></label><button class="icon-button" aria-label="重新加载" @click="loadRecords">↻</button></div><div class="result-count">{{ selectedType }} <span>{{ records.length }} 条结果</span></div><div v-if="loading" class="empty-state compact">正在查询…</div><button v-for="record in records" :key="record.id" class="object-result" :class="{ selected: selectedRecord?.id === record.id }" @click="selectRecord(record)"><span class="result-glyph">{{ record.object_type_display_name.slice(0, 1) }}</span><span><strong>{{ String(record.properties.name || record.primary_key_value) }}</strong><code>{{ record.primary_key_value }}</code></span><small>v{{ record.version }}</small></button><div v-if="!loading && records.length === 0" class="empty-state compact"><strong>没有匹配的对象</strong><span>修改搜索词，或创建首条对象记录。</span></div></div>
      <div class="object-detail-panel"><template v-if="selectedRecord"><header class="object-detail-header"><div><span class="eyebrow">{{ selectedRecord.object_type_display_name }} / 对象记录</span><h2>{{ String(selectedRecord.properties.name || selectedRecord.primary_key_value) }}</h2><p><code>{{ selectedRecord.primary_key_value }}</code><span>版本 {{ selectedRecord.version }}</span></p></div><span class="api-tag">{{ selectedRecord.object_type_api_name }}</span></header><section class="detail-section"><h3>属性</h3><dl class="property-grid"><template v-for="(value, key) in selectedRecord.properties" :key="key"><dt>{{ key }}</dt><dd>{{ typeof value === "object" ? JSON.stringify(value) : String(value ?? "—") }}</dd></template></dl></section><section class="detail-section"><div class="section-heading"><div><h3>对象关系</h3><p>此对象已连接的本体记录</p></div></div><div v-if="selectedRecord.links.length" class="detail-links"><div v-for="link in selectedRecord.links" :key="String(link.link_id)" class="detail-link"><span class="relation-symbol">⇄</span><strong>{{ link.link_type_display_name }}</strong><span>{{ link.linked_object_type_display_name }} · {{ link.linked_primary_key }}</span></div></div><p v-else class="quiet-empty">当前对象还没有关系。</p></section><section class="detail-section action-section"><div class="section-heading"><div><h3>可执行 Action</h3><p>服务端将再次校验角色、参数和对象版本。</p></div></div><div v-if="matchingActions.length" class="action-form"><select v-model="selectedAction" class="select-control"><option v-for="action in matchingActions" :key="action.id" :value="action.api_name">{{ action.display_name }} · {{ action.api_name }}</option></select><label v-for="(definition, name) in actionFields" :key="name">{{ name }}<input v-model="actionValues[name]" :placeholder="definition.required ? '必填参数' : '可选参数'" /></label><button class="button button-primary" @click="runAction">执行 Action</button></div><p v-else class="quiet-empty">该类型暂无可用 Action。</p></section></template><div v-else class="empty-detail"><span class="empty-orbit">◇</span><h2>选择一个对象</h2><p>对象属性、链接和可执行 Action 会显示在这里。</p></div></div>
    </section>
  </div>
</template>
