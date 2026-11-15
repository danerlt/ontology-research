import { createRouter, createWebHistory } from "vue-router";
import type { Pinia } from "pinia";
import { useAuthStore } from "./stores/auth";

export function createAppRouter(pinia?: Pinia) {
  const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: "/login", name: "login", component: () => import("./views/Login.vue") },
      { path: "/", name: "overview", component: () => import("./views/Overview.vue"), meta: { requiresAuth: true } },
      { path: "/ontology", name: "ontology", component: () => import("./views/Ontology.vue"), meta: { requiresAuth: true } },
      { path: "/objects", name: "objects", component: () => import("./views/Objects.vue"), meta: { requiresAuth: true } },
      { path: "/proposals", name: "proposals", component: () => import("./views/Proposals.vue"), meta: { requiresAuth: true } },
      { path: "/branches", name: "branches", component: () => import("./views/Branches.vue"), meta: { requiresAuth: true } },
      { path: "/data-sources", name: "data-sources", component: () => import("./views/DataSources.vue"), meta: { requiresAuth: true } },
      { path: "/agents", name: "agents", component: () => import("./views/Agents.vue"), meta: { requiresAuth: true } },
      { path: "/agent-builder/:agentId", name: "agent-builder", component: () => import("./views/AgentBuilder.vue"), meta: { requiresAuth: true } },
      { path: "/sessions", name: "sessions", component: () => import("./views/Agents.vue"), meta: { requiresAuth: true } },
      { path: "/sessions/:sessionId", name: "session-detail", component: () => import("./views/AgentSession.vue"), meta: { requiresAuth: true } },
      { path: "/audit", name: "audit", component: () => import("./views/Audit.vue"), meta: { requiresAuth: true } },
      { path: "/:pathMatch(.*)*", redirect: "/" },
    ],
  });

  router.beforeEach((to) => {
    const auth = useAuthStore(pinia);
    if (to.meta.requiresAuth && !auth.isAuthenticated) return { name: "login" };
    if (to.name === "login" && auth.isAuthenticated) return { name: "overview" };
    return true;
  });

  return router;
}
