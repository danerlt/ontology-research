import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";

const apiMock = vi.hoisted(() => ({ get: vi.fn(), post: vi.fn(), put: vi.fn() }));

vi.mock("../api/client", () => ({
  api: apiMock,
  readableError: (error: unknown) => (error instanceof Error ? error.message : "请求失败"),
}));

import DataSources from "./DataSources.vue";

const ontology = { id: "ontology-1", api_name: "operations", display_name: "运营本体", revision: 4 };
const objectType = {
  id: "type-1",
  ontology_id: "ontology-1",
  api_name: "customer",
  display_name: "客户",
  primary_key_property: "id",
  properties: [
    { id: "p-id", api_name: "id", display_name: "客户编号", data_type: "string", required: true, editable: false, unique_value: true, options: {} },
    { id: "p-name", api_name: "name", display_name: "客户名称", data_type: "string", required: true, editable: true, unique_value: false, options: {} },
  ],
};
const connection = {
  id: "source-1",
  ontology_id: "ontology-1",
  name: "客户 CSV",
  description: "运营每周文件",
  connector_type: "local_file",
  status: "ready",
  mapping_count: 1,
  last_run_status: "completed",
  last_run_at: "2026-11-15T00:00:00Z",
  created_at: "2026-11-14T00:00:00Z",
};
const mapping = {
  id: "mapping-1",
  connection_id: "source-1",
  object_type_id: "type-1",
  object_type_api_name: "customer",
  object_type_display_name: "客户",
  primary_key_field: "customer_id",
  field_mappings: { customer_id: "id", full_name: "name" },
  updated_at: "2026-11-15T00:00:00Z",
};

describe("数据源与属性映射工作区", () => {
  beforeEach(() => {
    apiMock.get.mockReset();
    apiMock.post.mockReset();
    apiMock.put.mockReset();
    apiMock.get.mockImplementation((path: string) => {
      if (path === "/api/ontology") return Promise.resolve([ontology]);
      if (path === "/api/object-types") return Promise.resolve([objectType]);
      if (path === "/api/data-sources") return Promise.resolve([connection]);
      if (path.endsWith("/mappings")) return Promise.resolve([mapping]);
      if (path.endsWith("/runs")) return Promise.resolve([]);
      return Promise.resolve([]);
    });
    apiMock.post.mockResolvedValue({ ...connection, id: "source-2" });
  });

  it("显示服务端连接、字段映射和最近一次同步状态", async () => {
    const wrapper = mount(DataSources);
    await flushPromises();

    expect(wrapper.text()).toContain("客户 CSV");
    expect(wrapper.text()).toContain("本地文件");
    expect(wrapper.text()).toContain("customer_id → id");
    expect(wrapper.text()).toContain("完成");
  });

  it("创建新的本地文件连接并保存到服务端", async () => {
    const wrapper = mount(DataSources);
    await flushPromises();
    await wrapper.get('[aria-label="数据源名称"]').setValue("订单快照");
    await wrapper.get('[aria-label="数据源说明"]').setValue("每晚导出的订单 JSON");
    await wrapper.get(".data-source-create-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/data-sources", {
      ontology_id: "ontology-1",
      name: "订单快照",
      description: "每晚导出的订单 JSON",
      connector_type: "local_file",
    });
  });

  it("解析带引号逗号的 CSV，服务端预览有效后才允许原子导入", async () => {
    apiMock.put.mockResolvedValue(mapping);
    apiMock.post.mockImplementation((path: string) => path.endsWith("/preview")
      ? Promise.resolve({
        valid: true,
        rows_total: 1,
        items: [{ row: 1, primary_key_value: "C-300", properties: { id: "C-300", name: "北辰, 华东" } }],
        errors: [],
      })
      : Promise.resolve({ id: "run-1", status: "completed", rows_total: 1, rows_imported: 1, errors: [] }));
    const wrapper = mount(DataSources);
    await flushPromises();
    const input = wrapper.get('input[type="file"]');
    const file = {
      name: "customers.csv",
      text: async () => 'id,name\r\nC-300,"北辰, 华东"',
    } as File;
    Object.defineProperty(input.element, "files", { value: [file] });
    await input.trigger("change");
    await flushPromises();
    await wrapper.get(".data-source-section .mapping-actions .button-secondary").trigger("click");
    await flushPromises();
    await wrapper.get(".import-section .button-secondary").trigger("click");
    await flushPromises();

    expect(apiMock.put).toHaveBeenCalledWith("/api/data-sources/source-1/mappings", {
      object_type_api_name: "customer",
      primary_key_field: "id",
      field_mappings: { id: "id", name: "name" },
    });
    expect(apiMock.post).toHaveBeenCalledWith("/api/data-sources/source-1/mappings/mapping-1/preview", {
      rows: [{ id: "C-300", name: "北辰, 华东" }],
    });
    expect(apiMock.post).not.toHaveBeenCalledWith("/api/data-sources/source-1/mappings/mapping-1/import", expect.anything());

    await wrapper.get('.import-section button.button-primary').trigger("click");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/data-sources/source-1/mappings/mapping-1/import", {
      rows: [{ id: "C-300", name: "北辰, 华东" }],
    });
    expect(wrapper.text()).toContain("导入完成");
  });
});
