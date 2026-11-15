<script setup lang="ts">
import { computed, onMounted, ref, watch } from "vue";
import { Background, Controls, MarkerType, MiniMap, VueFlow } from "@xyflow/vue";
import type { Edge, Node, NodeTypesObject, VueFlowInstance, Viewport } from "@xyflow/vue";
import { api, readableError } from "../api/client";
import CanvasActionNode from "../components/ontology/CanvasActionNode.vue";
import CanvasObjectNode from "../components/ontology/CanvasObjectNode.vue";
import CanvasSystemNode from "../components/ontology/CanvasSystemNode.vue";
import { useAuthStore } from "../stores/auth";
import type { DerivedPropertyDefinition, DerivedPropertyPreview, ObjectRecord, Ontology, OntologyBranch, OntologyCanvasResponse } from "../types";
import { canvasLayoutKey, mapCanvasToFlow } from "./ontologyCanvasGraph";
import type { CanvasLayout, OntologyCanvasEdge, OntologyCanvasNode } from "./ontologyCanvasGraph";
import "@xyflow/vue/dist/style.css";

const auth = useAuthStore();
const nodeTypes = { objectType: CanvasObjectNode, sourceSystem: CanvasSystemNode, action: CanvasActionNode } as unknown as NodeTypesObject<OntologyCanvasNode>;
const ontologies = ref<Ontology[]>([]);
const branches = ref<OntologyBranch[]>([]);
const selectedOntologyId = ref("");
const selectedBranchId = ref("");
const canvas = ref<OntologyCanvasResponse | null>(null);
const graphNodes = ref<OntologyCanvasNode[]>([]);
const graphEdges = ref<OntologyCanvasEdge[]>([]);
const loading = ref(false);
const error = ref("");
const resourceQuery = ref("");
const selectedNodeId = ref("");
const selectedEdgeId = ref("");
const selectedDerivedApiName = ref("");
const showSources = ref(true);
const showActions = ref(true);
const showDerived = ref(true);
const activeLayoutKey = ref("");
const activeLayout = ref<CanvasLayout | undefined>();
const flowInstance = ref<VueFlowInstance | null>(null);
const sampleObjects = ref<ObjectRecord[]>([]);
const selectedObjectId = ref("");
const preview = ref<DerivedPropertyPreview | null>(null);
const previewLoading = ref(false);
const previewError = ref("");

const selectedNodeResource = computed(() => canvas.value?.nodes.find((node) => node.id === selectedNodeId.value) ?? null);
const selectedEdgeResource = computed(() => canvas.value?.edges.find((edge) => edge.id === selectedEdgeId.value) ?? null);
const selectedObjectProperties = computed(() => selectedNodeResource.value?.type === "objectType" ? selectedNodeResource.value.data.properties as Array<Record<string, any>> : []);
const selectedDerivedProperty = computed(() => selectedObjectProperties.value.find((property) => property.is_derived && property.api_name === selectedDerivedApiName.value) ?? null);
const selectedDerivedDefinition = computed(() => selectedDerivedProperty.value?.derived_definition as DerivedPropertyDefinition | undefined);
const selectedObjectTypeName = computed(() => selectedNodeResource.value?.type === "objectType" ? String(selectedNodeResource.value.data.api_name) : "");
const allDerivedProperties = computed(() => canvas.value?.nodes
  .filter((node) => node.type === "objectType")
  .flatMap((node) => (node.data.properties as Array<Record<string, any>>)
    .filter((property) => property.is_derived)
    .map((property) => ({
      objectTypeApiName: String(node.data.api_name),
      objectTypeDisplayName: String(node.data.display_name),
      nodeId: node.id,
      property,
    }))) ?? []);
