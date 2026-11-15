<script setup lang="ts">
import { computed, nextTick, onMounted, ref, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { api } from "../api/client";
import { useAuthStore } from "../stores/auth";
import type { ProjectSummary } from "../stores/auth";
import type { ActionDefinition, AgentDefinition, AgentSession, LinkType, ObjectRecord, ObjectType, Ontology, Proposal } from "../types";

const route = useRoute();
const router = useRouter();
const auth = useAuthStore();
const revision = ref(1);
const projectLoading = ref(true);
const projectReady = ref(false);
const projectError = ref("");
const projectDialogOpen = ref(false);
const projectSaving = ref(false);
const projectSaveError = ref("");
const projectForm = ref({ api_name: "", display_name: "", description: "" });
const memberDialogOpen = ref(false);
const memberSaving = ref(false);
const memberError = ref("");
const memberNotice = ref("");
const projectMembers = ref<Array<{ id: string; user_id: string; email: string; role: "admin" | "editor" | "viewer" }>>([]);
const memberForm = ref({ email: "", role: "editor" as "admin" | "editor" | "viewer" });
const searchOpen = ref(false);
const searchQuery = ref("");
const searchResults = ref<Array<{ key: string; kind: string; title: string; subtitle: string; to: string }>>([]);
const searchLoading = ref(false);
const searchError = ref("");
const activeSearchResult = ref(0);
const hasSearched = ref(false);
const searchHint = computed(() => searchQuery.value.trim().length < 2 ? "输入至少两个字符搜索工作区资源" : "按 Enter 搜索；方向键选择，Escape 关闭");
const navigationSections = [
  { heading: "工作区", items: [{ label: "发现与总览", to: "/", icon: "⌂" }] },
  {
    heading: "本体管理",
    items: [
      { label: "本体画布", to: "/ontology/canvas", icon: "⌘" },
      { label: "本体资源", to: "/ontology", icon: "◇" },
      { label: "对象浏览", to: "/objects", icon: "▦" },
      { label: "分支管理", to: "/branches", icon: "⌘" },
      { label: "数据源与映射", to: "/data-sources", icon: "⇢" },
      { label: "变更评审", to: "/proposals", icon: "⇄" },
    ],
  },
  { heading: "智能体管理", items: [
    { label: "智能体管理", to: "/agents", icon: "◉" },
    { label: "智能体构建器", to: "/agent-builder/new", icon: "⌘" },
    { label: "运行会话", to: "/sessions", icon: "▤" },
  ] },
  { heading: "治理与审计", items: [{ label: "审计记录", to: "/audit", icon: "≡" }] },
];
const titles: Record<string, string> = {
  overview: "工作区总览",
  ontology: "本体结构",
  "ontology-canvas": "本体关系画布",
  objects: "对象数据",
  proposals: "变更提案",
  branches: "本体分支",
  "data-sources": "数据源与映射",
  agents: "智能体管理",
  "agent-builder": "智能体构建器",
  sessions: "运行会话",
  "session-detail": "会话检查器",
  audit: "审计记录",
};

function signOut() {
  auth.clearSession();
  router.push({ name: "login" });
}

async function openGlobalSearch() {
  searchOpen.value = true;
  searchQuery.value = "";
  searchResults.value = [];
  searchError.value = "";
  hasSearched.value = false;
  activeSearchResult.value = 0;
  await nextTick();
  document.querySelector<HTMLInputElement>("[aria-label='全局搜索']")?.focus();
}

function closeGlobalSearch() {
  searchOpen.value = false;
}

function fulfilled<T>(result: PromiseSettledResult<T>, fallback: T): T {
  return result.status === "fulfilled" ? result.value : fallback;
}

async function loadRevision() {
  try {
    const ontologies = await api.get<Ontology[]>("/api/ontology");
    revision.value = ontologies[0]?.revision ?? 1;
  } catch {
    revision.value = 1;
  }
}

async function loadProjectContext() {
  projectLoading.value = true;
  projectError.value = "";
  try {
    const projects = await api.get<ProjectSummary[]>("/api/projects");
    auth.setProjects(projects);
    if (!projects.length) {
      projectError.value = "当前账号尚未加入项目，请联系项目管理员。";
      return;
    }
    projectReady.value = Boolean(auth.activeProjectId);
    await loadRevision();
  } catch (cause) {
    projectError.value = cause instanceof Error ? cause.message : "项目列表暂时无法加载。";
  } finally {
    projectLoading.value = false;
  }
}

function changeProject() {
  auth.setActiveProjectId(auth.activeProjectId);
}

function openProjectDialog() {
  projectForm.value = { api_name: "", display_name: "", description: "" };
  projectSaveError.value = "";
  projectDialogOpen.value = true;
}

async function createProject() {
  if (projectSaving.value) return;
  projectSaving.value = true;
  projectSaveError.value = "";
  try {
    const project = await api.post<ProjectSummary>("/api/projects", projectForm.value);
    auth.setProjects([...auth.projects, project]);
    auth.setActiveProjectId(project.id);
    projectReady.value = true;
    projectDialogOpen.value = false;
    await loadRevision();
  } catch (cause) {
    projectSaveError.value = cause instanceof Error ? cause.message : "项目创建失败，请检查输入后重试。";
  } finally {
    projectSaving.value = false;
  }
}

async function openMemberDialog() {
  memberDialogOpen.value = true;
  memberError.value = "";
  memberNotice.value = "";
  memberForm.value = { email: "", role: "editor" };
  await loadProjectMembers();
}

async function loadProjectMembers() {
  if (!auth.activeProjectId) return;
  try {
    projectMembers.value = await api.get<typeof projectMembers.value>(`/api/projects/${auth.activeProjectId}/members`);
  } catch (cause) {
    memberError.value = cause instanceof Error ? cause.message : "成员列表暂时无法加载。";
  }
}

async function saveProjectMember() {
  if (memberSaving.value || !auth.activeProjectId) return;
  memberSaving.value = true;
  memberError.value = "";
  memberNotice.value = "";
  try {
    const member = await api.put<typeof projectMembers.value[number]>(
      `/api/projects/${auth.activeProjectId}/members`,
      { ...memberForm.value },
    );
    const existingIndex = projectMembers.value.findIndex((item) => item.user_id === member.user_id);
    if (existingIndex < 0) projectMembers.value.push(member);
    else projectMembers.value.splice(existingIndex, 1, member);
    memberForm.value.email = "";
    memberNotice.value = "项目成员角色已保存。只有已注册账号可以加入项目。";
  } catch (cause) {
    memberError.value = cause instanceof Error ? cause.message : "成员角色更新失败。";
  } finally {
    memberSaving.value = false;
  }
}

async function runGlobalSearch() {
  const query = searchQuery.value.trim();
  if (query.length < 2) return;
  searchLoading.value = true;
  searchError.value = "";
  hasSearched.value = true;
  try {
    const ontologies = await api.get<Ontology[]>("/api/ontology");
    const ontology = ontologies[0];
    if (!ontology) {
      searchResults.value = [];
      return;
    }
    const [typesResponse, linksResponse, actionsResponse, objectsResponse, sourcesResponse, proposalsResponse, agentsResponse, sessionsResponse] = await Promise.allSettled([
      api.get<ObjectType[]>("/api/object-types", { ontology_id: ontology.id }),
      api.get<LinkType[]>("/api/link-types", { ontology_id: ontology.id }),
      api.get<ActionDefinition[]>("/api/actions", { ontology_id: ontology.id }),
      api.get<{ items: ObjectRecord[] }>("/api/objects", { ontology_id: ontology.id, query, page: 1, page_size: 8 }),
      api.get<Array<{ id: string; name: string; connector_type: string }>>("/api/data-sources", { ontology_id: ontology.id }),
      api.get<Proposal[]>("/api/proposals", { ontology_id: ontology.id }),
      api.get<AgentDefinition[]>("/api/agents", undefined, "/agent-api"),
      api.get<{ items: AgentSession[] }>("/api/sessions", { query, page: 1, page_size: 8 }, "/agent-api"),
    ]);
    const types = fulfilled(typesResponse, []);
    const links = fulfilled(linksResponse, []);
    const actions = fulfilled(actionsResponse, []);
    const objects = fulfilled(objectsResponse, { items: [] }).items;
    const sources = fulfilled(sourcesResponse, []);
    const proposals = fulfilled(proposalsResponse, []);
    const agents = fulfilled(agentsResponse, []);
    const sessions = fulfilled(sessionsResponse, { items: [] }).items;
    const lower = query.toLocaleLowerCase();
    const typeById = new Map(types.map((item) => [item.id, item.api_name]));
    const matches = (value: string | null | undefined) => (value ?? "").toLocaleLowerCase().includes(lower);
    const results = [
      ...types.filter((item) => matches(`${item.display_name} ${item.plural_display_name || ""} ${item.api_name} ${item.description} ${item.aliases?.join(" ") || ""} ${item.groups?.join(" ") || ""}`)).map((item) => ({ key: `object_type:${item.api_name}`, kind: "对象类型", title: item.display_name, subtitle: `对象类型 · ${item.api_name}`, to: `/ontology?type=${encodeURIComponent(item.api_name)}` })),
      ...links.filter((item) => matches(`${item.display_name} ${item.api_name} ${item.description}`)).map((item) => ({ key: `link_type:${item.api_name}`, kind: "链接类型", title: item.display_name, subtitle: `链接 · ${typeById.get(item.source_type_id) ?? "?"} → ${typeById.get(item.target_type_id) ?? "?"}`, to: `/ontology?type=${encodeURIComponent(typeById.get(item.source_type_id) ?? "")}&tab=links` })),
      ...actions.filter((item) => matches(`${item.display_name} ${item.api_name} ${item.description}`)).map((item) => ({ key: `action:${item.api_name}`, kind: "Action", title: item.display_name, subtitle: `Action · ${item.api_name}`, to: `/ontology?type=${encodeURIComponent(item.object_type_api_name)}&tab=actions` })),
      ...objects.map((item) => ({ key: `object:${item.id}`, kind: "对象", title: String(item.properties.name ?? item.primary_key_value), subtitle: `${item.object_type_display_name} · ${item.primary_key_value}`, to: `/objects?type=${encodeURIComponent(item.object_type_api_name)}&query=${encodeURIComponent(query)}&record=${encodeURIComponent(item.id)}` })),
      ...sources.filter((item) => matches(`${item.name} ${item.connector_type}`)).map((item) => ({ key: `data_source:${item.id}`, kind: "数据源", title: item.name, subtitle: `数据源 · ${item.connector_type}`, to: "/data-sources" })),
      ...proposals.filter((item) => matches(`${item.title} ${item.description}`)).map((item) => ({ key: `proposal:${item.id}`, kind: "变更提案", title: item.title, subtitle: `提案 · ${item.status}`, to: "/proposals" })),
      ...agents.filter((item) => matches(`${item.display_name} ${item.api_name} ${item.description}`)).map((item) => ({ key: `agent:${item.id}`, kind: "Agent", title: item.display_name, subtitle: `Agent · ${item.api_name}`, to: `/agent-builder/${item.id}` })),
      ...sessions.filter((item) => matches(`${item.agent_id} ${item.origin_resource} ${item.version_number}`)).map((item) => ({ key: `session:${item.id}`, kind: "Agent 会话", title: `Agent 会话 · ${item.agent_id}`, subtitle: `${item.origin_resource} · 版本 ${item.version_number}`, to: `/sessions/${item.id}` })),
    ];
    searchResults.value = results.slice(0, 24);
    activeSearchResult.value = 0;
  } catch {
    searchError.value = "全局搜索暂不可用，请检查本体服务连接后重试。";
  } finally {
    searchLoading.value = false;
  }
}

function navigateSearchResult(path: string) {
  closeGlobalSearch();
  void router.push(path);
}

function handleSearchKeydown(event: KeyboardEvent) {
  if (event.key === "Escape") {
    closeGlobalSearch();
  } else if (event.key === "ArrowDown" && searchResults.value.length) {
    event.preventDefault();
    activeSearchResult.value = (activeSearchResult.value + 1) % searchResults.value.length;
  } else if (event.key === "ArrowUp" && searchResults.value.length) {
    event.preventDefault();
    activeSearchResult.value = (activeSearchResult.value + searchResults.value.length - 1) % searchResults.value.length;
  } else if (event.key === "Enter" && hasSearched.value && searchResults.value[activeSearchResult.value]) {
    event.preventDefault();
    navigateSearchResult(searchResults.value[activeSearchResult.value].to);
  }
}

watch(() => auth.activeProjectId, () => {
  if (projectReady.value) void loadRevision();
});

onMounted(loadProjectContext);
</script>

<template>
  <div class="studio-shell" @keydown.ctrl.k.window.prevent="openGlobalSearch">
    <aside class="sidebar">
      <div class="brand-lockup"><span class="brand-mark">O</span><span>本体工作台<small>Ontology Studio</small></span></div>
      <div class="workspace-switch"><span class="workspace-dot" /><div><strong>运营知识图谱</strong><small>主本体 · 本地工作区</small></div><span class="switch-chevron">⌄</span></div>
      <nav class="main-nav" aria-label="主导航">
        <section v-for="section in navigationSections" :key="section.heading" class="nav-section">
          <span class="nav-heading">{{ section.heading }}</span>
          <RouterLink v-for="item in section.items" :key="item.to" :to="item.to" class="nav-link" :class="{ active: route.path === item.to || item.to !== '/' && route.path.startsWith(item.to) }">
            <span class="nav-icon">{{ item.icon }}</span>{{ item.label }}
          </RouterLink>
        </section>
      </nav>
      <div class="sidebar-bottom"><span class="connection-dot" />服务已连接<span class="version-label">v0.1</span></div>
    </aside>
    <main class="workspace-main">
      <header class="topbar">
        <div class="breadcrumbs"><span>{{ auth.activeProject?.display_name || "项目" }}</span><span class="crumb-divider">/</span><strong>{{ titles[String(route.name)] || "工作区" }}</strong></div>
        <div class="topbar-actions"><label class="project-context-label">项目<select v-model="auth.activeProjectId" aria-label="切换项目" :disabled="projectLoading || auth.projects.length < 2" @change="changeProject"><option v-for="project in auth.projects" :key="project.id" :value="project.id">{{ project.display_name }}</option></select></label><button v-if="auth.user?.role === 'admin'" class="button button-secondary project-create-trigger" data-action="create-project" @click="openProjectDialog">新建项目</button><button v-if="auth.role === 'admin'" class="button button-quiet project-create-trigger" data-action="manage-project-members" @click="openMemberDialog">项目成员</button><button class="global-search-trigger" data-action="open-global-search" aria-label="打开全局搜索" @click="openGlobalSearch"><span>⌕</span>搜索对象、类型、Action 或 Agent<kbd>Ctrl K</kbd></button><span class="revision-pill">结构版本 <b>v{{ revision }}</b></span><span class="user-chip"><span class="avatar">{{ auth.user?.email.slice(0, 1).toUpperCase() || "U" }}</span>{{ auth.user?.email }}<em>{{ auth.role }}</em></span><button class="logout-button" @click="signOut">退出</button></div>
      </header>
      <section class="page-frame">
        <div v-if="projectLoading" class="project-loading" role="status">正在加载可访问的项目…</div>
        <div v-else-if="projectError" class="notice notice-error" role="alert">{{ projectError }}</div>
        <RouterView v-else-if="projectReady" :key="auth.activeProjectId" />
      </section>
    </main>
    <div v-if="searchOpen" class="global-search-backdrop" @click.self="closeGlobalSearch">
      <section class="global-search-dialog" role="dialog" aria-modal="true" aria-labelledby="global-search-title" @keydown="handleSearchKeydown">
        <header><div><span class="eyebrow">工作区搜索</span><h2 id="global-search-title">查找本体与运行资源</h2></div><button class="search-close-button" aria-label="关闭搜索" @click="closeGlobalSearch">Esc</button></header>
        <form class="global-search-form" @submit.prevent="runGlobalSearch"><span>⌕</span><input v-model="searchQuery" aria-label="全局搜索" autocomplete="off" placeholder="搜索对象类型、记录、Action、提案、Agent…" @keydown="handleSearchKeydown" /><button type="button" class="button button-primary" data-action="run-global-search" :disabled="searchLoading || searchQuery.trim().length < 2" @click="runGlobalSearch">{{ searchLoading ? "搜索中…" : "搜索" }}</button></form>
        <p v-if="searchError" class="global-search-error" role="alert">{{ searchError }}</p>
        <div v-if="searchResults.length" class="global-search-results" role="listbox" aria-label="搜索结果">
          <button v-for="(result, index) in searchResults" :key="result.key" class="global-search-result" :class="{ selected: index === activeSearchResult }" :data-result="result.key" role="option" :aria-selected="index === activeSearchResult" @mouseenter="activeSearchResult = index" @click="navigateSearchResult(result.to)"><span class="search-result-kind">{{ result.kind }}</span><span class="search-result-copy"><strong>{{ result.title }}</strong><small>{{ result.subtitle }}</small></span><span class="search-result-arrow">↗</span></button>
        </div>
        <div v-else-if="hasSearched && !searchLoading && !searchError" class="global-search-empty"><strong>没有找到匹配项</strong><span>尝试对象显示名称、API 名称或关键字。</span></div>
        <div v-else class="global-search-empty"><strong>搜索范围</strong><span>{{ searchHint }}。只会返回当前账号有权访问的资源。</span></div>
        <footer><span><kbd>↑</kbd><kbd>↓</kbd> 选择结果</span><span><kbd>Enter</kbd> 打开 · <kbd>Esc</kbd> 关闭</span></footer>
      </section>
    </div>
    <div v-if="projectDialogOpen" class="global-search-backdrop" @click.self="projectDialogOpen = false">
      <section class="project-create-dialog" role="dialog" aria-modal="true" aria-labelledby="project-create-title">
        <header><div><span class="eyebrow">项目管理</span><h2 id="project-create-title">创建工作区项目</h2></div><button class="search-close-button" aria-label="关闭项目创建" @click="projectDialogOpen = false">关闭</button></header>
        <form class="project-create-form" @submit.prevent="createProject">
          <label>显示名称<input v-model="projectForm.display_name" aria-label="项目显示名称" required minlength="2" maxlength="160" placeholder="例如：供应链本体" /></label>
          <label>API 名称<input v-model="projectForm.api_name" aria-label="项目 API 名称" required minlength="2" maxlength="80" pattern="[a-z][a-z0-9_]*" placeholder="例如：supply_chain" /></label>
          <label>项目说明<textarea v-model="projectForm.description" aria-label="项目说明" rows="3" maxlength="2000" placeholder="说明项目的业务范围与责任边界" /></label>
          <p v-if="projectSaveError" class="global-search-error" role="alert">{{ projectSaveError }}</p>
          <footer><span>创建后会将此项目设为当前工作区。</span><button type="submit" class="button button-primary" data-action="save-project" :disabled="projectSaving">{{ projectSaving ? "正在创建…" : "创建项目" }}</button></footer>
        </form>
      </section>
    </div>
    <div v-if="memberDialogOpen" class="global-search-backdrop" @click.self="memberDialogOpen = false">
      <section class="project-create-dialog project-members-dialog" role="dialog" aria-modal="true" aria-labelledby="project-members-title">
        <header><div><span class="eyebrow">项目访问控制</span><h2 id="project-members-title">{{ auth.activeProject?.display_name }} · 成员</h2></div><button class="search-close-button" aria-label="关闭成员管理" @click="memberDialogOpen = false">关闭</button></header>
        <p class="member-management-note">项目成员角色限制本体结构、数据源、Agent 与评审操作。只能添加已注册账号。</p>
        <div class="project-member-list" aria-label="当前项目成员">
          <div v-for="member in projectMembers" :key="member.user_id" class="project-member-row"><span class="avatar">{{ member.email.slice(0, 1).toUpperCase() }}</span><strong>{{ member.email }}</strong><span class="member-role-badge">{{ member.role === "admin" ? "管理员" : member.role === "editor" ? "编辑者" : "只读者" }}</span></div>
          <p v-if="!projectMembers.length && !memberError" class="canvas-empty-note">正在读取项目成员…</p>
        </div>
        <form class="project-create-form member-form" @submit.prevent="saveProjectMember">
          <label>成员邮箱<input v-model="memberForm.email" aria-label="项目成员邮箱" type="email" required placeholder="name@example.com" /></label>
          <label>项目角色<select v-model="memberForm.role" aria-label="项目成员角色"><option value="admin">管理员</option><option value="editor">编辑者</option><option value="viewer">只读者</option></select></label>
          <p v-if="memberError" class="global-search-error" role="alert">{{ memberError }}</p>
          <p v-if="memberNotice" class="member-success-note" role="status">{{ memberNotice }}</p>
          <footer><span>已存在的成员会更新角色。</span><button type="submit" class="button button-primary" :disabled="memberSaving">{{ memberSaving ? "保存中…" : "保存成员" }}</button></footer>
        </form>
      </section>
    </div>
  </div>
</template>
