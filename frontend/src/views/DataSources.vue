<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { api, readableError } from "../api/client";
import type { ObjectType, Ontology } from "../types";

interface DataSourceConnection {
  id: string;
  ontology_id: string;
  name: string;
  description: string;
  connector_type: string;
  status: string;
  mapping_count: number;
  last_run_status: string | null;
  last_run_at: string | null;
  created_at: string;
}
interface DataMapping {
  id: string;
  connection_id: string;
  object_type_api_name: string;
  object_type_display_name: string;
  primary_key_field: string;
  field_mappings: Record<string, string>;
  updated_at: string;
}
interface ImportRun {
  id: string;
  status: "completed" | "failed";
  rows_total: number;
  rows_imported: number;
  errors: Array<{ row: number; field: string; message: string }>;
  created_at: string;
  completed_at: string | null;
}
interface PreviewResult {
  valid: boolean;
  rows_total: number;
  items: Array<{ row: number; primary_key_value: string; properties: Record<string, unknown> }>;
  errors: Array<{ row: number; field: string; message: string }>;
}

const ontologies = ref<Ontology[]>([]);
const objectTypes = ref<ObjectType[]>([]);
const connections = ref<DataSourceConnection[]>([]);
const mappings = ref<DataMapping[]>([]);
const runs = ref<ImportRun[]>([]);
const selectedOntologyId = ref("");
const selectedConnectionId = ref("");
const selectedMappingId = ref("");
const mappingTypeApiName = ref("");
const primaryKeyField = ref("");
const fieldMappings = ref<Record<string, string>>({});
const rows = ref<Record<string, unknown>[]>([]);
const sourceColumns = ref<string[]>([]);
const sourceFileName = ref("");
const preview = ref<PreviewResult | null>(null);
const createForm = ref({ name: "", description: "" });
const loading = ref(false);
const busy = ref(false);
const error = ref("");
const notice = ref("");

const selectedOntology = computed(() => ontologies.value.find((item) => item.id === selectedOntologyId.value) ?? null);
const selectedConnection = computed(() => connections.value.find((item) => item.id === selectedConnectionId.value) ?? null);
const selectedType = computed(() => objectTypes.value.find((item) => item.api_name === mappingTypeApiName.value) ?? null);
const selectedMapping = computed(() => mappings.value.find((item) => item.id === selectedMappingId.value) ?? null);
const canSaveMapping = computed(() => Boolean(
  selectedConnection.value
  && selectedType.value
  && sourceColumns.value.length
  && primaryKeyField.value
  && fieldMappings.value[primaryKeyField.value] === selectedType.value.primary_key_property,
));

