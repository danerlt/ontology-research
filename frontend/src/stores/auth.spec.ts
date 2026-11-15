import { beforeEach, describe, expect, it } from "vitest";
import { createPinia, setActivePinia } from "pinia";
import { useAuthStore } from "./auth";

describe("项目身份上下文", () => {
  beforeEach(() => {
    localStorage.clear();
    setActivePinia(createPinia());
  });

  it("保持用户选中的成员项目并使用该项目角色", () => {
    const auth = useAuthStore();
    auth.setSession("token", { id: "user-1", email: "admin@example.com", role: "admin" }, "project-b");
    auth.setProjects([
      { id: "project-a", api_name: "ops", display_name: "运营", description: "", role: "admin" },
      { id: "project-b", api_name: "supply", display_name: "供应链", description: "", role: "viewer" },
    ]);

    expect(auth.activeProjectId).toBe("project-b");
    expect(auth.activeProject?.display_name).toBe("供应链");
    expect(auth.role).toBe("viewer");
  });

  it("当前项目失去访问资格后回退到第一个可访问项目", () => {
    const auth = useAuthStore();
    auth.setSession("token", { id: "user-1", email: "admin@example.com", role: "admin" }, "project-gone");
    auth.setProjects([
      { id: "project-a", api_name: "ops", display_name: "运营", description: "", role: "editor" },
    ]);

    expect(auth.activeProjectId).toBe("project-a");
    expect(auth.role).toBe("editor");
  });
});
