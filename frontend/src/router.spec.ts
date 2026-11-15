import { beforeEach, describe, expect, it } from "vitest";
import { createPinia, setActivePinia } from "pinia";
import { createAppRouter } from "./router";
import { useAuthStore } from "./stores/auth";

describe("页面访问控制", () => {
  beforeEach(() => setActivePinia(createPinia()));

  it("未登录时将受保护页面转到登录页", async () => {
    const router = createAppRouter();

    await router.push("/objects");

    expect(router.currentRoute.value.name).toBe("login");
  });

  it("已登录用户可以进入本体分支管理", async () => {
    const pinia = createPinia();
    useAuthStore(pinia).setSession("test-token", { id: "u-1", email: "editor@example.com", role: "editor" });
    const router = createAppRouter(pinia);

    await router.push("/branches");

    expect(router.currentRoute.value.name).toBe("branches");
  });

  it("已登录用户可以进入数据源映射工作区", async () => {
    const pinia = createPinia();
    useAuthStore(pinia).setSession("test-token", { id: "u-1", email: "editor@example.com", role: "editor" });
    const router = createAppRouter(pinia);

    await router.push("/data-sources");

    expect(router.currentRoute.value.name).toBe("data-sources");
  });

  it("已登录用户可以进入 Agent Builder 和指定版本编辑器", async () => {
    const pinia = createPinia();
    useAuthStore(pinia).setSession("test-token", { id: "u-1", email: "admin@example.com", role: "admin" });
    const router = createAppRouter(pinia);

    await router.push("/agent-builder/agent-1");

    expect(router.currentRoute.value.name).toBe("agent-builder");
    expect(router.currentRoute.value.params.agentId).toBe("agent-1");
  });

  it("已登录用户可以打开 Agent Manager 会话检查器", async () => {
    const pinia = createPinia();
    useAuthStore(pinia).setSession("test-token", { id: "u-1", email: "editor@example.com", role: "editor" });
    const router = createAppRouter(pinia);

    await router.push("/sessions/session-1");

    expect(router.currentRoute.value.name).toBe("session-detail");
    expect(router.currentRoute.value.params.sessionId).toBe("session-1");
  });
});
