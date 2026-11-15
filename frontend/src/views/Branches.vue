<script setup lang="ts">
import { computed, onMounted, ref, watch } from "vue";
import { api, readableError } from "../api/client";
import type { Ontology, OntologyBranch } from "../types";

type ResourceKind = "object_type" | "property" | "link_type" | "action";

const ontologies = ref<Ontology[]>([]);
const branches = ref<OntologyBranch[]>([]);
const selectedOntologyId = ref("");
const selectedBranchId = ref("");
const loading = ref(false);
const busy = ref(false);
const error = ref("");
const notice = ref("");
const resourceKind = ref<ResourceKind>("object_type");
const objectTypeMode = ref<"create" | "edit">("create");
const propertyMode = ref<"create" | "edit">("create");
const linkMode = ref<"create" | "edit">("create");
const actionMode = ref<"create" | "edit">("create");
const objectTypeEditSelection = ref("");
const propertyEditSelection = ref("");
const linkEditSelection = ref("");
const actionEditSelection = ref("");
const resourceKinds: Array<{ value: ResourceKind; label: string }> = [
  { value: "object_type", label: "对象" },
  { value: "property", label: "属性" },
  { value: "link_type", label: "链接" },
  { value: "action", label: "Action" },
];
const branchForm = ref({ name: "", description: "" });
const proposalTitle = ref("");
const objectTypeForm = ref({
  api_name: "", display_name: "", plural_display_name: "", description: "", primary_key_property: "id", title_key_property: "id",
  aliases: "", groups: "", icon: "object", icon_color: "#4F8067",
});
const objectTypeProperties = ref<Array<{ api_name: string; display_name: string; data_type: string; enum_choices: string; required: boolean; editable: boolean; unique_value: boolean; sensitive: boolean }>>([]);
const propertyForm = ref({
  object_type_api_name: "",
  api_name: "",
  display_name: "",
  data_type: "string",
  required: false,
  editable: true,
  unique_value: false,
  sensitive: false,
  enum_choices: "",
});
const linkForm = ref({ api_name: "", display_name: "", description: "", source_type_api_name: "", target_type_api_name: "" });
const actionForm = ref({
  api_name: "",
  display_name: "",
  description: "",
  object_type_api_name: "",
  allowed_properties: [] as string[],
  submission_criteria_json: "",
  parameters_schema_json: "",
  enabled: true,
});

const selectedOntology = computed(() => ontologies.value.find((item) => item.id === selectedOntologyId.value) ?? null);
const selectedBranch = computed(() => branches.value.find((item) => item.id === selectedBranchId.value) ?? null);
const objectTypes = computed(() => selectedBranch.value?.snapshot.object_types ?? []);
const editedObjectType = computed(() => objectTypes.value.find((item) => item.api_name === objectTypeEditSelection.value) ?? null);
const selectedProperty = computed(() => {
  const [typeName, propertyName] = propertyEditSelection.value.split(".");
  return objectTypes.value.find((item) => item.api_name === typeName)?.properties.find((item) => item.api_name === propertyName) ?? null;
});
const selectedLink = computed(() => selectedBranch.value?.snapshot.link_types.find((item) => item.api_name === linkEditSelection.value) ?? null);
const selectedAction = computed(() => selectedBranch.value?.snapshot.actions?.find((item) => item.api_name === actionEditSelection.value) ?? null);
const editableProperties = computed(() => objectTypes.value.flatMap((item) => item.properties.map((property) => ({
  key: `${item.api_name}.${property.api_name}`,
  label: `${item.display_name} · ${property.display_name} · ${property.api_name}`,
}))));
const selectedActionType = computed(() => objectTypes.value.find((item) => item.api_name === actionForm.value.object_type_api_name) ?? null);
const titleKeyOptions = computed(() => [
  { api_name: objectTypeForm.value.primary_key_property.trim(), display_name: "主键属性" },
  ...(objectTypeMode.value === "edit"
    ? (editedObjectType.value?.properties ?? []).map((item) => ({ api_name: item.api_name, display_name: item.display_name || item.api_name }))
    : objectTypeProperties.value.map((item) => ({ api_name: item.api_name, display_name: item.display_name || item.api_name }))),
].filter((item, index, all) => item.api_name && all.findIndex((candidate) => candidate.api_name === item.api_name) === index));
const selectedBranchCanEdit = computed(() => selectedBranch.value?.status === "active");
const resourceCount = computed(() => {
  const snapshot = selectedBranch.value?.snapshot;
  return (snapshot?.object_types.length ?? 0)
    + (snapshot?.object_types.reduce((total, type) => total + type.properties.length, 0) ?? 0)
    + (snapshot?.link_types.length ?? 0)
    + (snapshot?.actions?.length ?? 0);
});

