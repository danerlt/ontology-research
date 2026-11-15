<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { api, readableError } from "../api/client";
import type { ActionDefinition, ActionPreview, ObjectRecord, ObjectType, Ontology } from "../types";

const route = useRoute();
const ontologies = ref<Ontology[]>([]);
const types = ref<ObjectType[]>([]);
const selectedType = ref("");
const query = ref("");
const records = ref<ObjectRecord[]>([]);
const totalRecords = ref(0);
const page = ref(1);
const pageSize = ref(25);
const sortBy = ref("created_at");
const sortOrder = ref("desc");
const selectedRecord = ref<ObjectRecord | null>(null);
const actions = ref<ActionDefinition[]>([]);
const selectedAction = ref("");
const actionValues = ref<Record<string, string>>({});
const actionPreview = ref<ActionPreview | null>(null);
const previewRequestKey = ref("");
const loading = ref(false);
const error = ref("");
const notice = ref("");
const matchingActions = computed(() => actions.value.filter((item) => item.object_type_api_name === selectedRecord.value?.object_type_api_name && item.enabled));
const actionFields = computed(() => matchingActions.value.find((item) => item.api_name === selectedAction.value)?.parameters_schema ?? {});
const currentPreviewKey = computed(() => {
  if (!selectedRecord.value || !selectedAction.value) return "";
  return JSON.stringify({ object_id: selectedRecord.value.id, version: selectedRecord.value.version, action: selectedAction.value, values: actionValues.value });
});
const previewIsCurrent = computed(() => Boolean(actionPreview.value) && previewRequestKey.value === currentPreviewKey.value);
const pageCount = computed(() => Math.max(1, Math.ceil(totalRecords.value / pageSize.value)));

function recordTitle(record: ObjectRecord) {
  const objectType = types.value.find((item) => item.api_name === record.object_type_api_name);
  const titleKey = objectType?.title_key_property;
  const value = titleKey ? record.properties[titleKey] : undefined;
  return String(value ?? record.properties.name ?? record.primary_key_value);
}

function displayPropertyName(apiName: string) {
  const property = types.value.find((item) => item.api_name === selectedType.value)?.properties.find((item) => item.api_name === apiName);
  return property?.display_name ?? apiName;
}

async function loadInitial() {
  try {
    ontologies.value = await api.get<Ontology[]>("/api/ontology");
    const ontology = ontologies.value[0];
    if (!ontology) return;
    types.value = await api.get<ObjectType[]>("/api/object-types", { ontology_id: ontology.id });
    actions.value = await api.get<ActionDefinition[]>("/api/actions", { ontology_id: ontology.id });
    query.value = String(route.query.query || "");
    page.value = Math.max(1, Number.parseInt(String(route.query.page || "1"), 10) || 1);
    selectedType.value = String(route.query.type || types.value[0]?.api_name || "");
    await loadRecords();
    const requestedRecord = String(route.query.record || "");
    const selected = records.value.find((item) => item.id === requestedRecord);
    if (selected) await selectRecord(selected);
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
      page: page.value,
      page_size: pageSize.value,
      sort_by: sortBy.value,
      sort_order: sortOrder.value,
    });
    records.value = result.items;
    totalRecords.value = result.total;
    selectedRecord.value = null;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

function searchRecords() {
  page.value = 1;
  void loadRecords();
}

function changePage(nextPage: number) {
  if (nextPage < 1 || nextPage > pageCount.value) return;
  page.value = nextPage;
  void loadRecords();
}

function changeType() {
  page.value = 1;
  void loadRecords();
}

async function selectRecord(record: ObjectRecord) {
  error.value = "";
  try {
    selectedRecord.value = await api.get<ObjectRecord>(`/api/objects/${record.id}`);
    selectedAction.value = matchingActions.value[0]?.api_name ?? "";
    actionValues.value = {};
    actionPreview.value = null;
  } catch (cause) {
    error.value = readableError(cause);
  }
}

function typedValue(propertyName: string, value: string): unknown {
  const schema = actionFields.value[propertyName];
  const property = types.value.find((type) => type.api_name === selectedType.value)?.properties.find((item) => item.api_name === propertyName);
  const dataType = schema?.type ?? property?.data_type;
  if (dataType === "integer") return Number.parseInt(value, 10);
  if (dataType === "number") return Number(value);
  if (dataType === "boolean") return value === "true";
  if (dataType === "json" || dataType === "object" || dataType === "array") return JSON.parse(value);
  return value;
}