const highlightedLinkApis = computed(() => selectedDerivedDefinition.value?.path.map((step) => step.link_api_name) ?? []);
const visibleFlowNodes = computed<OntologyCanvasNode[]>({
  get() {
    return graphNodes.value
      .filter((node) => (showSources.value || node.type !== "sourceSystem") && (showActions.value || node.type !== "action"))
      .map((node) => node.type === "objectType" ? { ...node, data: { ...node.data, showDerived: showDerived.value } } : node);
  },
  set(nodes: Node[]) {
    const updates = new Map(nodes.map((node) => [node.id, node]));
    graphNodes.value = graphNodes.value.map((node) => updates.has(node.id) ? { ...node, ...updates.get(node.id)! } as OntologyCanvasNode : node);
  },
});
const visibleFlowEdges = computed<OntologyCanvasEdge[]>({
  get() {
    return graphEdges.value.filter((edge) =>
      (showSources.value || edge.data?.canvas_type !== "sourceMapping")
      && (showActions.value || edge.data?.canvas_type !== "actionAssociation"),
    );
  },
  set(edges: Edge[]) {
    const updates = new Map(edges.map((edge) => [edge.id, edge]));
    graphEdges.value = graphEdges.value.map((edge) => updates.has(edge.id) ? { ...edge, ...updates.get(edge.id)! } as OntologyCanvasEdge : edge);
  },
});
const searchableResources = computed(() => (canvas.value?.nodes ?? []).filter((node) => {
  const query = resourceQuery.value.trim().toLocaleLowerCase();
  if (!query) return true;
  return `${node.data.display_name ?? node.data.name ?? ""} ${node.data.api_name ?? ""} ${node.data.connector_type ?? ""}`.toLocaleLowerCase().includes(query);
}));
const layoutPositionMap = computed(() => Object.fromEntries(graphNodes.value.map((node) => [node.id, node.position])));

function readLayout(key: string): CanvasLayout | undefined {
  try {
    const raw = localStorage.getItem(key);
    if (!raw) return undefined;
    const parsed = JSON.parse(raw) as CanvasLayout;
    if (!parsed.nodes || typeof parsed.nodes !== "object") return undefined;
    return parsed;
  } catch {
    return undefined;
  }
}

function persistLayout(viewport?: Viewport) {
  if (!activeLayoutKey.value) return;
  const savedViewport = viewport ?? flowInstance.value?.getViewport() ?? activeLayout.value?.viewport;
  const layout: CanvasLayout = {
    nodes: Object.fromEntries(graphNodes.value.map((node) => [node.id, { x: node.position.x, y: node.position.y }])),
    ...(savedViewport ? { viewport: savedViewport } : {}),
  };
  activeLayout.value = layout;
  try {
    localStorage.setItem(activeLayoutKey.value, JSON.stringify(layout));
  } catch {
    error.value = "浏览器没有可用的本地存储空间，节点布局无法保存。";
  }
}

function rebuildGraph() {
  if (!canvas.value) return;
  const layout = activeLayout.value ?? { nodes: layoutPositionMap.value };
  const graph = mapCanvasToFlow(canvas.value, layout, highlightedLinkApis.value);
  graphNodes.value = graph.nodes;
  graphEdges.value = graph.edges;
}

