<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { api, readableError } from "../api/client";
import { useAuthStore } from "../stores/auth";

const router = useRouter();
const auth = useAuthStore();
const email = ref("admin@example.com");
const password = ref("change-this-local-password");
const error = ref("");
const loading = ref(false);

async function signIn() {
  error.value = "";
  loading.value = true;
  try {
    const result = await api.post<{
      access_token: string;
      project_id: string | null;
      user: { id: string; email: string; role: "admin" | "editor" | "viewer" };
    }>("/api/auth/login", { email: email.value, password: password.value });
    auth.setSession(result.access_token, result.user, result.project_id);
    await router.push({ name: "overview" });
  } catch (cause) {
    error.value = readableError(cause);
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <main class="login-screen">
    <div class="login-visual">
      <div class="login-emblem">O</div>
      <div class="login-diagram" aria-hidden="true">
        <span class="diagram-line line-a" /><span class="diagram-line line-b" /><span class="diagram-line line-c" />
        <span class="diagram-node node-a">客户</span><span class="diagram-node node-b">订单</span><span class="diagram-node node-c">设备</span>
      </div>
      <p>让业务对象、关系与操作<br />在同一张图里协作。</p>
      <span class="login-visual-foot">本体工作台 · 本地演示版</span>
    </div>
    <section class="login-form-side">
      <form class="login-form" @submit.prevent="signIn">
        <span class="eyebrow">欢迎回来</span>
        <h1>登录工作区</h1>
        <p class="muted">使用工作账号访问运营知识图谱。</p>
        <label>邮箱地址<input v-model="email" type="email" autocomplete="username" required /></label>
        <label>密码<input v-model="password" type="password" autocomplete="current-password" required /></label>
        <p v-if="error" class="inline-error" role="alert">{{ error }}</p>
        <button class="button button-primary login-submit" :disabled="loading">
          {{ loading ? "正在登录…" : "进入工作区" }}
        </button>
        <p class="login-hint">本地演示账号可在 `.env.example` 中查看。</p>
      </form>
    </section>
  </main>
</template>
