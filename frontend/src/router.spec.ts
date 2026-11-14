import { beforeEach, describe, expect, it } from "vitest";
import { createPinia, setActivePinia } from "pinia";
import { createAppRouter } from "./router";

describe("页面访问控制", () => {
  beforeEach(() => setActivePinia(createPinia()));

  it("未登录时将受保护页面转到登录页", async () => {
    const router = createAppRouter();

    await router.push("/objects");

    expect(router.currentRoute.value.name).toBe("login");
  });
});