async function loadCanvas() {
  if (!selectedOntologyId.value) {
    canvas.value = null;
    graphNodes.value = [];
    graphEdges.value = [];
    return;
  }
  loading.value = true;
  error.value = "";
  preview.value = null;
  previewError.value = "";
  try {
    const params: Record<string, string> = { ontology_id: selectedOntologyId.value };
    if (selectedBranchId.value) params.branch_id = selectedBranchId.value;
    const loaded = await api.get<OntologyCanvasResponse>("/api/ontology/canvas", params);
    canvas.value = loaded;
    activeLayoutKey.value = canvasLayoutKey(auth.activeProjectId, selectedOntologyId.value, selectedBranchId.value || "main");
    activeLayout.value = readLayout(activeLayoutKey.value);
    const graph = mapCanvasToFlow(loaded, activeLayout.value);
    graphNodes.value = graph.nodes;
    graphEdges.value = graph.edges;
    selectedNodeId.value = loaded.nodes.find((node) => node.type === "objectType")?.id ?? loaded.nodes[0]?.id ?? "";
    selectedEdgeId.value = "";
    selectedDerivedApiName.value = "";
    sampleObjects.value = [];
    selectedObjectId.value = "";
    if (activeLayout.value?.viewport) {
      requestAnimationFrame(() => void flowInstance.value?.setViewport(activeLayout.value!.viewport!, { duration: 0 }));
    } else {
      requestAnimationFrame(() => void flowInstance.value?.fitView({ padding: 0.2, duration: 0 }));
    }
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function loadWorkspace() {
  loading.value = true;
  error.value = "";
  try {
    ontologies.value = await api.get<Ontology[]>("/api/ontology");
    if (!ontologies.value.some((ontology) => ontology.id === selectedOntologyId.value)) {
      selectedOntologyId.value = ontologies.value[0]?.id ?? "";
    }
    if (!selectedOntologyId.value) {
      branches.value = [];
      canvas.value = null;
      return;
    }
    branches.value = await api.get<OntologyBranch[]>("/api/branches", { ontology_id: selectedOntologyId.value });
    if (!branches.value.some((branch) => branch.id === selectedBranchId.value)) {
      selectedBranchId.value = branches.value.find((branch) => branch.status === "active")?.id ?? "";
    }
    await loadCanvas();
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}

async function changeOntology() {
  selectedBranchId.value = "";
  branches.value = [];
  canvas.value = null;
  try {
    branches.value = await api.get<OntologyBranch[]>("/api/branches", { ontology_id: selectedOntologyId.value });
    selectedBranchId.value = branches.value.find((branch) => branch.status === "active")?.id ?? "";
    await loadCanvas();
  } catch (cause) {
    error.value = readableError(cause);
  }
}

function onFlowInit(instance: VueFlowInstance) {
  flowInstance.value = instance;
}

function selectNode(nodeId: string) {
  selectedNodeId.value = nodeId;
  selectedEdgeId.value = "";
  selectedDerivedApiName.value = "";
  preview.value = null;
  previewError.value = "";
  const node = graphNodes.value.find((item) => item.id === nodeId);
  if (node) void flowInstance.value?.setCenter(node.position.x + 125, node.position.y + 90, { zoom: 1, duration: 250 });
}

function onNodeClick(event: { node: Node }) {
  selectedNodeId.value = event.node.id;
  selectedEdgeId.value = "";
  selectedDerivedApiName.value = "";
  preview.value = null;
  previewError.value = "";
}

function onEdgeClick(event: { edge: Edge }) {
  selectedEdgeId.value = event.edge.id;
  selectedNodeId.value = "";
  selectedDerivedApiName.value = "";
  preview.value = null;
}

function selectDerivedProperty(nodeId: string, apiName: string) {
  const node = canvas.value?.nodes.find((item) => item.id === nodeId);
  if (node) selectedNodeId.value = node.id;
  selectedEdgeId.value = "";
  selectedDerivedApiName.value = apiName;
  const graph = mapCanvasToFlow(canvas.value!, { nodes: layoutPositionMap.value, viewport: activeLayout.value?.viewport }, highlightedLinkApis.value);
  graphNodes.value = graph.nodes;
  graphEdges.value = graph.edges;
  preview.value = null;
  previewError.value = "";
  sampleObjects.value = [];
  selectedObjectId.value = "";
  void loadSampleObjects(nodeId);
}

async function loadSampleObjects(nodeId: string) {
  const node = canvas.value?.nodes.find((item) => item.id === nodeId);
  const apiName = String(node?.data.api_name ?? "");
  if (!apiName || !canvas.value) return;
  try {
    const response = await api.get<{ items: ObjectRecord[] }>("/api/objects", {
      ontology_id: canvas.value.ontology.id,
      object_type_api_name: apiName,
      page: 1,
      page_size: 25,
    });
    sampleObjects.value = response.items;
    selectedObjectId.value = response.items[0]?.id ?? "";
  } catch (cause) {
    previewError.value = readableError(cause);
  }
}

async function runDerivedPreview() {
  if (!canvas.value || !selectedObjectId.value || !selectedDerivedDefinition.value) return;
  previewLoading.value = true;
  previewError.value = "";
  try {
    preview.value = await api.post<DerivedPropertyPreview>("/api/derived-properties/preview", {
      ontology_id: canvas.value.ontology.id,
      ...(selectedBranchId.value ? { branch_id: selectedBranchId.value } : {}),
      object_id: selectedObjectId.value,
      definition: selectedDerivedDefinition.value,
    });
  } catch (cause) {
    previewError.value = readableError(cause);
    preview.value = null;
  } finally {
    previewLoading.value = false;
  }
}

function resetLayout() {
  if (activeLayoutKey.value) localStorage.removeItem(activeLayoutKey.value);
  activeLayout.value = undefined;
  rebuildGraph();
  void flowInstance.value?.fitView({ padding: 0.2, duration: 250 });
  persistLayout();
}

function onMoveEnd(payload: { viewport?: Viewport }) {
  persistLayout(payload.viewport);
}

function onNodeDragStop() {
  persistLayout();
}

function edgeResourceName() {
  const edge = selectedEdgeResource.value;
  return String(edge?.data.display_name ?? edge?.data.api_name ?? "关系");
}

watch(highlightedLinkApis, () => {
  if (!canvas.value) return;
  const graph = mapCanvasToFlow(canvas.value, { nodes: layoutPositionMap.value, viewport: activeLayout.value?.viewport }, highlightedLinkApis.value);
  graphNodes.value = graph.nodes;
  graphEdges.value = graph.edges;
}, { deep: true });
watch(() => auth.activeProjectId, () => void loadWorkspace());
onMounted(loadWorkspace);
</script>

<template>
  <div class="page-content ontology-canvas-page">
    <header class="canvas-page-heading">
      <div><span class="eyebrow">本体 · 关系、来源与推理</span><h1>本体关系画布</h1><p>从真实对象类型、链接、系统映射与 Action 浏览语义结构；选择派生属性可检查路径并运行只读试算。</p></div>
      <div class="canvas-heading-actions"><span v-if="canvas" class="revision-pill">{{ canvas.ontology.display_name }} · v{{ canvas.ontology.revision }}</span><RouterLink class="button button-secondary" to="/branches">管理分支与定义</RouterLink></div>
    </header>

    <section class="canvas-toolbar panel" aria-label="画布范围与图层">
      <label>本体<select v-model="selectedOntologyId" aria-label="选择画布本体" @change="changeOntology"><option v-for="ontology in ontologies" :key="ontology.id" :value="ontology.id">{{ ontology.display_name }} · {{ ontology.api_name }}</option></select></label>
      <label>分支<select v-model="selectedBranchId" aria-label="选择本体分支" @change="loadCanvas"><option value="">main</option><option v-for="branch in branches" :key="branch.id" :value="branch.id">{{ branch.name }} · {{ branch.status === "active" ? "编辑中" : branch.status }}</option></select></label>
      <div class="canvas-layer-toggles"><span>图层</span><label><input v-model="showSources" type="checkbox" />来源系统</label><label><input v-model="showActions" type="checkbox" />Action</label><label><input v-model="showDerived" type="checkbox" />派生属性</label></div>
      <button class="button button-quiet" data-action="reset-canvas-layout" @click="resetLayout">重置布局</button>
      <span class="canvas-save-state"><i />布局保存在此浏览器</span>
    </section>

    <div v-if="error" class="notice notice-error" role="alert">{{ error }}</div>
    <div v-if="loading" class="canvas-loading" role="status">正在加载项目本体结构与来源映射…</div>
    <div v-else-if="canvas" class="ontology-canvas-layout">
      <aside class="canvas-resource-rail panel">
        <header><div><span class="eyebrow">当前图谱</span><h2>{{ canvas.nodes.length }} 个资源</h2></div><span class="canvas-count-badge">{{ canvas.edges.length }} 关系</span></header>
        <label class="canvas-search">查找资源<input v-model="resourceQuery" aria-label="搜索画布资源" placeholder="名称或 API 名称" /></label>
        <div class="canvas-resource-groups">
          <section><h3>对象类型 <span>{{ canvas.nodes.filter((node) => node.type === 'objectType').length }}</span></h3>
            <button v-for="node in searchableResources.filter((item) => item.type === 'objectType')" :key="node.id" class="canvas-resource-item" :class="{ selected: selectedNodeId === node.id }" @click="selectNode(node.id)"><span class="canvas-resource-glyph object">◈</span><span><strong>{{ node.data.display_name }}</strong><code>{{ node.data.api_name }}</code></span><b>{{ node.data.properties?.length ?? 0 }}</b></button>
          </section>
          <section v-if="showSources"><h3>来源系统 <span>{{ canvas.nodes.filter((node) => node.type === 'sourceSystem').length }}</span></h3>
            <button v-for="node in searchableResources.filter((item) => item.type === 'sourceSystem')" :key="node.id" class="canvas-resource-item" :class="{ selected: selectedNodeId === node.id }" @click="selectNode(node.id)"><span class="canvas-resource-glyph source">⇢</span><span><strong>{{ node.data.name }}</strong><code>{{ node.data.connector_type }}</code></span><b>{{ node.data.mapping_count }}</b></button>
          </section>
          <section v-if="showActions"><h3>Actions <span>{{ canvas.nodes.filter((node) => node.type === 'action').length }}</span></h3>
            <button v-for="node in searchableResources.filter((item) => item.type === 'action')" :key="node.id" class="canvas-resource-item" :class="{ selected: selectedNodeId === node.id }" @click="selectNode(node.id)"><span class="canvas-resource-glyph action">↗</span><span><strong>{{ node.data.display_name }}</strong><code>{{ node.data.api_name }}</code></span><i :class="node.data.enabled ? 'is-enabled' : 'is-disabled'" /></button>
          </section>
        </div>
        <p v-if="!canvas.nodes.length" class="canvas-empty-note">当前本体还没有定义对象类型。可从“本体资源”或“分支管理”创建。</p>
      </aside>

      <main class="canvas-graph-stage" aria-label="本体关系图画布">
        <div v-if="!graphNodes.length" class="canvas-empty-stage"><span>◇</span><strong>等待本体资源</strong><p>创建对象类型与链接后，关系图会在这里呈现。</p></div>
        <VueFlow
          v-else
          v-model:nodes="visibleFlowNodes"
          v-model:edges="visibleFlowEdges"
          :node-types="nodeTypes"
          :default-viewport="activeLayout?.viewport"
          :fit-view-on-init="!activeLayout?.viewport"
          :min-zoom="0.2"
          :max-zoom="2.2"
          :selection-on-drag="true"
          :pan-on-drag="[1, 2]"
          :zoom-on-scroll="true"
          :nodes-connectable="false"
          :edges-updatable="false"
          :delete-key-code="null"
          :default-edge-options="{ type: 'smoothstep', markerEnd: MarkerType.ArrowClosed }"
          @init="onFlowInit"
          @node-click="onNodeClick"
          @edge-click="onEdgeClick"
          @node-drag-stop="onNodeDragStop"
          @move-end="onMoveEnd"
        >
          <Background variant="dots" :gap="18" :size="1" color="#cbd8d1" />
          <Controls position="bottom-left" />
          <MiniMap position="bottom-right" pannable zoomable node-color="#5e8a75" mask-color="rgba(235, 241, 237, .72)" />
          <div class="canvas-stage-legend"><span><i class="legend-object" />对象类型</span><span><i class="legend-link" />本体链接</span><span><i class="legend-source" />系统映射</span><span><i class="legend-derived" />派生路径</span></div>
          <div class="canvas-stage-branch">{{ canvas.branch?.name ?? "main" }} <span>只读图层</span></div>
        </VueFlow>
      </main>

      <aside class="canvas-inspector panel">
        <header><div><span class="eyebrow">资源检查器</span><h2>{{ selectedEdgeResource ? edgeResourceName() : selectedNodeResource?.data.display_name ?? selectedNodeResource?.data.name ?? selectedNodeResource?.data.api_name ?? "选择资源" }}</h2></div><span v-if="selectedNodeResource" class="canvas-inspector-kind">{{ selectedNodeResource.type === "objectType" ? "对象类型" : selectedNodeResource.type === "sourceSystem" ? "来源系统" : "Action" }}</span></header>
        <template v-if="selectedNodeResource?.type === 'objectType'">
          <p class="canvas-inspector-api">{{ selectedNodeResource.data.api_name }}</p>
          <p class="canvas-inspector-description">{{ selectedNodeResource.data.description || "暂无语义说明。" }}</p>
          <div class="canvas-inspector-meta"><span>原生属性<strong>{{ selectedObjectProperties.filter((property) => !property.is_derived).length }}</strong></span><span>派生属性<strong>{{ selectedObjectProperties.filter((property) => property.is_derived).length }}</strong></span><span>关联 Action<strong>{{ selectedNodeResource.data.actions?.length ?? 0 }}</strong></span></div>
          <section class="inspector-property-section"><h3>属性与派生值</h3>
            <button v-for="property in selectedObjectProperties" :key="property.api_name" class="inspector-property-row" :class="{ 'is-derived': property.is_derived }" :data-derived-property="property.is_derived ? property.api_name : undefined" @click="property.is_derived && selectDerivedProperty(selectedNodeResource!.id, property.api_name)"><span><i>{{ property.is_derived ? "ƒ" : "◻" }}</i><strong>{{ property.display_name }}</strong><code>{{ property.api_name }}</code></span><b>{{ property.data_type }}</b><small v-if="property.is_derived">查看路径并试算</small><small v-else-if="property.sensitive">敏感</small></button>
          </section>
          <section v-if="selectedNodeResource.data.actions?.length" class="inspector-property-section"><h3>关联 Actions</h3><p v-for="action in selectedNodeResource.data.actions" :key="action" class="inspector-action-row">↗ <code>{{ action }}</code></p></section>
          <section v-if="showSources" class="inspector-property-section"><h3>来源映射</h3><p v-for="edge in canvas.edges.filter((item) => item.type === 'sourceMapping' && item.target === selectedNodeResource!.id)" :key="edge.id" class="inspector-action-row">⇢ <code>{{ canvas.nodes.find((node) => node.id === edge.source)?.data.name }}</code><small>{{ edge.data.mapped_property_count }} 字段</small></p><p v-if="!canvas.edges.some((item) => item.type === 'sourceMapping' && item.target === selectedNodeResource!.id)" class="canvas-empty-note">尚无来源映射</p></section>
        </template>
        <template v-else-if="selectedNodeResource?.type === 'sourceSystem'">
          <p class="canvas-inspector-api">{{ selectedNodeResource.data.connector_type }} · {{ selectedNodeResource.data.status }}</p><p class="canvas-inspector-description">数据连接通过字段映射进入本体对象类型；映射线来自当前本体的数据连接配置。</p>
          <section class="inspector-property-section"><h3>已映射对象类型</h3><p v-for="edge in canvas.edges.filter((item) => item.type === 'sourceMapping' && item.source === selectedNodeResource!.id)" :key="edge.id" class="inspector-action-row">→ <code>{{ edge.data.object_type_api_name }}</code><small>{{ edge.data.mapped_property_count }} 字段</small></p><p v-if="!selectedNodeResource.data.mapping_count" class="canvas-empty-note">此来源系统还没有对象映射。</p></section>
        </template>
        <template v-else-if="selectedNodeResource?.type === 'action'">
          <p class="canvas-inspector-api">{{ selectedNodeResource.data.api_name }}</p><p class="canvas-inspector-description">关联对象：{{ selectedNodeResource.data.object_type_api_name }} · {{ selectedNodeResource.data.enabled ? "已启用" : "已停用" }}</p><p class="canvas-boundary-note">画布展示 Action 关联，不在此处执行写入操作。</p>
        </template>
        <template v-else-if="selectedEdgeResource">
          <p class="canvas-inspector-api">{{ selectedEdgeResource.data.api_name ?? selectedEdgeResource.id }}</p><p class="canvas-inspector-description">{{ selectedEdgeResource.data.description || "该关系由当前本体资源定义生成。" }}</p>
          <dl class="canvas-edge-details"><dt>关系类型</dt><dd>{{ selectedEdgeResource.type === "ontologyLink" ? "本体链接" : selectedEdgeResource.type === "sourceMapping" ? "来源字段映射" : "Action 关联" }}</dd><dt>起点</dt><dd>{{ selectedEdgeResource.source }}</dd><dt>终点</dt><dd>{{ selectedEdgeResource.target }}</dd><template v-if="selectedEdgeResource.type === 'ontologyLink'"><dt>起点基数</dt><dd>{{ selectedEdgeResource.data.source_cardinality }}</dd><dt>终点基数</dt><dd>{{ selectedEdgeResource.data.target_cardinality }}</dd></template></dl>
        </template>
        <div v-else class="canvas-inspector-empty"><span>◇</span><strong>选择对象或关系</strong><p>检查器会显示本体元数据、来源映射和派生属性路径。</p></div>
      </aside>
    </div>

    <section class="derived-preview-tray panel">
      <header><div><span class="eyebrow">运行时推理 · 只读试算</span><h2>派生属性路径与计算结果</h2><p>选择一个派生属性，指定起始对象；服务端沿定义的链接实时读取并返回可见路径。</p></div><span class="derived-hop-limit">最多 3 跳</span></header>
      <div v-if="selectedDerivedDefinition" class="derived-preview-workspace">
        <div class="derived-preview-definition"><span class="derived-preview-glyph">ƒ</span><div><strong>{{ selectedDerivedProperty?.display_name }}</strong><code>{{ selectedObjectTypeName }}.{{ selectedDerivedProperty?.api_name }}</code><small>{{ selectedDerivedDefinition.path.map((step) => `${step.direction === 'outgoing' ? '→' : '←'} ${step.link_api_name}`).join('  /  ') }} · {{ selectedDerivedDefinition.aggregation || "单值" }} · {{ selectedDerivedProperty?.data_type }}</small></div></div>
        <label>试算起点<select v-model="selectedObjectId" aria-label="选择派生属性试算对象"><option value="" disabled>{{ sampleObjects.length ? "选择对象记录" : "此类型暂无对象记录" }}</option><option v-for="record in sampleObjects" :key="record.id" :value="record.id">{{ record.primary_key_value }} · {{ String(record.properties[selectedNodeResource?.data.title_key_property ?? ''] ?? record.primary_key_value) }}</option></select></label>
        <button class="button button-primary" data-action="run-derived-preview" :disabled="previewLoading || !selectedObjectId" @click="runDerivedPreview">{{ previewLoading ? "试算中…" : "运行试算" }}</button>
        <button class="button button-quiet" data-action="reselect-derived" @click="selectDerivedProperty(selectedNodeResource!.id, selectedDerivedProperty!.api_name)">刷新起点记录</button>
        <p v-if="previewError" class="global-search-error" role="alert">{{ previewError }}</p>
        <div v-if="preview" class="derived-preview-result"><div class="derived-result-value"><span>计算结果</span><strong>{{ JSON.stringify(preview.value) }}</strong></div><div class="derived-result-facts"><span>有效值 <b>{{ preview.matched_count }}</b></span><span>路径终点 <b>{{ preview.path_object_count }}</b></span><span>空值跳过 <b>{{ preview.ignored_null_count }}</b></span></div><div v-if="preview.warnings.length" class="derived-preview-warnings"><p v-for="warning in preview.warnings" :key="warning">{{ warning }}</p></div><ol class="derived-trace-list"><li v-for="(step, index) in preview.trace" :key="`${index}-${step.link_api_name ?? step.object_id}`"><span class="trace-step-number">{{ String(index + 1).padStart(2, '0') }}</span><span v-if="step.link_api_name"><strong>{{ step.direction === 'outgoing' ? '沿出向链接' : '沿入向链接' }} {{ step.link_api_name }}</strong><code>{{ step.from_object_id }} → {{ step.to_object_id }}</code></span><span v-else><strong>读取终点字段 {{ step.property_api_name }}</strong><code>{{ step.object_id }} · {{ JSON.stringify(step.value) }}</code></span></li></ol></div>
      </div>
      <div v-else class="derived-preview-empty"><strong>从检查器选择派生属性</strong><span>本体级派生定义以原生属性为终点，试算返回结果、聚合计数、空值提示与每条可见对象链接。</span><div class="derived-quick-picks"><button v-for="item in allDerivedProperties" :key="`${item.nodeId}:${item.property.api_name}`" @click="selectDerivedProperty(item.nodeId, item.property.api_name)"><i>ƒ</i><span><strong>{{ item.property.display_name }}</strong><small>{{ item.objectTypeDisplayName }} · {{ item.property.api_name }}</small></span><b>试算 →</b></button><p v-if="!allDerivedProperties.length">当前图谱还没有已发布或分支内的派生属性，可到“分支管理”创建。</p></div></div>
    </section>
  </div>
</template>