async function loadWorkspace() {
  loading.value = true;
  error.value = "";
  try {
    ontologies.value = await api.get<Ontology[]>("/api/ontology");
    if (!selectedOntologyId.value || !ontologies.value.some((item) => item.id === selectedOntologyId.value)) {
      selectedOntologyId.value = ontologies.value[0]?.id ?? "";
    }
    await loadBranches();
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function loadBranches() {
  if (!selectedOntologyId.value) {
    branches.value = [];
    selectedBranchId.value = "";
    return;
  }
  branches.value = await api.get<OntologyBranch[]>("/api/branches", { ontology_id: selectedOntologyId.value });
  if (!branches.value.some((item) => item.id === selectedBranchId.value)) {
    selectedBranchId.value = branches.value.find((item) => item.status === "active")?.id ?? branches.value[0]?.id ?? "";
  }
}

async function changeOntology() {
  selectedBranchId.value = "";
  await loadWorkspace();
}

function replaceBranch(updated: OntologyBranch) {
  const index = branches.value.findIndex((item) => item.id === updated.id);
  if (index === -1) branches.value.unshift(updated);
  else branches.value.splice(index, 1, updated);
  selectedBranchId.value = updated.id;
}

async function createBranch() {
  if (!selectedOntologyId.value || !branchForm.value.name.trim()) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const branch = await api.post<OntologyBranch>("/api/branches", {
      ontology_id: selectedOntologyId.value,
      name: branchForm.value.name.trim(),
      description: branchForm.value.description.trim(),
    });
    replaceBranch(branch);
    branchForm.value = { name: "", description: "" };
    notice.value = `已基于 v${branch.base_revision} 创建分支。修改只保存在此分支中。`;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

function splitCsv(value: string) {
  return [...new Set(value.split(",").map((item) => item.trim()).filter(Boolean))];
}

function addObjectProperty() {
  const index = objectTypeProperties.value.length + 1;
  objectTypeProperties.value.push({
    api_name: `property_${index}`,
    display_name: `属性 ${index}`,
    data_type: "string",
    enum_choices: "",
    required: false,
    editable: true,
    unique_value: false,
    sensitive: false,
  });
}

function removeObjectProperty(index: number) {
  const removed = objectTypeProperties.value[index];
  objectTypeProperties.value.splice(index, 1);
  if (removed && objectTypeForm.value.title_key_property === removed.api_name) {
    objectTypeForm.value.title_key_property = objectTypeForm.value.primary_key_property;
  }
}

function loadObjectTypeForEdit(apiName: string) {
  const item = objectTypes.value.find((candidate) => candidate.api_name === apiName);
  if (!item) return;
  objectTypeForm.value = {
    api_name: item.api_name,
    display_name: item.display_name,
    plural_display_name: item.plural_display_name || item.display_name,
    description: item.description || "",
    primary_key_property: item.primary_key_property || item.properties[0]?.api_name || "id",
    title_key_property: item.title_key_property || item.primary_key_property || item.properties[0]?.api_name || "id",
    aliases: (item.aliases ?? []).join(", "),
    groups: (item.groups ?? []).join(", "),
    icon: item.icon || "object",
    icon_color: item.icon_color || "#4F8067",
  };
  objectTypeProperties.value = [];
}

function loadPropertyForEdit(key: string) {
  const [typeName, propertyName] = key.split(".");
  const property = objectTypes.value.find((item) => item.api_name === typeName)?.properties.find((item) => item.api_name === propertyName);
  if (!property) return;
  propertyForm.value = {
    object_type_api_name: typeName,
    api_name: property.api_name,
    display_name: property.display_name,
    data_type: property.data_type,
    required: !!property.required,
    editable: !!property.editable,
    unique_value: !!property.unique_value,
    sensitive: !!property.sensitive,
    enum_choices: Array.isArray(property.options?.choices) ? property.options.choices.join(", ") : "",
  };
}

function loadLinkForEdit(apiName: string) {
  const link = selectedBranch.value?.snapshot.link_types.find((item) => item.api_name === apiName);
  if (!link) return;
  linkForm.value = {
    api_name: link.api_name,
    display_name: link.display_name,
    description: link.description || "",
    source_type_api_name: link.source_type_api_name,
    target_type_api_name: link.target_type_api_name,
  };
}

function loadActionForEdit(apiName: string) {
  const action = selectedBranch.value?.snapshot.actions?.find((item) => item.api_name === apiName);
  if (!action) return;
  actionForm.value = {
    api_name: action.api_name,
    display_name: action.display_name,
    description: action.description || "",
    object_type_api_name: action.object_type_api_name,
    allowed_properties: [...action.allowed_properties],
    submission_criteria_json: JSON.stringify(action.submission_criteria ?? {}, null, 2) === "{}" ? "" : JSON.stringify(action.submission_criteria ?? {}, null, 2),
    parameters_schema_json: JSON.stringify(action.parameters_schema ?? {}, null, 2),
    enabled: action.enabled,
  };
}

function buildChanges(): Array<Record<string, unknown>> {
  if (resourceKind.value === "object_type") {
    if (objectTypeMode.value === "edit") {
      if (!editedObjectType.value) throw new Error("请选择要修改的对象类型");
      return [{
        op: "update_object_type",
        api_name: objectTypeForm.value.api_name,
        display_name: objectTypeForm.value.display_name.trim(),
        plural_display_name: objectTypeForm.value.plural_display_name.trim() || objectTypeForm.value.display_name.trim(),
        description: objectTypeForm.value.description.trim(),
        title_key_property: objectTypeForm.value.title_key_property,
        aliases: splitCsv(objectTypeForm.value.aliases),
        groups: splitCsv(objectTypeForm.value.groups),
        icon: objectTypeForm.value.icon.trim() || "object",
        icon_color: objectTypeForm.value.icon_color,
      }];
    }
    const primaryKey = objectTypeForm.value.primary_key_property.trim() || "id";
    const titleKey = objectTypeForm.value.title_key_property.trim() || primaryKey;
    if (![primaryKey, ...objectTypeProperties.value.map((item) => item.api_name.trim())].includes(titleKey)) {
      throw new Error("标题键必须选择主键或本次创建的属性");
    }
    return [
      {
        op: "add_object_type",
        api_name: objectTypeForm.value.api_name.trim(),
        display_name: objectTypeForm.value.display_name.trim(),
        plural_display_name: objectTypeForm.value.plural_display_name.trim() || objectTypeForm.value.display_name.trim(),
        description: objectTypeForm.value.description.trim(),
        primary_key_property: primaryKey,
        title_key_property: titleKey,
        aliases: splitCsv(objectTypeForm.value.aliases),
        groups: splitCsv(objectTypeForm.value.groups),
        icon: objectTypeForm.value.icon.trim() || "object",
        icon_color: objectTypeForm.value.icon_color,
      },
      ...objectTypeProperties.value.map((item) => {
        const { enum_choices, ...property } = item;
        return {
          op: "add_property",
          object_type_api_name: objectTypeForm.value.api_name.trim(),
          ...property,
          api_name: item.api_name.trim(),
          display_name: item.display_name.trim(),
          ...(item.data_type === "enum" ? { options: { choices: splitCsv(enum_choices) } } : {}),
        };
      }),
    ];
  }
  if (resourceKind.value === "property") {
    if (propertyMode.value === "edit") {
      if (!selectedProperty.value) throw new Error("请选择要修改的属性");
      return [{
        op: "update_property",
        object_type_api_name: propertyForm.value.object_type_api_name,
        api_name: propertyForm.value.api_name,
        display_name: propertyForm.value.display_name.trim(),
        data_type: propertyForm.value.data_type,
        required: propertyForm.value.required,
        editable: propertyForm.value.editable,
        unique_value: propertyForm.value.unique_value,
        sensitive: propertyForm.value.sensitive,
        ...(propertyForm.value.data_type === "enum" ? { options: { choices: splitCsv(propertyForm.value.enum_choices) } } : {}),
      }];
    }
    return [{
      op: "add_property",
      ...propertyForm.value,
      api_name: propertyForm.value.api_name.trim(),
      display_name: propertyForm.value.display_name.trim(),
      ...(propertyForm.value.data_type === "enum" ? { options: { choices: splitCsv(propertyForm.value.enum_choices) } } : {}),
    }];
  }
  if (resourceKind.value === "link_type") {
    if (linkMode.value === "edit") {
      if (!selectedLink.value) throw new Error("请选择要修改的链接类型");
      return [{ op: "update_link_type", api_name: linkForm.value.api_name, display_name: linkForm.value.display_name.trim(), description: linkForm.value.description.trim() }];
    }
    return [{ op: "add_link_type", ...linkForm.value }];
  }

  if (actionMode.value === "edit" && !selectedAction.value) throw new Error("请选择要修改的 Action");
  if (!actionForm.value.allowed_properties.length) throw new Error("至少选择一个 Action 可修改的属性");
  const objectType = selectedActionType.value;
  if (!objectType) throw new Error("请选择 Action 目标对象类型");
  let parameters_schema: Record<string, Record<string, unknown>> = Object.fromEntries(actionForm.value.allowed_properties.map((apiName) => {
    const property = objectType.properties.find((item) => item.api_name === apiName);
    if (!property) throw new Error(`属性 ${apiName} 不存在于当前对象类型`);
    const type = property.data_type === "enum" ? "string" : property.data_type === "date" || property.data_type === "datetime" ? "string" : property.data_type === "json" ? undefined : property.data_type;
    return [apiName, {
      ...(type ? { type } : {}),
      required: property.required,
      ...(property.data_type === "enum" ? { enum: property.options?.choices ?? [] } : {}),
    }];
  }));
  if (actionMode.value === "edit" && actionForm.value.parameters_schema_json.trim()) {
    const parsed = JSON.parse(actionForm.value.parameters_schema_json);
    if (!parsed || Array.isArray(parsed) || typeof parsed !== "object") {
      throw new Error("参数 Schema 必须是 JSON 对象");
    }
    parameters_schema = parsed as Record<string, Record<string, unknown>>;
  }
  let submission_criteria: Record<string, unknown> = {};
  if (actionForm.value.submission_criteria_json.trim()) {
    const parsed = JSON.parse(actionForm.value.submission_criteria_json);
    if (!parsed || Array.isArray(parsed) || typeof parsed !== "object") {
      throw new Error("提交条件必须是 JSON 对象");
    }
    submission_criteria = parsed as Record<string, unknown>;
  }
  return [{
    op: actionMode.value === "edit" ? "update_action" : "add_action",
    api_name: actionForm.value.api_name.trim(),
    display_name: actionForm.value.display_name.trim(),
    description: actionForm.value.description.trim(),
    object_type_api_name: actionForm.value.object_type_api_name,
    allowed_properties: actionForm.value.allowed_properties,
    parameters_schema,
    submission_criteria,
    enabled: actionMode.value === "edit" ? actionForm.value.enabled : true,
  }];
}

async function stageChange() {
  if (!selectedBranch.value || !selectedBranchCanEdit.value) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const updated = await api.post<OntologyBranch>(`/api/branches/${selectedBranch.value.id}/changes`, {
      changes: buildChanges(),
    });
    replaceBranch(updated);
    notice.value = "修改已暂存在分支中；当前 main 尚未改变。";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

async function validateBranch() {
  if (!selectedBranch.value) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const validation = await api.post<OntologyBranch["validation"]>(
      `/api/branches/${selectedBranch.value.id}/validate`,
    );
    replaceBranch({ ...selectedBranch.value, validation });
    notice.value = validation.valid ? "本体检查通过，可以提交评审。" : "检查发现错误，请先处理下方项目。";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

async function rebaseBranch() {
  if (!selectedBranch.value) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    const updated = await api.post<OntologyBranch>(`/api/branches/${selectedBranch.value.id}/rebase`);
    replaceBranch(updated);
    notice.value = `分支已更新到 main v${updated.base_revision}，原有修改已保留。`;
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

async function proposeBranch() {
  if (!selectedBranch.value || !selectedBranchCanEdit.value) return;
  busy.value = true;
  error.value = "";
  notice.value = "";
  try {
    await api.post(`/api/branches/${selectedBranch.value.id}/propose`, {
      title: proposalTitle.value.trim() || `合并 ${selectedBranch.value.name}`,
      description: selectedBranch.value.description,
    });
    replaceBranch({ ...selectedBranch.value, status: "proposed" });
    notice.value = "提案已提交，变更资源将逐项评审；通过前不会修改 main。";
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    busy.value = false;
  }
}

onMounted(loadWorkspace);
watch(() => objectTypeForm.value.primary_key_property, (next, previous) => {
  if (objectTypeForm.value.title_key_property === previous) objectTypeForm.value.title_key_property = next;
});
</script>

<template>
  <div class="page-content ontology-manager-page">
    <div class="page-heading manager-heading">
      <div>
        <span class="eyebrow">ONTOLOGY · CHANGE MANAGEMENT</span>
        <h1>本体分支</h1>
        <p>在隔离快照中修改本体，检查依赖与冲突，再按资源提交评审。</p>
      </div>
      <label class="ontology-select-label">本体
        <select v-model="selectedOntologyId" class="select-control" @change="changeOntology">
          <option v-for="ontology in ontologies" :key="ontology.id" :value="ontology.id">{{ ontology.display_name }} · v{{ ontology.revision }}</option>
        </select>
      </label>
    </div>

    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div>
    <div v-if="notice" class="notice notice-success" role="status" aria-live="polite">{{ notice }}</div>

    <div class="branch-workbench">
      <aside class="branch-index panel">
        <div class="panel-title-row">
          <div><span class="eyebrow">分支目录</span><h2>{{ branches.length }} 个分支</h2></div>
          <span class="revision-pill">main · v{{ selectedOntology?.revision ?? "—" }}</span>
        </div>
        <form class="branch-create-form" @submit.prevent="createBranch">
          <label>新建隔离分支
            <input v-model="branchForm.name" aria-label="分支名称" placeholder="例如 customer-cleanup" required minlength="2" />
          </label>
          <input v-model="branchForm.description" aria-label="分支说明" placeholder="修改目的（可选）" />
          <button class="button button-primary" aria-label="创建分支" :disabled="busy || !selectedOntologyId">新建分支</button>
        </form>
        <div class="branch-list" aria-label="分支列表">
          <button
            v-for="branch in branches"
            :key="branch.id"
            class="branch-list-item"
            :class="{ selected: branch.id === selectedBranchId }"
            :aria-pressed="branch.id === selectedBranchId"
            @click="selectedBranchId = branch.id"
          >
            <span class="branch-state-dot" :class="`state-${branch.status}`" />
            <span class="branch-list-copy"><strong>{{ branch.name }}</strong><small>{{ branch.description || "无说明" }}</small></span>
            <span class="branch-revision">v{{ branch.base_revision }}</span>
          </button>
          <p v-if="!loading && !branches.length" class="quiet-empty">还没有分支。创建分支后，修改才会与 main 隔离。</p>
          <p v-if="loading" class="quiet-empty">正在读取分支…</p>
        </div>
      </aside>

      <section v-if="selectedBranch" class="branch-detail panel">
        <div class="branch-detail-header">
          <div>
            <div class="resource-title-line"><span class="resource-kind-tag">ONTOLOGY BRANCH</span><span class="status-chip" :class="`status-${selectedBranch.status}`">{{ selectedBranch.status === "active" ? "编辑中" : selectedBranch.status === "proposed" ? "待评审" : selectedBranch.status === "merged" ? "已合并" : "已关闭" }}</span></div>
            <h2>{{ selectedBranch.name }}</h2>
            <p>{{ selectedBranch.description || "在独立本体快照中编辑对象、属性与链接。" }}</p>
          </div>
          <div class="branch-actions">
            <button class="button button-secondary" aria-label="更新分支基线" :disabled="busy || !selectedBranchCanEdit" @click="rebaseBranch">更新基线</button>
            <button class="button button-primary" aria-label="校验本体分支" :disabled="busy || !selectedBranchCanEdit" @click="validateBranch">检查变更</button>
          </div>
        </div>

        <div class="branch-summary-strip">
          <div><span>基于版本</span><strong>v{{ selectedBranch.base_revision }}</strong></div>
          <div><span>Schema 资源</span><strong>{{ resourceCount }}</strong></div>
          <div><span>暂存修改</span><strong>{{ selectedBranch.changes.length }}</strong></div>
            <div><span>检查结果</span><strong :class="{ 'text-danger': !selectedBranch.validation.valid }">{{ selectedBranch.validation.valid ? "通过" : `${selectedBranch.validation.errors.length} 个错误` }}</strong></div>
        </div>

        <div class="branch-detail-grid">
          <section class="branch-schema-section">
            <div class="section-heading"><div><h3>分支本体快照</h3><p>以下定义仅对当前分支可见。</p></div><span class="muted">{{ selectedBranch.snapshot.object_types.length }} Object types · {{ selectedBranch.snapshot.link_types.length }} Links</span></div>
            <div class="table-wrap schema-table-wrap">
              <table>
                <thead><tr><th>对象类型</th><th>API 名称</th><th>主键 / 标题键</th><th>属性</th></tr></thead>
                <tbody>
                  <tr v-for="type in selectedBranch.snapshot.object_types" :key="type.api_name">
                    <td><strong>{{ type.display_name }}</strong><small>{{ type.plural_display_name || type.display_name }}</small></td><td><code>{{ type.api_name }}</code></td><td><code>{{ type.primary_key_property }} / {{ type.title_key_property || type.primary_key_property }}</code></td><td>{{ type.properties.length }}</td>
                  </tr>
                  <tr v-if="!selectedBranch.snapshot.object_types.length"><td colspan="4" class="quiet-empty">此本体尚未定义对象类型。</td></tr>
                </tbody>
              </table>
            </div>
            <div class="branch-link-list">
              <div class="section-heading"><div><h3>链接类型</h3><p>关系方向以源类型和目标类型显示。</p></div></div>
              <div v-for="link in selectedBranch.snapshot.link_types" :key="link.api_name" class="branch-link-row">
                <code>{{ link.api_name }}</code><strong>{{ link.display_name }}</strong><span>{{ link.source_type_api_name }} <b>→</b> {{ link.target_type_api_name }}</span>
              </div>
              <p v-if="!selectedBranch.snapshot.link_types.length" class="quiet-empty">暂无链接类型。</p>
            </div>
            <div class="branch-link-list">
              <div class="section-heading"><div><h3>Action 定义</h3><p>配置对象写入范围、参数校验与提交条件。</p></div><span class="muted">{{ selectedBranch.snapshot.actions?.length ?? 0 }} Actions</span></div>
              <div v-for="action in selectedBranch.snapshot.actions ?? []" :key="action.api_name" class="branch-action-row">
                <div><strong>{{ action.display_name }}</strong><code>{{ action.api_name }}</code></div>
                <span>{{ action.object_type_api_name }}</span>
                <span>{{ action.allowed_properties.join("、") }}</span>
                <span class="status-chip" :class="action.enabled ? 'status-active' : 'status-closed'">{{ action.enabled ? "已启用" : "已停用" }}</span>
              </div>
              <p v-if="!selectedBranch.snapshot.actions?.length" class="quiet-empty">暂无 Action。选择右侧 Action 标签，在分支中添加配置。</p>
            </div>
            <div class="branch-change-list">
              <div class="section-heading"><div><h3>待审资源</h3><p>评审与合并按本体资源逐项处理。</p></div></div>
              <div v-for="(change, index) in selectedBranch.changes" :key="`${index}-${change.api_name}`" class="change-line">
                <span class="change-index">{{ String(index + 1).padStart(2, "0") }}</span>
                <span><strong>{{ change.display_name || change.api_name }}</strong><small>{{ change.op }} · {{ change.api_name || change.object_type_api_name }}</small></span>
                <span class="status-chip status-draft">待检查</span>
              </div>
              <p v-if="!selectedBranch.changes.length" class="quiet-empty">尚未暂存修改。</p>
            </div>
            <div v-if="selectedBranch.validation.errors.length || selectedBranch.validation.warnings.length" class="validation-list" aria-label="校验结果">
              <div v-for="issue in selectedBranch.validation.errors" :key="`error-${issue.path}-${issue.message}`" class="validation-issue validation-error"><strong>错误</strong><code>{{ issue.path }}</code><span>{{ issue.message }}</span></div>
              <div v-for="issue in selectedBranch.validation.warnings" :key="`warning-${issue.path}-${issue.message}`" class="validation-issue validation-warning"><strong>提示</strong><code>{{ issue.path }}</code><span>{{ issue.message }}</span></div>
            </div>
          </section>

          <aside class="branch-editor">
            <div class="section-heading"><div><h3>编辑分支</h3><p>新增结构先暂存到当前分支。</p></div></div>
            <div class="resource-kind-tabs" role="tablist" aria-label="结构资源类型">
              <button v-for="kind in resourceKinds" :key="kind.value" :class="{ selected: resourceKind === kind.value }" @click="resourceKind = kind.value">{{ kind.label }}</button>
            </div>

            <form v-if="resourceKind === 'object_type'" class="branch-edit-form" @submit.prevent="stageChange">
              <label>对象操作模式<select v-model="objectTypeMode" aria-label="对象操作模式"><option value="create">新建对象类型</option><option value="edit">修改现有对象</option></select></label>
              <label v-if="objectTypeMode === 'edit'">选择对象类型<select v-model="objectTypeEditSelection" aria-label="选择待修改对象类型" @change="loadObjectTypeForEdit(objectTypeEditSelection)" required><option value="" disabled>选择待修改的对象</option><option v-for="type in objectTypes" :key="type.api_name" :value="type.api_name">{{ type.display_name }} · {{ type.api_name }}</option></select></label>
              <label>对象 API 名称<input v-model="objectTypeForm.api_name" aria-label="对象 API 名称" placeholder="site" required pattern="[a-z][a-z0-9_]*" :readonly="objectTypeMode === 'edit'" /></label>
              <label>对象显示名称<input v-model="objectTypeForm.display_name" aria-label="对象显示名称" placeholder="站点" required /></label>
              <label>对象复数显示名称<input v-model="objectTypeForm.plural_display_name" aria-label="对象复数显示名称" placeholder="站点" /></label>
              <label>说明<textarea v-model="objectTypeForm.description" aria-label="对象说明" rows="2" placeholder="描述业务语义和边界" /></label>
              <label v-if="objectTypeMode === 'create'">主键属性<input v-model="objectTypeForm.primary_key_property" aria-label="主键属性" required /></label>
              <label v-else>主键属性<input v-model="objectTypeForm.primary_key_property" aria-label="主键属性" readonly /></label>
              <label>标题键<select v-model="objectTypeForm.title_key_property" aria-label="对象标题键"><option v-for="property in titleKeyOptions" :key="property.api_name" :value="property.api_name">{{ property.display_name }} · {{ property.api_name }}</option></select></label>
              <section v-if="objectTypeMode === 'create'" class="object-wizard-properties"><header><div><strong>对象属性</strong><small>主键属性会自动创建；在这里补充标题及其他业务属性。</small></div><button type="button" class="button button-quiet" data-action="add-object-property" @click="addObjectProperty">添加属性</button></header>
                <div v-for="(property, index) in objectTypeProperties" :key="index" class="object-wizard-property"><label>API 名称<input v-model="property.api_name" aria-label="新对象属性 API 名称" required pattern="[a-z][a-z0-9_]*" /></label><label>显示名称<input v-model="property.display_name" aria-label="新对象属性显示名称" required /></label><label>类型<select v-model="property.data_type" aria-label="新对象属性类型"><option value="string">文本</option><option value="integer">整数</option><option value="number">数字</option><option value="boolean">布尔</option><option value="date">日期</option><option value="datetime">日期时间</option><option value="enum">枚举</option><option value="json">JSON</option></select></label><label v-if="property.data_type === 'enum'">枚举选项<input v-model="property.enum_choices" aria-label="新对象属性枚举选项" placeholder="standard,preferred" /></label><label class="check-row"><input v-model="property.required" type="checkbox" />必填</label><label class="check-row"><input v-model="property.editable" type="checkbox" />可编辑</label><label class="check-row"><input v-model="property.unique_value" type="checkbox" />唯一</label><label class="check-row"><input v-model="property.sensitive" type="checkbox" />敏感</label><button type="button" class="text-button" @click="removeObjectProperty(index)">移除</button></div>
              </section>
              <p v-else class="form-help">属性结构通过“属性”页单独修改；此处仅调整对象类型元数据。</p>
              <label>别名（逗号分隔）<input v-model="objectTypeForm.aliases" aria-label="对象别名" placeholder="门店,仓库" /></label>
              <label>分组（逗号分隔）<input v-model="objectTypeForm.groups" aria-label="对象分组" placeholder="运营,供应链" /></label>
              <div class="form-grid"><label>图标名称<input v-model="objectTypeForm.icon" aria-label="对象图标" placeholder="warehouse" /></label><label>图标颜色<input v-model="objectTypeForm.icon_color" aria-label="对象图标颜色" pattern="#[0-9A-Fa-f]{6}" /></label></div>
              <button class="button button-primary" aria-label="暂存分支修改" :disabled="busy || !selectedBranchCanEdit">暂存修改</button>
            </form>

            <form v-else-if="resourceKind === 'property'" class="branch-edit-form" @submit.prevent="stageChange">
              <label>属性操作模式<select v-model="propertyMode" aria-label="属性操作模式"><option value="create">新增属性</option><option value="edit">修改现有属性</option></select></label>
              <label v-if="propertyMode === 'edit'">选择属性<select v-model="propertyEditSelection" aria-label="选择待修改属性" @change="loadPropertyForEdit(propertyEditSelection)" required><option value="" disabled>选择待修改的属性</option><option v-for="property in editableProperties" :key="property.key" :value="property.key">{{ property.label }}</option></select></label>
              <label v-if="propertyMode === 'create'">所属对象类型<select v-model="propertyForm.object_type_api_name" aria-label="所属对象类型" required><option value="" disabled>选择对象类型</option><option v-for="type in objectTypes" :key="type.api_name" :value="type.api_name">{{ type.display_name }} · {{ type.api_name }}</option></select></label>
              <label v-else>所属对象类型<input v-model="propertyForm.object_type_api_name" aria-label="所属对象类型" readonly /></label>
              <label>属性 API 名称<input v-model="propertyForm.api_name" aria-label="属性 API 名称" required pattern="[a-z][a-z0-9_]*" :readonly="propertyMode === 'edit'" /></label>
              <label>属性显示名称<input v-model="propertyForm.display_name" aria-label="属性显示名称" required /></label>
              <label>数据类型<select v-model="propertyForm.data_type" aria-label="属性数据类型"><option value="string">String</option><option value="integer">Integer</option><option value="number">Number</option><option value="boolean">Boolean</option><option value="date">Date</option><option value="datetime">DateTime</option><option value="enum">Enum</option><option value="json">JSON</option></select></label>
              <label v-if="propertyForm.data_type === 'enum'">枚举选项<input v-model="propertyForm.enum_choices" aria-label="属性枚举选项" placeholder="standard,preferred" /></label>
              <label class="check-row"><input v-model="propertyForm.required" type="checkbox" />必填</label>
              <label class="check-row"><input v-model="propertyForm.editable" type="checkbox" />可编辑</label>
              <label class="check-row"><input v-model="propertyForm.unique_value" type="checkbox" />唯一值</label>
              <label class="check-row"><input v-model="propertyForm.sensitive" type="checkbox" aria-label="敏感字段" />敏感字段</label>
              <button class="button button-primary" aria-label="暂存分支修改" :disabled="busy || !selectedBranchCanEdit">暂存修改</button>
            </form>

            <form v-else-if="resourceKind === 'link_type'" class="branch-edit-form" @submit.prevent="stageChange">
              <label>链接操作模式<select v-model="linkMode" aria-label="链接操作模式"><option value="create">新增链接</option><option value="edit">修改现有链接</option></select></label>
              <label v-if="linkMode === 'edit'">选择链接<select v-model="linkEditSelection" aria-label="选择待修改链接" @change="loadLinkForEdit(linkEditSelection)" required><option value="" disabled>选择待修改的链接</option><option v-for="link in selectedBranch?.snapshot.link_types ?? []" :key="link.api_name" :value="link.api_name">{{ link.display_name }} · {{ link.api_name }}</option></select></label>
              <label>链接 API 名称<input v-model="linkForm.api_name" aria-label="链接 API 名称" required pattern="[a-z][a-z0-9_]*" :readonly="linkMode === 'edit'" /></label>
              <label>链接显示名称<input v-model="linkForm.display_name" aria-label="链接显示名称" required /></label>
              <label>链接说明<textarea v-model="linkForm.description" aria-label="链接说明" rows="2" /></label>
              <label v-if="linkMode === 'create'">源对象类型<select v-model="linkForm.source_type_api_name" aria-label="源对象类型" required><option value="" disabled>选择起点</option><option v-for="type in objectTypes" :key="type.api_name" :value="type.api_name">{{ type.display_name }}</option></select></label>
              <label v-else>源对象类型<input v-model="linkForm.source_type_api_name" aria-label="源对象类型" readonly /></label>
              <label v-if="linkMode === 'create'">目标对象类型<select v-model="linkForm.target_type_api_name" aria-label="目标对象类型" required><option value="" disabled>选择终点</option><option v-for="type in objectTypes" :key="type.api_name" :value="type.api_name">{{ type.display_name }}</option></select></label>
              <label v-else>目标对象类型<input v-model="linkForm.target_type_api_name" aria-label="目标对象类型" readonly /></label>
              <button class="button button-primary" aria-label="暂存分支修改" :disabled="busy || !selectedBranchCanEdit">暂存修改</button>
            </form>

            <form v-else class="branch-edit-form" @submit.prevent="stageChange">
              <label>Action 操作模式<select v-model="actionMode" aria-label="Action 操作模式"><option value="create">新增 Action</option><option value="edit">修改现有 Action</option></select></label>
              <label v-if="actionMode === 'edit'">选择 Action<select v-model="actionEditSelection" aria-label="选择待修改 Action" @change="loadActionForEdit(actionEditSelection)" required><option value="" disabled>选择待修改的 Action</option><option v-for="action in selectedBranch?.snapshot.actions ?? []" :key="action.api_name" :value="action.api_name">{{ action.display_name }} · {{ action.api_name }}</option></select></label>
              <label>Action API 名称<input v-model="actionForm.api_name" aria-label="Action API 名称" required pattern="[a-z][a-z0-9_]*" :readonly="actionMode === 'edit'" /></label>
              <label>Action 显示名称<input v-model="actionForm.display_name" aria-label="Action 显示名称" required /></label>
              <label>说明<textarea v-model="actionForm.description" aria-label="Action 说明" rows="2" placeholder="描述动作目的和业务影响" /></label>
              <label v-if="actionMode === 'create'">目标对象类型<select v-model="actionForm.object_type_api_name" aria-label="Action 目标对象类型" required><option value="" disabled>选择对象类型</option><option v-for="type in objectTypes" :key="type.api_name" :value="type.api_name">{{ type.display_name }} · {{ type.api_name }}</option></select></label>
              <label v-else>目标对象类型<input v-model="actionForm.object_type_api_name" aria-label="Action 目标对象类型" readonly /></label>
              <fieldset v-if="selectedActionType" class="action-property-picker"><legend>Action 可修改属性</legend><label v-for="property in selectedActionType.properties.filter((item) => item.editable)" :key="property.api_name" class="check-row"><input v-model="actionForm.allowed_properties" type="checkbox" :value="property.api_name" :aria-label="`Action 可修改属性 ${property.api_name}`" />{{ property.display_name }} · {{ property.api_name }}</label><p v-if="!selectedActionType.properties.some((item) => item.editable)" class="quiet-empty">此对象类型没有可修改属性。</p></fieldset>
              <label>提交条件（JSON）<textarea v-model="actionForm.submission_criteria_json" aria-label="Action 提交条件 JSON" rows="4" placeholder='{"property":"state","operator":"equals","value":"open"}' /></label>
              <label v-if="actionMode === 'edit'">参数 Schema（JSON）<textarea v-model="actionForm.parameters_schema_json" aria-label="Action 参数 Schema JSON" rows="5" /></label>
              <label v-if="actionMode === 'edit'" class="check-row"><input v-model="actionForm.enabled" type="checkbox" aria-label="启用此 Action" />启用此 Action</label>
              <p class="form-help">参数类型和枚举约束从所选属性生成；提交条件使用安全的条件表达式。</p>
              <button class="button button-primary" aria-label="暂存分支修改" :disabled="busy || !selectedBranchCanEdit">暂存修改</button>
            </form>

            <div class="branch-submit-box">
              <label>评审标题<input v-model="proposalTitle" aria-label="评审标题" placeholder="本体变更提案" /></label>
              <button class="button button-secondary" aria-label="提交分支评审" :disabled="busy || !selectedBranchCanEdit || !selectedBranch.changes.length || !selectedBranch.validation.valid" @click="proposeBranch">提交逐资源评审</button>
              <p>评审通过并完成合并后，变更才会进入 main。</p>
            </div>
          </aside>
        </div>
      </section>
      <section v-else class="branch-empty panel">
        <span class="eyebrow">MAIN · v{{ selectedOntology?.revision ?? "—" }}</span>
        <h2>从隔离分支开始建模</h2>
        <p>分支会记录主本体基线。结构修改先在此处检查，再由提案审批后合并。</p>
        <div v-if="loading" class="quiet-empty">正在读取本体与分支…</div>
        <div v-else-if="!ontologies.length" class="quiet-empty">没有可用本体，请先创建一个 Ontology。</div>
      </section>
    </div>
  </div>
</template>
