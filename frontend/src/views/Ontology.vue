<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { api, readableError } from "../api/client";
import type { ActionDefinition, LinkType, ObjectType, Ontology as OntologyRecord } from "../types";

interface DataSource {
  id: string;
  name: string;
  connector_type: string;
  last_run_status: string | null;
  last_run_at: string | null;
}
interface DataMapping {
  id: string;
  connection_id: string;
  object_type_api_name: string;
  object_type_display_name: string;
  primary_key_field: string;
  field_mappings: Record<string, string>;
}
interface AuditEntry {
  id: string;
  actor_email?: string;
  event_type: string;
  resource_type: string;
  resource_id: string;
  details: Record<string, unknown>;
  created_at: string;
}

const route = useRoute();
const router = useRouter();
const tabs = [
  { id: "overview", label: "概览" },
  { id: "properties", label: "属性" },
  { id: "links", label: "链接" },
  { id: "actions", label: "Actions" },
  { id: "data", label: "数据" },
  { id: "dependents", label: "依赖" },
  { id: "usage", label: "使用情况" },
  { id: "security", label: "安全" },
  { id: "history", label: "历史" },
];
const ontologies = ref<OntologyRecord[]>([]);
const selectedOntology = ref("");
const objectTypes = ref<ObjectType[]>([]);
const linkTypes = ref<LinkType[]>([]);
const actions = ref<ActionDefinition[]>([]);
const dataSources = ref<DataSource[]>([]);
const dataMappings = ref<DataMapping[]>([]);
const auditEvents = ref<AuditEntry[]>([]);
const selectedTypeId = ref("");
const activeTab = ref("overview");
const filterText = ref("");
const objectCount = ref(0);
const error = ref("");
const loading = ref(false);
const detailLoading = ref(false);

const selectedType = computed(() => objectTypes.value.find((item) => item.id === selectedTypeId.value) ?? null);
const filteredTypes = computed(() => {
  const query = filterText.value.trim().toLowerCase();
  if (!query) return objectTypes.value;
  return objectTypes.value.filter((item) => `${item.display_name} ${item.plural_display_name || ""} ${item.api_name} ${item.description} ${item.aliases?.join(" ") || ""} ${item.groups?.join(" ") || ""}`.toLowerCase().includes(query));
});
const relatedLinks = computed(() => linkTypes.value.filter((item) => item.source_type_id === selectedTypeId.value || item.target_type_id === selectedTypeId.value));
const typeActions = computed(() => actions.value.filter((item) => item.object_type_api_name === selectedType.value?.api_name));
const typeMappings = computed(() => dataMappings.value.filter((item) => item.object_type_api_name === selectedType.value?.api_name));
const linkedTypes = computed(() => objectTypes.value.filter((item) => relatedLinks.value.some((link) => link.source_type_id === item.id || link.target_type_id === item.id)));

function typeDisplay(id: string) {
  return objectTypes.value.find((item) => item.id === id)?.display_name ?? "未知对象类型";
}

function routeString(value: unknown, fallback: string) {
  return typeof value === "string" ? value : fallback;
}

