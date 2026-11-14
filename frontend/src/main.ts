import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import { createAppRouter } from "./router";
import { api } from "./api/client";
import { useAuthStore } from "./stores/auth";
import "./styles.css";

const pinia = createPinia();
const router = createAppRouter(pinia);
const auth = useAuthStore(pinia);
api.configure({
  tokenProvider: () => auth.accessToken || null,
  onUnauthorized: () => {
    auth.clearSession();
    if (router.currentRoute.value.name !== "login") router.push({ name: "login" });
  },
});

createApp(App).use(pinia).use(router).mount("#app");
