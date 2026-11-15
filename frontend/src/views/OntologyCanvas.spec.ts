import { createPinia } from "pinia";
import process from "node:process";
import { defineComponent, h } from "vue";
import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

const apiMock = vi.hoisted(() => ({ get: vi.fn(), post: vi.fn() }));

vi.mock("../api/client", () => ({
  api: apiMock,
  readableError: (error: unknown) => (error instanceof Error ? error.message : "请求失败"),
}));

import OntologyCanvas from "./OntologyCanvas.vue";
import { useAuthStore } from "../stores/auth";

const ontology = {
  id: "ontology-1",
  api_name: "operations",
  display_name: "运营本体",
  description: "运营知识图谱",
  revision: 4,
  object_type_count: 2,
  link_type_count: 1,
};

const canvas = {
  ontology: { id: ontology.id, api_name: ontology.api_name, display_name: ontology.display_name, revision: ontology.revision },
  branch: null,
  nodes: [
    { id: "object_type:customer", type: "objectType", data: { api_name: "customer", display_name: "客户", description: "客户资料", properties: [], actions: [] } },
    { id: "object_type:order", type: "objectType", data: { api_name: "order", display_name: "订单", description: "交易订单", properties: [], actions: [] } },
  ],
  edges: [
    { id: "link:customer_orders", source: "object_type:customer", target: "object_type:order", type: "ontologyLink", data: { api_name: "customer_orders", display_name: "客户订单", source_cardinality: "many", target_cardinality: "one" } },
  ],
};

describe("本体关系画布", () => {
  beforeEach(() => {
    localStorage.clear();
    apiMock.get.mockReset();
    apiMock.post.mockReset();
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/ontology") return Promise.resolve([ontology]);
      if (path === "/api/branches") return Promise.resolve([]);
      if (path === "/api/ontology/canvas") return Promise.resolve(canvas);
      return Promise.resolve([]);
    });
  });

  it("在本体和关系数据加载成功后退出加载态并显示图谱资源", async () => {
    const pinia = createPinia();
    useAuthStore(pinia).activeProjectId = "project-1";
    if (!globalThis.ResizeObserver) {
      globalThis.ResizeObserver = class {
        observe() {}
        unobserve() {}
        disconnect() {}
      } as unknown as typeof ResizeObserver;
    }
    const svgPrototype = SVGElement.prototype as SVGElement & { getBBox?: () => DOMRect };
    if (!svgPrototype.getBBox) {
      svgPrototype.getBBox = () => ({ x: 0, y: 0, width: 100, height: 24 }) as DOMRect;
    }
    const offsetWidth = vi.spyOn(HTMLElement.prototype, "offsetWidth", "get").mockReturnValue(800);
    const offsetHeight = vi.spyOn(HTMLElement.prototype, "offsetHeight", "get").mockReturnValue(600);
    const runtimeErrors: unknown[] = [];
    const unhandledReasons: unknown[] = [];
    const captureUnhandled = (reason: unknown) => unhandledReasons.push(reason);
    process.on("unhandledRejection", captureUnhandled);
    const canvasRoot = defineComponent({
      setup: () => () => h(OntologyCanvas),
      errorCaptured(error) {
        runtimeErrors.push(error);
        return false;
      },
    });
    let wrapper: ReturnType<typeof mount> | undefined;
    try {
      wrapper = mount(canvasRoot, {
        global: {
          plugins: [pinia],
          stubs: {
            RouterLink: { template: "<a><slot /></a>" },
            Background: true,
            Controls: true,
            MiniMap: true,
          },
        },
      });
      await flushPromises();
      await new Promise((resolve) => setTimeout(resolve, 0));

      expect(wrapper.find(".canvas-loading").exists()).toBe(false);
      expect(wrapper.find(".canvas-resource-rail h2").text()).toBe("2 个资源");
      expect(wrapper.text()).toContain("客户");
      expect(wrapper.findAll(".vue-flow__node")).toHaveLength(2);
      expect(runtimeErrors.some((error) => String(error).includes("Maximum recursive updates exceeded"))).toBe(false);
      expect(unhandledReasons.some((error) => String(error).includes("Maximum recursive updates exceeded"))).toBe(false);
    } finally {
      wrapper?.unmount();
      offsetWidth.mockRestore();
      offsetHeight.mockRestore();
      process.off("unhandledRejection", captureUnhandled);
    }
  });
});
