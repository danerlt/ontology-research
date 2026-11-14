import { describe, expect, it } from "vitest";
import { mount } from "@vue/test-utils";
import { createPinia } from "pinia";
import { createMemoryHistory, createRouter } from "vue-router";
import Login from "./Login.vue";

describe("本地登录表单", () => {
  it("预填可通过邮箱校验的管理员账号", () => {
    const router = createRouter({ history: createMemoryHistory(), routes: [{ path: "/", component: { template: "<div />" } }] });
    const wrapper = mount(Login, { global: { plugins: [createPinia(), router] } });

    expect((wrapper.get('input[type="email"]').element as HTMLInputElement).value).toBe("admin@example.com");
  });
});