function buildParameters() {
  const parameters: Record<string, unknown> = {};
  Object.keys(actionFields.value).forEach((name) => {
    const value = actionValues.value[name];
    if (value !== undefined && value !== "") parameters[name] = typedValue(name, value);
  });
  return parameters;
}

async function previewAction() {
  if (!selectedRecord.value || !selectedAction.value) return;
  notice.value = "";
  error.value = "";
  try {
    const parameters = buildParameters();
    const preview = await api.post<ActionPreview>(`/api/actions/${selectedAction.value}/preview`, {
      object_id: selectedRecord.value.id,
      expected_version: selectedRecord.value.version,
      parameters,
    });
    actionPreview.value = preview;
    previewRequestKey.value = currentPreviewKey.value;
    notice.value = "影响预览已生成。请检查属性变化后确认执行；此时尚未写入对象。";
  } catch (cause) {
    actionPreview.value = null;
    error.value = readableError(cause);
  }
}

async function runAction() {
  if (!selectedRecord.value || !selectedAction.value || !previewIsCurrent.value) return;
  notice.value = "";
  error.value = "";
  try {
    const result = await api.post<ObjectRecord>(`/api/actions/${selectedAction.value}/execute`, {
      object_id: selectedRecord.value.id,
      expected_version: selectedRecord.value.version,
      parameters: buildParameters(),
    });
    selectedRecord.value = result;
    records.value = records.value.map((item) => (item.id === result.id ? result : item));
    actionPreview.value = null;
    notice.value = "Action 已执行，对象版本已更新。";
  } catch (cause) {
    error.value = readableError(cause);
  }
}

function propertyName(apiName: string) {
  const property = types.value.find((type) => type.api_name === selectedType.value)?.properties.find((item) => item.api_name === apiName);
  return property?.display_name ?? apiName;
}

onMounted(loadInitial);
</script>