async function loadWorkspace() {
  loading.value = true;
  error.value = "";
  try {
    ontologies.value = await api.get<OntologyRecord[]>("/api/ontology");
    selectedOntology.value = ontologies.value[0]?.id ?? "";
    if (!selectedOntology.value) return;
    const [types, links, actionList, sources] = await Promise.all([
      api.get<ObjectType[]>("/api/object-types", { ontology_id: selectedOntology.value }),
      api.get<LinkType[]>("/api/link-types", { ontology_id: selectedOntology.value }),
      api.get<ActionDefinition[]>("/api/actions", { ontology_id: selectedOntology.value }),
      api.get<DataSource[]>("/api/data-sources", { ontology_id: selectedOntology.value }),
    ]);
    objectTypes.value = types;
    linkTypes.value = links;
    actions.value = actionList;
    dataSources.value = sources;
    const preferredApiName = routeString(route.query.type, "");
    selectedTypeId.value = types.find((item) => item.api_name === preferredApiName)?.id ?? types[0]?.id ?? "";
    const requestedTab = routeString(route.query.tab, "overview");
    activeTab.value = tabs.some((tab) => tab.id === requestedTab) ? requestedTab : "overview";
    const sourceMappings = await Promise.all(
      sources.map((source) => api.get<DataMapping[]>(`/api/data-sources/${source.id}/mappings`)),
    );
    dataMappings.value = sourceMappings.flat();
    await loadSelectedTypeContext();
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function loadSelectedTypeContext() {
  if (!selectedType.value) {
    objectCount.value = 0;
    auditEvents.value = [];
    return;
  }
  detailLoading.value = true;
  try {
    const [records, history] = await Promise.all([
      api.get<{ total: number }>("/api/objects", {
        ontology_id: selectedOntology.value,
        object_type_api_name: selectedType.value.api_name,
        page_size: 1,
      }),
      api.get<{ data: AuditEntry[] }>("/api/audit-events", { resource_type: "proposal", page: 1, page_size: 10 }),
    ]);
    objectCount.value = records.total;
    auditEvents.value = history.data;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    detailLoading.value = false;
  }
}

function selectType(typeId: string) {
  selectedTypeId.value = typeId;
  void loadSelectedTypeContext();
  void router.replace({ query: { ...route.query, type: selectedType.value?.api_name, tab: activeTab.value } });
}

function selectTab(tabId: string) {
  activeTab.value = tabId;
  void router.replace({ query: { ...route.query, type: selectedType.value?.api_name, tab: tabId } });
}

function formatCriteria(criteria: Record<string, unknown> | undefined) {
  return criteria && Object.keys(criteria).length ? JSON.stringify(criteria) : "无额外条件";
}

function statusLabel(status: string | null) {
  if (status === "completed") return "最近导入成功";
  if (status === "failed") return "最近导入失败";
  if (status === "running") return "正在运行";
  return "尚未运行";
}

function describeEvent(event: AuditEntry) {
  const labels: Record<string, string> = {
    "schema.proposal.created": "创建结构提案",
    "schema.proposal.submitted": "提交结构提案",
    "schema.proposal.merged": "合并结构提案",
    "schema.proposal.rejected": "驳回结构提案",
  };
  return labels[event.event_type] ?? event.event_type;
}

onMounted(loadWorkspace);
</script>

<template>
  <div class="page-content ontology-manager-page">
    <div class="page-heading manager-heading">
      <div><span class="eyebrow">ONTOLOGY MANAGER · RESOURCE CATALOG</span><h1>本体结构</h1><p>浏览对象类型、属性、链接、Action、数据来源和治理状态。</p></div>
      <label class="ontology-select-label">本体<select v-model="selectedOntology" class="select-control" @change="loadWorkspace"><option v-for="ontology in ontologies" :key="ontology.id" :value="ontology.id">{{ ontology.display_name }} · v{{ ontology.revision }}</option></select></label>
    </div>
    <div v-if="error" class="notice notice-error" role="alert">{{ error }} <button @click="loadWorkspace">重新加载</button></div>
    <div class="ontology-explorer-layout">
      <aside class="ontology-resource-index panel">
        <div class="resource-index-heading"><div><span class="eyebrow">资源目录</span><strong>对象类型</strong></div><span>{{ filteredTypes.length }} / {{ objectTypes.length }}</span></div>
        <label class="resource-search">搜索名称或 API<input v-model="filterText" aria-label="筛选本体资源" placeholder="例如 customer" /></label>
        <button v-for="item in filteredTypes" :key="item.id" class="resource-index-item" :class="{ selected: selectedTypeId === item.id }" @click="selectType(item.id)">
          <span class="type-glyph" :style="{ backgroundColor: item.icon_color }">{{ item.display_name.slice(0, 1) }}</span><span><strong>{{ item.display_name }}</strong><code>{{ item.api_name }}</code></span><small>{{ item.properties.length }}</small>
        </button>
        <div class="resource-index-heading link-index-heading"><div><span class="eyebrow">关系</span><strong>链接类型</strong></div><span>{{ linkTypes.length }}</span></div>
        <div v-for="link in linkTypes" :key="link.id" class="resource-link-index"><span class="link-symbol">⇄</span><span><strong>{{ link.display_name }}</strong><small>{{ typeDisplay(link.source_type_id) }} → {{ typeDisplay(link.target_type_id) }}</small></span></div>
        <p v-if="!loading && !objectTypes.length" class="quiet-empty">当前本体尚无对象类型。创建隔离分支开始建模。</p>
        <p v-else-if="!loading && !filteredTypes.length" class="quiet-empty">没有符合筛选条件的对象类型。</p>
      </aside>

      <section v-if="selectedType" class="ontology-resource-detail panel">
        <header class="ontology-resource-header">
          <div><span class="eyebrow">OBJECT TYPE · {{ selectedType.api_name }}</span><h2>{{ selectedType.display_name }}</h2><p>{{ selectedType.description || "尚未添加类型说明。" }}</p><div class="ontology-type-metadata"><span>{{ selectedType.plural_display_name || selectedType.display_name }}</span><code>标题键：{{ selectedType.title_key_property || selectedType.primary_key_property }}</code><span v-for="group in selectedType.groups || []" :key="group">{{ group }}</span><small v-if="selectedType.aliases?.length">别名：{{ selectedType.aliases.join("、") }}</small></div></div>
          <div class="resource-header-actions"><span class="api-tag">{{ selectedType.api_name }}</span><RouterLink class="button button-secondary" to="/branches">在隔离分支中编辑</RouterLink></div>
        </header>
        <nav class="resource-detail-tabs" aria-label="对象类型详情视图" role="tablist">
          <button v-for="tab in tabs" :key="tab.id" :class="{ selected: activeTab === tab.id }" :aria-pressed="activeTab === tab.id" @click="selectTab(tab.id)">{{ tab.label }}</button>
        </nav>

        <div v-if="detailLoading" class="empty-state compact">正在读取对象使用情况…</div>
        <div v-else-if="activeTab === 'overview'" class="resource-tab-content">
          <div class="resource-stat-strip"><div><span>主键属性</span><strong><code>{{ selectedType.primary_key_property }}</code></strong></div><div><span>对象属性</span><strong>{{ selectedType.properties.length }}</strong></div><div><span>链接</span><strong>{{ relatedLinks.length }}</strong></div><div><span>Actions</span><strong>{{ typeActions.length }}</strong></div><div><span>对象记录</span><strong>{{ objectCount }}</strong></div><div><span>本体版本</span><strong>v{{ ontologies.find((item) => item.id === selectedOntology)?.revision ?? "—" }}</strong></div></div>
          <section class="resource-overview-card"><div class="section-heading"><div><h3>资源说明</h3><p>对象类型 ID 和语义边界</p></div></div><dl class="resource-metadata-grid"><dt>显示名称</dt><dd>{{ selectedType.display_name }}</dd><dt>API 名称</dt><dd><code>{{ selectedType.api_name }}</code></dd><dt>类型说明</dt><dd>{{ selectedType.description || "未填写" }}</dd><dt>数据来源</dt><dd>{{ typeMappings.length ? typeMappings.map((mapping) => mapping.object_type_display_name).join("、") : "无 backing datasource；数据可由 Action 或直接对象 API 写入" }}</dd></dl></section>
          <section class="resource-overview-card"><div class="section-heading"><div><h3>对象属性</h3><p>主键、类型和读写约束</p></div><button class="button button-quiet" @click="selectTab('properties')">查看全部属性</button></div><div class="table-wrap"><table><thead><tr><th>属性</th><th>API 名称</th><th>类型</th><th>约束</th></tr></thead><tbody><tr v-for="property in selectedType.properties.slice(0, 8)" :key="property.id"><td>{{ property.display_name }}</td><td><code>{{ property.api_name }}</code></td><td>{{ property.data_type }}</td><td><span v-if="property.api_name === selectedType.primary_key_property" class="constraint-chip">主键</span><span v-if="property.required" class="constraint-chip">必填</span><span v-if="property.sensitive" class="constraint-chip sensitive-chip">敏感</span></td></tr></tbody></table></div></section>
        </div>

        <div v-else-if="activeTab === 'properties'" class="resource-tab-content"><div class="section-heading"><div><h3>属性定义</h3><p>类型、可空性、唯一性、读写与敏感标记由服务端返回。</p></div><span class="revision-pill">{{ selectedType.properties.length }} 项</span></div><div class="table-wrap"><table><thead><tr><th>显示名称</th><th>API 名称</th><th>数据类型</th><th>约束与安全</th><th>枚举选项</th></tr></thead><tbody><tr v-for="property in selectedType.properties" :key="property.id"><td><strong>{{ property.display_name }}</strong></td><td><code>{{ property.api_name }}</code></td><td><span class="type-badge">{{ property.data_type }}</span></td><td><span v-if="property.api_name === selectedType.primary_key_property" class="constraint-chip">主键</span><span v-if="property.required" class="constraint-chip">必填</span><span v-if="property.unique_value" class="constraint-chip">唯一值</span><span v-if="property.sensitive" class="constraint-chip sensitive-chip">敏感字段</span><span v-if="!property.editable" class="constraint-chip">只读</span></td><td>{{ Array.isArray(property.options?.choices) ? property.options.choices.join("、") : "—" }}</td></tr></tbody></table></div><p v-if="!selectedType.properties.length" class="quiet-empty">此对象类型尚无属性。</p></div>

        <div v-else-if="activeTab === 'links'" class="resource-tab-content"><div class="section-heading"><div><h3>关联链接类型</h3><p>显示该类型作为关系起点或终点的链接定义。</p></div><span class="revision-pill">{{ relatedLinks.length }} 项</span></div><div v-if="relatedLinks.length" class="table-wrap"><table><thead><tr><th>链接</th><th>API 名称</th><th>方向</th><th>两端对象类型</th></tr></thead><tbody><tr v-for="link in relatedLinks" :key="link.id"><td><strong>{{ link.display_name }}</strong></td><td><code>{{ link.api_name }}</code></td><td>{{ link.source_type_id === selectedType.id ? "出向" : "入向" }}</td><td>{{ typeDisplay(link.source_type_id) }} → {{ typeDisplay(link.target_type_id) }}</td></tr></tbody></table></div><p v-else class="quiet-empty">此类型暂未参与任何链接。</p></div>

        <div v-else-if="activeTab === 'actions'" class="resource-tab-content"><div class="section-heading"><div><h3>对象 Actions</h3><p>可写属性、参数约束与提交条件；执行时服务端再次检查授权和版本。</p></div><span class="revision-pill">{{ typeActions.length }} 项</span></div><div v-if="typeActions.length" class="action-definition-list"><article v-for="action in typeActions" :key="action.id" class="action-definition-card"><header><div><strong>{{ action.display_name }}</strong><code>{{ action.api_name }}</code></div><span class="status-chip" :class="action.enabled ? 'status-active' : 'status-closed'">{{ action.enabled ? "已启用" : "已停用" }}</span></header><p>{{ action.description || "未填写说明" }}</p><div class="action-definition-meta"><span>写入范围：{{ action.allowed_properties.join("、") || "无" }}</span><span>参数 schema</span></div><pre>{{ JSON.stringify(action.parameters_schema, null, 2) }}</pre><div class="action-definition-meta"><span>提交条件</span><code>{{ formatCriteria(action.submission_criteria) }}</code></div></article></div><p v-else class="quiet-empty">此类型暂无 Action。可在隔离分支的 Action 编辑器中创建。</p></div>

        <div v-else-if="activeTab === 'data'" class="resource-tab-content"><div class="section-heading"><div><h3>Backing datasource 与列映射</h3><p>查看来源连接、映射列、主键和最近导入状态。</p></div><RouterLink class="button button-secondary" to="/data-sources">管理数据源</RouterLink></div><div v-if="typeMappings.length" class="data-mapping-detail-list"><article v-for="mapping in typeMappings" :key="mapping.id" class="data-mapping-detail-card"><header><div><strong>{{ mapping.object_type_display_name }}</strong><code>{{ dataSources.find((source) => source.id === mapping.connection_id)?.name ?? "数据源" }}</code></div><span class="status-chip">{{ statusLabel(dataSources.find((source) => source.id === mapping.connection_id)?.last_run_status ?? null) }}</span></header><div class="mapping-column-list"><span v-for="(target, source) in mapping.field_mappings" :key="source"><code>{{ source }}</code><b>→</b><code>{{ target }}</code><small v-if="source === mapping.primary_key_field">主键</small></span></div></article></div><p v-else class="quiet-empty">此类型没有 backing datasource 映射；你可以从数据源工作区配置本地 CSV/JSON 映射。</p></div>

        <div v-else-if="activeTab === 'dependents'" class="resource-tab-content"><div class="section-heading"><div><h3>直接依赖资源</h3><p>由当前对象类型链接到的对象类型，以及依赖它的 Action 和数据映射。</p></div></div><div class="dependent-resource-grid"><article><span class="eyebrow">LINK TYPES</span><strong>{{ relatedLinks.length }}</strong><p>{{ relatedLinks.map((item) => item.display_name).join("、") || "无链接依赖" }}</p></article><article><span class="eyebrow">ACTIONS</span><strong>{{ typeActions.length }}</strong><p>{{ typeActions.map((item) => item.display_name).join("、") || "无 Action 依赖" }}</p></article><article><span class="eyebrow">DATASOURCE MAPPINGS</span><strong>{{ typeMappings.length }}</strong><p>{{ typeMappings.map((item) => item.object_type_display_name).join("、") || "无数据映射依赖" }}</p></article><article><span class="eyebrow">RELATED TYPES</span><strong>{{ linkedTypes.length }}</strong><p>{{ linkedTypes.map((item) => item.display_name).join("、") || "无关联类型" }}</p></article></div></div>

        <div v-else-if="activeTab === 'usage'" class="resource-tab-content"><div class="section-heading"><div><h3>使用情况</h3><p>当前使用量和本体资源引用摘要。</p></div></div><div class="resource-stat-strip usage-stat-strip"><div><span>对象记录</span><strong>{{ objectCount }}</strong></div><div><span>来源映射</span><strong>{{ typeMappings.length }}</strong></div><div><span>入向/出向链接</span><strong>{{ relatedLinks.length }}</strong></div><div><span>可用 Actions</span><strong>{{ typeActions.filter((item) => item.enabled).length }}</strong></div></div><div class="resource-overview-card"><h3>引用路径</h3><p>该对象类型参与 {{ relatedLinks.length }} 种链接、提供 {{ typeActions.length }} 个 Action，并由 {{ typeMappings.length }} 个本地数据映射填充。</p></div></div>

        <div v-else-if="activeTab === 'security'" class="resource-tab-content"><div class="section-heading"><div><h3>对象与属性访问边界</h3><p>当前实现按应用角色控制读取和写入；属性敏感标记在对象响应时执行字段隐藏。</p></div></div><div class="security-role-grid"><article><strong>查看者</strong><span>可以读取对象与关系；敏感属性从响应中移除。</span></article><article><strong>编辑者</strong><span>可以读取敏感属性、创建对象与链接、预览或执行已授权 Action。</span></article><article><strong>管理员</strong><span>拥有编辑者权限，并可管理提案评审与合并。</span></article></div><div class="resource-overview-card"><h3>敏感属性</h3><div v-if="selectedType.properties.some((item) => item.sensitive)" class="sensitive-property-list"><span v-for="property in selectedType.properties.filter((item) => item.sensitive)" :key="property.id"><strong>{{ property.display_name }}</strong><code>{{ property.api_name }}</code><small>查看者不可见</small></span></div><p v-else class="quiet-empty">此类型没有标记为敏感的属性。</p></div><p class="security-boundary-note">此项目暂未实现 Foundry 的 Compass 资源权限、对象级策略或行/列/格细粒度访问策略；上述为本项目已经实现的全局角色与字段隐藏行为。</p></div>

        <div v-else class="resource-tab-content"><div class="section-heading"><div><h3>本体变更历史</h3><p>列出最近的结构提案治理事件；事件详情返回实际记录的变更上下文。</p></div><RouterLink class="button button-secondary" to="/audit">打开完整审计记录</RouterLink></div><div v-if="auditEvents.length" class="resource-history-list"><article v-for="event in auditEvents" :key="event.id"><span class="history-dot" /><div><strong>{{ describeEvent(event) }}</strong><code>{{ event.event_type }}</code><small>{{ event.actor_email || "系统" }} · {{ new Date(event.created_at).toLocaleString("zh-CN") }}</small></div><code>{{ event.resource_type }} · {{ event.resource_id }}</code></article></div><p v-else class="quiet-empty">暂无结构提案审计事件。</p></div>
      </section>
      <section v-else class="ontology-empty panel"><span class="eyebrow">ONTOLOGY · v{{ ontologies[0]?.revision ?? "—" }}</span><h2>还没有对象类型</h2><p>从隔离分支创建对象类型、属性和关系；通过检查与评审后，再合并进入主本体。</p><RouterLink class="button button-primary" to="/branches">打开分支工作区</RouterLink></section>
    </div>
  </div>
</template>