async function loadWorkspace() {
  loading.value = true;
  error.value = "";
  try {
    ontologies.value = await api.get<Ontology[]>("/api/ontology");
    if (!selectedOntologyId.value || !ontologies.value.some((item) => item.id === selectedOntologyId.value)) {
      selectedOntologyId.value = ontologies.value[0]?.id ?? "";
    }
    if (!selectedOntologyId.value) return;
    const [types, sourceList] = await Promise.all([
      api.get<ObjectType[]>("/api/object-types", { ontology_id: selectedOntologyId.value }),
      api.get<DataSourceConnection[]>("/api/data-sources", { ontology_id: selectedOntologyId.value }),
    ]);
    objectTypes.value = types;
    connections.value = sourceList;
    if (!connections.value.some((item) => item.id === selectedConnectionId.value)) {
      selectedConnectionId.value = connections.value[0]?.id ?? "";
    }
    await loadConnectionDetails();
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function changeOntology() {
  selectedConnectionId.value = "";
  await loadWorkspace();
}

async function loadConnectionDetails() {
  const connectionId = selectedConnectionId.value;
  if (!connectionId) {
    mappings.value = [];
    runs.value = [];
    selectedMappingId.value = "";
    resetImportedFile();
    return;
  }
  const [sourceMappings, sourceRuns] = await Promise.all([
    api.get<DataMapping[]>(`/api/data-sources/${connectionId}/mappings`),
    api.get<ImportRun[]>(`/api/data-sources/${connectionId}/runs`),
  ]);
  mappings.value = sourceMappings;
  runs.value = sourceRuns;
  if (!sourceMappings.some((item) => item.id === selectedMappingId.value)) {
    selectedMappingId.value = sourceMappings[0]?.id ?? "";
  }
  if (selectedMapping.value) {
    mappingTypeApiName.value = selectedMapping.value.object_type_api_name;
    fieldMappings.value = { ...selectedMapping.value.field_mappings };
    primaryKeyField.value = selectedMapping.value.primary_key_field;
  } else {
    mappingTypeApiName.value = objectTypes.value[0]?.api_name ?? "";
    fieldMappings.value = {};
    primaryKeyField.value = "";
  }
}

async function selectConnection(connectionId: string) {
  selectedConnectionId.value = connectionId;
  selectedMappingId.value = "";
  error.value = "";
  notice.value = "";
  resetImportedFile();
  try {
    await loadConnectionDetails();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

async function createConnection() {
  if (!selectedOntologyId.value || !createForm.value.name.trim()) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const connection = await api.post<DataSourceConnection>("/api/data-sources", {
      ontology_id: selectedOntologyId.value,
      name: createForm.value.name.trim(),
      description: createForm.value.description.trim(),
      connector_type: "local_file",
    });
    connections.value.unshift(connection);
    createForm.value = { name: "", description: "" };
    await selectConnection(connection.id);
    notice.value = "本地文件数据源已创建。下一步选择 CSV 或 JSON 文件，配置列映射并运行预览。";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

function parseCsv(text: string): Record<string, string>[] {
  const records: string[][] = [];
  let record: string[] = [];
  let cell = "";
  let quoted = false;
  for (let index = 0; index < text.length; index += 1) {
    const character = text[index];
    if (quoted) {
      if (character === '"' && text[index + 1] === '"') {
        cell += '"';
        index += 1;
      } else if (character === '"') {
        quoted = false;
      } else {
        cell += character;
      }
      continue;
    }
    if (character === '"' && cell.length === 0) quoted = true;
    else if (character === ",") {
      record.push(cell);
      cell = "";
    } else if (character === "\n" || character === "\r") {
      record.push(cell);
      if (record.some((value) => value.length)) records.push(record);
      record = [];
      cell = "";
      if (character === "\r" && text[index + 1] === "\n") index += 1;
    } else cell += character;
  }
  if (quoted) throw new Error("CSV 中存在未闭合的引号");
  record.push(cell);
  if (record.some((value) => value.length)) records.push(record);
  if (records.length < 2) throw new Error("文件需要包含列标题和至少一行数据");
  const headers = records[0].map((value) => value.trim());
  if (headers.some((value) => !value)) throw new Error("CSV 列标题不能为空");
  if (new Set(headers).size !== headers.length) throw new Error("CSV 中存在重复列标题");
  return records.slice(1).map((values, index) => {
    if (values.length !== headers.length) throw new Error(`第 ${index + 2} 行列数与标题不一致`);
    return Object.fromEntries(headers.map((header, cellIndex) => [header, values[cellIndex]]));
  });
}

function initializeColumnMapping() {
  const type = selectedType.value;
  const saved = selectedMapping.value?.object_type_api_name === type?.api_name ? selectedMapping.value : null;
  fieldMappings.value = Object.fromEntries(sourceColumns.value.map((column) => {
    const savedTarget = saved?.field_mappings[column];
    const suggestedTarget = type?.properties.some((property) => property.api_name === column) ? column : "";
    return [column, savedTarget ?? suggestedTarget];
  }));
  primaryKeyField.value = saved?.primary_key_field && sourceColumns.value.includes(saved.primary_key_field)
    ? saved.primary_key_field
    : sourceColumns.value.find((column) => fieldMappings.value[column] === type?.primary_key_property) ?? "";
  preview.value = null;
}

function selectObjectType() {
  initializeColumnMapping();
}

async function loadFile(event: Event) {
  const input = event.target as HTMLInputElement;
  const file = input.files?.[0];
  if (!file) return;
  error.value = "";
  notice.value = "";
  preview.value = null;
  try {
    const content = await file.text();
    if (file.name.toLowerCase().endsWith(".json")) {
      const parsed: unknown = JSON.parse(content);
      const data = Array.isArray(parsed) ? parsed : (parsed as { rows?: unknown } | null)?.rows;
      if (!Array.isArray(data) || !data.length || data.some((item) => !item || Array.isArray(item) || typeof item !== "object")) {
        throw new Error("JSON 文件必须是对象数组，或包含 rows 对象数组");
      }
      rows.value = data as Record<string, unknown>[];
    } else if (file.name.toLowerCase().endsWith(".csv")) {
      rows.value = parseCsv(content);
    } else {
      throw new Error("仅支持 CSV 与 JSON 文件");
    }
    sourceFileName.value = file.name;
    sourceColumns.value = Object.keys(rows.value[0]);
    if (!sourceColumns.value.length) throw new Error("文件没有可映射的列");
    initializeColumnMapping();
    notice.value = `已读取 ${rows.value.length} 行；请核对每个来源列的目标属性。`;
  } catch (cause) {
    resetImportedFile();
    error.value = readableError(cause);
  }
}

function resetImportedFile() {
  rows.value = [];
  sourceColumns.value = [];
  sourceFileName.value = "";
  preview.value = null;
}

async function saveMapping() {
  if (!selectedConnection.value || !selectedType.value || !canSaveMapping.value) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const mapping = await api.put<DataMapping>(`/api/data-sources/${selectedConnection.value.id}/mappings`, {
      object_type_api_name: selectedType.value.api_name,
      primary_key_field: primaryKeyField.value,
      field_mappings: Object.fromEntries(Object.entries(fieldMappings.value).filter(([, target]) => target)),
    });
    const current = mappings.value.findIndex((item) => item.id === mapping.id);
    if (current === -1) mappings.value.unshift(mapping);
    else mappings.value.splice(current, 1, mapping);
    selectedMappingId.value = mapping.id;
    notice.value = "列映射已保存。下一步生成服务端预览，检查主键、必填属性和数据类型。";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

async function previewImport() {
  if (!selectedConnection.value || !selectedMapping.value || !rows.value.length) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    preview.value = await api.post<PreviewResult>(
      `/api/data-sources/${selectedConnection.value.id}/mappings/${selectedMapping.value.id}/preview`,
      { rows: rows.value },
    );
    notice.value = preview.value.valid ? "服务端校验通过；预览尚未写入对象。" : "预览发现数据问题，修正文件或映射后重新检查。";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

async function importRows() {
  if (!selectedConnection.value || !selectedMapping.value || !preview.value?.valid) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    await api.post<ImportRun>(
      `/api/data-sources/${selectedConnection.value.id}/mappings/${selectedMapping.value.id}/import`,
      { rows: rows.value },
    );
    runs.value = await api.get<ImportRun[]>(`/api/data-sources/${selectedConnection.value.id}/runs`);
    notice.value = `导入完成：${preview.value.rows_total} 行对象已写入本体。`;
    preview.value = null;
    const refreshed = await api.get<DataSourceConnection[]>("/api/data-sources", { ontology_id: selectedOntologyId.value });
    connections.value = refreshed;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

function statusLabel(status: string | null) {
  if (status === "completed") return "完成";
  if (status === "failed") return "失败";
  if (status === "running") return "运行中";
  return "尚未运行";
}

function formatTime(value: string | null) {
  return value ? new Date(value).toLocaleString("zh-CN") : "—";
}

onMounted(loadWorkspace);
</script>

<template>
  <div class="page-content ontology-manager-page">
    <div class="page-heading manager-heading">
      <div><span class="eyebrow">ONTOLOGY · DATA SOURCES</span><h1>数据源与映射</h1><p>把本地 CSV/JSON 列映射到本体属性，先预览校验，再原子写入对象。</p></div>
      <label class="ontology-select-label">本体<select v-model="selectedOntologyId" class="select-control" @change="changeOntology"><option v-for="ontology in ontologies" :key="ontology.id" :value="ontology.id">{{ ontology.display_name }} · v{{ ontology.revision }}</option></select></label>
    </div>

    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div>
    <div v-if="notice" class="notice notice-success" role="status" aria-live="polite">{{ notice }}</div>

    <div class="data-source-workbench">
      <aside class="data-source-index panel">
        <div class="panel-title-row"><div><span class="eyebrow">连接目录</span><h2>{{ connections.length }} 个数据源</h2></div><span class="revision-pill">{{ selectedOntology?.api_name ?? "—" }}</span></div>
        <form class="data-source-create-form" @submit.prevent="createConnection">
          <label>新增本地文件连接<input v-model="createForm.name" aria-label="数据源名称" required minlength="2" placeholder="例如 customer-weekly" /></label>
          <input v-model="createForm.description" aria-label="数据源说明" placeholder="数据用途或文件周期" />
          <button class="button button-primary" :disabled="busy || !selectedOntologyId">创建连接</button>
        </form>
        <div class="data-source-list" aria-label="数据源列表">
          <button v-for="connection in connections" :key="connection.id" class="data-source-list-item" :class="{ selected: selectedConnectionId === connection.id }" @click="selectConnection(connection.id)">
            <span class="source-glyph">⇢</span><span class="data-source-copy"><strong>{{ connection.name }}</strong><small>{{ connection.mapping_count }} 个映射 · {{ statusLabel(connection.last_run_status) }}</small></span>
            <span class="source-state-dot" :class="connection.status === 'ready' ? 'ready' : 'failed'" />
          </button>
          <p v-if="loading" class="quiet-empty">正在读取连接…</p>
          <p v-else-if="!connections.length" class="quiet-empty">还没有数据源连接。创建本地文件连接后，可把数据列映射到本体属性。</p>
        </div>
      </aside>

      <section v-if="selectedConnection" class="data-source-detail panel">
        <header class="data-source-detail-header">
          <div><div class="resource-title-line"><span class="resource-kind-tag">{{ selectedConnection.connector_type === "local_file" ? "LOCAL FILE" : selectedConnection.connector_type }}</span><span class="status-chip status-active">{{ selectedConnection.status === "ready" ? "就绪" : selectedConnection.status }}</span></div><h2>{{ selectedConnection.name }}</h2><p>{{ selectedConnection.description || "未填写连接说明" }}</p></div>
          <div class="data-source-stats"><span>对象映射<strong>{{ mappings.length }}</strong></span><span>最近同步<strong>{{ statusLabel(selectedConnection.last_run_status) }}</strong></span></div>
        </header>
        <div class="connector-boundary"><strong>本地文件连接器</strong><span>此实现读取你在本页选择的 CSV/JSON 文件，不会连接 Palantir Foundry 或外部平台数据源。</span></div>

        <section class="data-source-section">
          <div class="section-heading"><div><h3>列到属性映射</h3><p>选择对象类型，为文件列指定本体属性并标记主键。</p></div><select v-model="mappingTypeApiName" class="select-control" aria-label="映射对象类型" @change="selectObjectType"><option v-for="type in objectTypes" :key="type.id" :value="type.api_name">{{ type.display_name }} · {{ type.api_name }}</option></select></div>
          <label class="file-drop-label">选择 CSV 或 JSON 文件<input type="file" accept=".csv,.json,text/csv,application/json" @change="loadFile" /></label>
          <p v-if="sourceFileName" class="file-loaded-line"><strong>{{ sourceFileName }}</strong><span>{{ rows.length }} 行 · {{ sourceColumns.length }} 列</span></p>
          <div v-if="sourceColumns.length && selectedType" class="table-wrap mapping-table-wrap">
            <table><thead><tr><th>来源列</th><th>示例值</th><th>映射到本体属性</th><th>主键</th></tr></thead><tbody>
              <tr v-for="column in sourceColumns" :key="column"><td><code>{{ column }}</code></td><td>{{ String(rows[0][column] ?? "—") }}</td><td><select v-model="fieldMappings[column]" class="mapping-target-select" :aria-label="`映射列 ${column}`"><option value="">不映射</option><option v-for="property in selectedType.properties" :key="property.id" :value="property.api_name">{{ property.display_name }} · {{ property.api_name }}</option></select></td><td><input v-model="primaryKeyField" type="radio" :value="column" :aria-label="`主键列 ${column}`" :disabled="fieldMappings[column] !== selectedType.primary_key_property" /></td></tr>
            </tbody></table>
          </div>
          <div v-else-if="!sourceColumns.length" class="mapping-empty"><strong>载入文件以配置映射</strong><span>文件列会和本体属性并排显示；匹配 API 名的列会自动建议映射。</span></div>
          <div class="mapping-actions"><label>主键来源列<select v-model="primaryKeyField" class="select-control" aria-label="主键来源列" :disabled="!sourceColumns.length"><option value="" disabled>选择映射到 {{ selectedType?.primary_key_property ?? "主键" }} 的列</option><option v-for="column in sourceColumns" :key="column" :value="column" :disabled="fieldMappings[column] !== selectedType?.primary_key_property">{{ column }}</option></select></label><button class="button button-secondary" :disabled="busy || !canSaveMapping" @click="saveMapping">保存映射</button></div>
          <div v-if="mappings.length" class="saved-mappings"><span class="eyebrow">已保存映射</span><div v-for="mapping in mappings" :key="mapping.id" class="saved-mapping-row"><button class="saved-mapping-select" :class="{ selected: selectedMappingId === mapping.id }" @click="selectedMappingId = mapping.id; mappingTypeApiName = mapping.object_type_api_name; fieldMappings = { ...mapping.field_mappings }; primaryKeyField = mapping.primary_key_field"><strong>{{ mapping.object_type_display_name }}</strong><small>{{ mapping.primary_key_field }} 为主键</small></button><span class="mapping-arrow-list">{{ Object.entries(mapping.field_mappings).map(([source, target]) => `${source} → ${target}`).join(" · ") }}</span></div></div>
        </section>

        <section class="data-source-section import-section">
          <div class="section-heading"><div><h3>预览与导入</h3><p>预览只运行校验，不写入对象；正式导入逐行写入并记录同步任务。</p></div><div class="mapping-actions"><button class="button button-secondary" :disabled="busy || !selectedMapping || !rows.length" @click="previewImport">运行预览</button><button class="button button-primary" :disabled="busy || !preview?.valid" @click="importRows">确认导入</button></div></div>
          <p v-if="preview" class="preview-summary" :class="preview.valid ? 'preview-valid' : 'preview-invalid'">{{ preview.valid ? `校验通过 · ${preview.rows_total} 行 · 未写入数据` : `发现 ${preview.errors.length} 个问题 · 未写入数据` }}</p>
          <div v-if="preview?.items.length" class="table-wrap preview-table-wrap"><table><thead><tr><th>行</th><th>对象主键</th><th>映射后属性</th></tr></thead><tbody><tr v-for="item in preview.items" :key="item.row"><td>{{ item.row }}</td><td><code>{{ item.primary_key_value }}</code></td><td>{{ Object.entries(item.properties).map(([key, value]) => `${key}: ${String(value)}`).join(" · ") }}</td></tr></tbody></table><p v-if="preview.rows_total > preview.items.length" class="quiet-empty">仅显示前 {{ preview.items.length }} 行预览。</p></div>
          <div v-if="preview?.errors.length" class="validation-list" aria-label="数据校验错误"><div v-for="issue in preview.errors" :key="`${issue.row}-${issue.field}-${issue.message}`" class="validation-issue validation-error"><strong>第 {{ issue.row }} 行</strong><code>{{ issue.field }}</code><span>{{ issue.message }}</span></div></div>
        </section>

        <section class="data-source-section sync-history">
          <div class="section-heading"><div><h3>导入运行记录</h3><p>记录行数、状态、错误摘要和创建时间。</p></div></div>
          <div v-if="runs.length" class="table-wrap"><table><thead><tr><th>状态</th><th>总行数</th><th>导入数</th><th>问题数</th><th>创建时间</th></tr></thead><tbody><tr v-for="run in runs" :key="run.id"><td><span class="status-chip" :class="run.status === 'completed' ? 'status-active' : 'status-closed'">{{ statusLabel(run.status) }}</span></td><td>{{ run.rows_total }}</td><td>{{ run.rows_imported }}</td><td>{{ run.errors.length }}</td><td>{{ formatTime(run.created_at) }}</td></tr></tbody></table></div>
          <p v-else class="quiet-empty">尚无导入记录。</p>
        </section>
      </section>
      <section v-else class="data-source-empty panel"><span class="eyebrow">DATA CONNECTION</span><h2>连接数据，再映射到本体</h2><p>先创建本地文件连接，然后选择 CSV 或 JSON、设置字段映射和主键。服务端校验通过后才允许原子导入。</p><div v-if="loading" class="quiet-empty">正在读取本体…</div><div v-else-if="!objectTypes.length" class="quiet-empty">当前本体还没有对象类型。先创建对象和属性，再配置数据映射。</div></section>
    </div>
  </div>
</template>
