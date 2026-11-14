import { defineStore } from "pinia";

export interface UserSession {
  id: string;
  email: string;
  role: "admin" | "editor" | "viewer";
}

interface StoredSession {
  accessToken: string;
  user: UserSession;
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
    } as { accessToken: string; user: UserSession | null };
  },
  getters: {
    isAuthenticated: (state) => Boolean(state.accessToken && state.user),
    role: (state) => state.user?.role ?? "viewer",
  },
  actions: {
    setSession(accessToken: string, user: UserSession) {
      this.accessToken = accessToken;
      this.user = user;
      localStorage.setItem("ontology-session", JSON.stringify({ accessToken, user }));
    },
    clearSession() {
      this.accessToken = "";
      this.user = null;
      localStorage.removeItem("ontology-session");
    },
  },
});
