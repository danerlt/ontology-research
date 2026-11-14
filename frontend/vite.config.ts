import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      "/api": "http://localhost:8000",
      "/agent-api": {
        target: "http://localhost:8001",
        rewrite: (path) => path.replace(/^\/agent-api/, ""),
      },
    },
  },
});
