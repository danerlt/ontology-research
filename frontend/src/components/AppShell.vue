<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { api } from "../api/client";
import { useAuthStore } from "../stores/auth";
import type { Ontology } from "../types";

const route = useRoute();
const router = useRouter();
const auth = useAuthStore();
const revision = ref(1);
const navigation = [
  { label: "工作区总览", to: "/", icon: "⌂" },
  { label: "本体结构", to: "/ontology", icon: "◇" },
  { label: "对象数据", to: "/objects", icon: "▦" },
  { label: "变更提案", to: "/proposals", icon: "⇄" },
  { label: "Agent 工作台", to: "/agents", icon: "◉" },
  { label: "审计记录", to: "/audit", icon: "≡" },
];
const titles: Record<string, string> = {
  overview: "工作区总览",
  ontology: "本体结构",
  objects: "对象数据",
  proposals: "变更提案",
  agents: "Agent 工作台",
  audit: "审计记录",
};

function signOut() {
  auth.clearSession();
  router.push({ name: "login" });
}

onMounted(async () => {
  try {
    const ontologies = await api.get<Ontology[]>("/api/ontology");
    revision.value = ontologies[0]?.revision ?? 1;
  } catch {
    revision.value = 1;
  }
});
</script>

<template>
  <div class="studio-shell">
    <aside class="sidebar">
      <div class="brand-lockup"><span class="brand-mark">O</span><span>本体工作台<small>Ontology Studio</small></span></div>
      <div class="workspace-switch"><span class="workspace-dot" /><div><strong>运营知识图谱</strong><small>本地演示工作区</small></div><span class="switch-chevron">⌄</span></div>
      <nav class="main-nav" aria-label="主导航">
        <span class="nav-heading">工作空间</span>
        <RouterLink v-for="item in navigation" :key="item.to" :to="item.to" class="nav-link" :class="{ active: route.path === item.to }">
          <span class="nav-icon">{{ item.icon }}</span>{{ item.label }}
        </RouterLink>
      </nav>
      <div class="sidebar-bottom"><span class="connection-dot" />服务已连接<span class="version-label">v0.1</span></div>
    </aside>
    <main class="workspace-main">
      <header class="topbar">
        <div class="breadcrumbs"><span>运营知识图谱</span><span class="crumb-divider">/</span><strong>{{ titles[String(route.name)] || "工作区" }}</strong></div>
        <div class="topbar-actions"><span class="revision-pill">结构版本 <b>v{{ revision }}</b></span><span class="user-chip"><span class="avatar">{{ auth.user?.email.slice(0, 1).toUpperCase() || "U" }}</span>{{ auth.user?.email }}<em>{{ auth.role }}</em></span><button class="logout-button" @click="signOut">退出</button></div>
      </header>
      <section class="page-frame"><RouterView /></section>
    </main>
  </div>
</template>