<template>
  <div class="page-content">
    <div class="page-heading"><div><span class="eyebrow">ONTOLOGY · OBJECT EXPLORER</span><h1>对象数据</h1><p>搜索对象记录，检查属性与关系，并预览 Action 对数据的影响。</p></div><div class="heading-tools"><label class="object-type-picker">对象类型<select v-model="selectedType" class="select-control" @change="changeType"><option v-for="type in types" :key="type.id" :value="type.api_name">{{ type.display_name }}</option></select></label></div></div>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div><div v-if="notice" class="notice notice-success">{{ notice }}</div>
    <section class="object-browser">
      <div class="object-list-panel">
        <div class="browser-toolbar">
          <label class="search-field"><span>⌕</span><input v-model="query" aria-label="搜索对象属性" placeholder="搜索对象属性" @keyup.enter="searchRecords" /><button type="button" @click="searchRecords">搜索</button></label>
          <button class="icon-button" aria-label="重新加载" @click="loadRecords">↻</button>
        </div>
        <div class="object-list-controls"><div class="result-count"><strong>{{ totalRecords.toLocaleString("zh-CN") }}</strong> 条记录 <code>{{ selectedType }}</code></div><label>排序<select v-model="sortBy" aria-label="对象排序方式" @change="searchRecords"><option value="created_at">最近更新</option><option value="primary_key">主键</option><option value="version">版本</option></select></label><button class="sort-direction" aria-label="切换排序方向" @click="sortOrder = sortOrder === 'asc' ? 'desc' : 'asc'; searchRecords()">{{ sortOrder === "asc" ? "升序 ↑" : "降序 ↓" }}</button></div>
        <div v-if="loading" class="empty-state compact">正在查询…</div>
        <button v-for="record in records" :key="record.id" class="object-result" :class="{ selected: selectedRecord?.id === record.id }" @click="selectRecord(record)"><span class="result-glyph" :style="{ backgroundColor: types.find((item) => item.api_name === record.object_type_api_name)?.icon_color || undefined }">{{ types.find((item) => item.api_name === record.object_type_api_name)?.icon || record.object_type_display_name.slice(0, 1) }}</span><span><strong>{{ recordTitle(record) }}</strong><code>{{ record.primary_key_value }}</code></span><small>v{{ record.version }}</small></button>
        <div v-if="!loading && records.length === 0" class="empty-state compact"><strong>没有匹配的对象</strong><span>修改搜索词，或创建首条对象记录。</span></div>
        <footer class="object-pagination"><span>第 {{ page }} / {{ pageCount }} 页</span><button class="button button-quiet" data-action="previous-object-page" :disabled="page <= 1 || loading" @click="changePage(page - 1)">上一页</button><button class="button button-quiet" data-action="next-object-page" :disabled="page >= pageCount || loading" @click="changePage(page + 1)">下一页</button></footer>
      </div>
      <div class="object-detail-panel"><template v-if="selectedRecord"><header class="object-detail-header"><div><span class="eyebrow">{{ selectedRecord.object_type_display_name }} / 对象记录</span><h2>{{ recordTitle(selectedRecord) }}</h2><p><code>{{ selectedRecord.primary_key_value }}</code><span>版本 {{ selectedRecord.version }}</span></p></div><span class="api-tag">{{ selectedRecord.object_type_api_name }}</span></header><section class="detail-section"><h3>属性</h3><dl class="property-grid"><template v-for="(value, key) in selectedRecord.properties" :key="key"><dt>{{ displayPropertyName(String(key)) }}</dt><dd>{{ typeof value === "object" ? JSON.stringify(value) : String(value ?? "—") }}</dd></template></dl></section><section class="detail-section"><div class="section-heading"><div><h3>对象关系</h3><p>此对象已连接的本体记录</p></div></div><div v-if="selectedRecord.links.length" class="detail-links"><div v-for="link in selectedRecord.links" :key="String(link.link_id)" class="detail-link"><span class="relation-symbol">⇄</span><strong>{{ link.link_type_display_name }}</strong><span>{{ link.linked_object_type_display_name }} · {{ link.linked_primary_key }}</span></div></div><p v-else class="quiet-empty">当前对象还没有关系。</p></section><section class="detail-section action-section"><div class="section-heading"><div><h3>可执行 Action</h3><p>先预览受影响属性，再确认写入；服务端会再次校验角色、规则与对象版本。</p></div></div><div v-if="matchingActions.length" class="action-form"><select v-model="selectedAction" class="select-control" aria-label="选择 Action" @change="actionPreview = null"><option v-for="action in matchingActions" :key="action.id" :value="action.api_name">{{ action.display_name }} · {{ action.api_name }}</option></select><label v-for="(definition, name) in actionFields" :key="name">{{ propertyName(name) }}<select v-if="definition.enum" v-model="actionValues[name]" :aria-label="propertyName(name)" :required="definition.required"><option value="">{{ definition.required ? "请选择必填值" : "不修改此属性" }}</option><option v-for="choice in definition.enum" :key="String(choice)" :value="String(choice)">{{ choice }}</option></select><select v-else-if="definition.type === 'boolean'" v-model="actionValues[name]" :aria-label="propertyName(name)" :required="definition.required"><option value="">{{ definition.required ? "请选择必填值" : "不修改此属性" }}</option><option value="true">是</option><option value="false">否</option></select><textarea v-else-if="['object', 'array', 'json'].includes(definition.type || '')" v-model="actionValues[name]" :aria-label="propertyName(name)" :placeholder="definition.required ? '输入 JSON（必填）' : '输入 JSON（可选）'" @input="actionPreview = null" /><input v-else v-model="actionValues[name]" :type="definition.type === 'integer' || definition.type === 'number' ? 'number' : 'text'" :step="definition.type === 'integer' ? '1' : 'any'" :min="definition.minimum" :max="definition.maximum" :minlength="definition.min_length" :maxlength="definition.max_length" :pattern="definition.pattern" :aria-label="propertyName(name)" :placeholder="definition.required ? '必填参数' : '可选参数'" :required="definition.required" @input="actionPreview = null" /></label><button class="button button-secondary" aria-label="预览 Action" @click="previewAction">生成影响预览</button><div v-if="actionPreview && previewIsCurrent" class="action-preview-card" aria-live="polite"><div class="section-heading"><div><h4>变更预览</h4><p>对象版本 v{{ actionPreview.current_version }} → v{{ actionPreview.next_version }}</p></div><span class="status-chip status-active">等待确认</span></div><table class="preview-diff-table"><thead><tr><th>属性</th><th>当前值</th><th>执行后</th></tr></thead><tbody><tr v-for="change in actionPreview.property_changes" :key="change.property"><td>{{ propertyName(change.property) }}</td><td>{{ change.before }}</td><td>{{ change.after }}</td></tr></tbody></table><button class="button button-primary" aria-label="确认执行 Action" @click="runAction">确认并执行</button></div></div><p v-else class="quiet-empty">该类型暂无可用 Action。</p></section></template><div v-else class="empty-detail"><span class="empty-orbit">◇</span><h2>选择一个对象</h2><p>对象属性、链接和可执行 Action 会显示在这里。</p></div></div>
    </section>
  </div>
</template>
