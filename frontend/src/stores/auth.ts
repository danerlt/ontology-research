import { defineStore } from "pinia";

export interface UserSession {
  id: string;
  email: string;
  role: "admin" | "editor" | "viewer";
}

export interface ProjectSummary {
  id: string;
  api_name: string;
  display_name: string;
  description: string;
  role: "admin" | "editor" | "viewer";
}

interface StoredSession {
  accessToken: string;
  user: UserSession;
  activeProjectId?: string;
}

function readStoredSession(): StoredSession | null {
  try {
    const serialized = localStorage.getItem("ontology-session");
    return serialized ? (JSON.parse(serialized) as StoredSession) : null;
  } catch {
    return null;
  }
}

export const useAuthStore = defineStore("auth", {
  state: () => {
    const saved = readStoredSession();
    return {
      accessToken: saved?.accessToken ?? "",
      user: saved?.user ?? null,
      projects: [] as ProjectSummary[],
      activeProjectId: saved?.activeProjectId ?? "",
    } as {
      accessToken: string;
      user: UserSession | null;
      projects: ProjectSummary[];
      activeProjectId: string;
    };
  },
  getters: {
    isAuthenticated: (state) => Boolean(state.accessToken && state.user),
    role: (state) => state.projects.find((project) => project.id === state.activeProjectId)?.role ?? state.user?.role ?? "viewer",
    activeProject: (state) => state.projects.find((project) => project.id === state.activeProjectId) ?? null,
  },
  actions: {
    setSession(accessToken: string, user: UserSession, projectId: string | null = null) {
      this.accessToken = accessToken;
      this.user = user;
      this.projects = [];
      this.activeProjectId = projectId ?? "";
      this.persistSession();
    },
    setProjects(projects: ProjectSummary[]) {
      this.projects = projects;
      if (!projects.some((project) => project.id === this.activeProjectId)) {
        this.activeProjectId = projects[0]?.id ?? "";
      }
      this.persistSession();
    },
    setActiveProjectId(projectId: string) {
      this.activeProjectId = projectId;
      this.persistSession();
    },
    clearSession() {
      this.accessToken = "";
      this.user = null;
      this.projects = [];
      this.activeProjectId = "";
      localStorage.removeItem("ontology-session");
    },
    persistSession() {
      if (!this.user) return;
      localStorage.setItem(
        "ontology-session",
        JSON.stringify({ accessToken: this.accessToken, user: this.user, activeProjectId: this.activeProjectId }),
      );
    },
  },
});
