import { beforeEach, describe, expect, it, vi } from "vitest";
import { flushPromises, mount } from "@vue/test-utils";

const apiMock = vi.hoisted(() => ({ get: vi.fn(), post: vi.fn() }));

vi.mock("../api/client", () => ({
  api: apiMock,
  readableError: (error: unknown) => (error instanceof Error ? error.message : "请求失败"),
}));

import Branches from "./Branches.vue";

const ontology = {
  id: "ontology-1",
  api_name: "operations",
  display_name: "运营本体",
  description: "运营数据模型",
  revision: 4,
  object_type_count: 1,
  link_type_count: 0,
};

const branch = {
  id: "branch-1",
  ontology_id: "ontology-1",
  author_id: "user-1",
  name: "customer-cleanup",
  description: "客户模型整理",
  base_revision: 4,
  snapshot: {
    object_types: [
      { api_name: "customer", display_name: "客户", properties: [{ api_name: "id", display_name: "客户编号", data_type: "string", required: true, editable: false }, { api_name: "name", display_name: "客户名称", data_type: "string", required: true, editable: true, options: {} }] },
    ],
    link_types: [{ api_name: "customer_site", display_name: "关联站点", description: "原说明", source_type_api_name: "customer", target_type_api_name: "customer" }],
    actions: [{ api_name: "rename_customer", display_name: "重命名客户", description: "更新客户名称", object_type_api_name: "customer", allowed_properties: ["name"], parameters_schema: { name: { type: "string", required: true } }, submission_criteria: {}, enabled: true }],
  },
  changes: [],
  validation: { errors: [], warnings: [], valid: true },
  status: "active",
  created_at: "2026-11-15T00:00:00Z",
  updated_at: "2026-11-15T00:00:00Z",
};

describe("本体分支工作区", () => {
  beforeEach(() => {
    apiMock.get.mockReset();
    apiMock.post.mockReset();
    apiMock.get.mockImplementation((path: string) =>
      Promise.resolve(path === "/api/ontology" ? [ontology] : [branch]),
    );
    apiMock.post.mockResolvedValue(branch);
  });

  it("显示从服务读取的分支基线和资源概况", async () => {
    const wrapper = mount(Branches);
    await flushPromises();

    expect(wrapper.text()).toContain("customer-cleanup");
    expect(wrapper.text()).toContain("基于版本v4");
  });

  it("创建分支时把当前本体和名称提交给服务", async () => {
    const wrapper = mount(Branches);
    await flushPromises();
    await wrapper.get('[aria-label="分支名称"]').setValue("release-candidate");
    await wrapper.get(".branch-create-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/branches", {
      ontology_id: "ontology-1",
      name: "release-candidate",
      description: "",
    });
  });

  it("把对象类型修改暂存在选中分支", async () => {
    const wrapper = mount(Branches);
    await flushPromises();
    await wrapper.get('[aria-label="对象 API 名称"]').setValue("site");
    await wrapper.get('[aria-label="对象显示名称"]').setValue("站点");
    await wrapper.get(".branch-edit-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/branches/branch-1/changes", {
      changes: [{
        op: "add_object_type", api_name: "site", display_name: "站点", plural_display_name: "站点", description: "",
        primary_key_property: "id", title_key_property: "id", aliases: [], groups: [], icon: "object", icon_color: "#4F8067",
      }],
    });
  });

  it("按创建向导提交对象元数据、标题键和附加属性", async () => {
    const wrapper = mount(Branches);
    await flushPromises();
    await wrapper.get('[aria-label="对象 API 名称"]').setValue("site");
    await wrapper.get('[aria-label="对象显示名称"]').setValue("站点");
    await wrapper.get('[aria-label="对象复数显示名称"]').setValue("站点");
    await wrapper.get('[aria-label="对象说明"]').setValue("履约站点");
    await wrapper.get('[aria-label="主键属性"]').setValue("site_id");
    await wrapper.get('[data-action="add-object-property"]').trigger("click");
    await wrapper.get('[aria-label="新对象属性 API 名称"]').setValue("site_name");
    await wrapper.get('[aria-label="新对象属性显示名称"]').setValue("站点名称");
    await wrapper.get('[aria-label="对象标题键"]').setValue("site_name");
    await wrapper.get('[aria-label="对象别名"]').setValue("仓库,门店");
    await wrapper.get('[aria-label="对象分组"]').setValue("履约,基础设施");
    await wrapper.get('[aria-label="对象图标"]').setValue("warehouse");
    await wrapper.get('[aria-label="对象图标颜色"]').setValue("#2E6658");
    await wrapper.get(".branch-edit-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/branches/branch-1/changes", {
      changes: [
        {
          op: "add_object_type", api_name: "site", display_name: "站点", plural_display_name: "站点", description: "履约站点",
          primary_key_property: "site_id", title_key_property: "site_name", aliases: ["仓库", "门店"], groups: ["履约", "基础设施"], icon: "warehouse", icon_color: "#2E6658",
        },
        {
          op: "add_property", object_type_api_name: "site", api_name: "site_name", display_name: "站点名称", data_type: "string",
          required: false, editable: true, unique_value: false, sensitive: false,
        },
      ],
    });
  });

  it("把现有对象类型元数据作为分支更新提交", async () => {
    const wrapper = mount(Branches);
    await flushPromises();
    await wrapper.get('[aria-label="对象操作模式"]').setValue("edit");
    await wrapper.get('[aria-label="选择待修改对象类型"]').setValue("customer");
    await wrapper.get('[aria-label="对象显示名称"]').setValue("重点客户");
    await wrapper.get(".branch-edit-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/branches/branch-1/changes", {
      changes: [{
        op: "update_object_type", api_name: "customer", display_name: "重点客户", plural_display_name: "客户",
        description: "", title_key_property: "id", aliases: [], groups: [], icon: "object", icon_color: "#4F8067",
      }],
    });
  });

  it("把现有属性定义更新暂存到分支", async () => {
    const wrapper = mount(Branches);
    await flushPromises();
    const propertyTab = wrapper.findAll(".resource-kind-tabs button").find((button) => button.text() === "属性");
    await propertyTab!.trigger("click");
    await wrapper.get('[aria-label="属性操作模式"]').setValue("edit");
    await wrapper.get('[aria-label="选择待修改属性"]').setValue("customer.name");
    await wrapper.get('[aria-label="属性显示名称"]').setValue("正式名称");
    await wrapper.get('[aria-label="敏感字段"]').setValue(true);
    await wrapper.get(".branch-edit-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/branches/branch-1/changes", {
      changes: [{
        op: "update_property", object_type_api_name: "customer", api_name: "name", display_name: "正式名称",
        data_type: "string", required: true, editable: true, unique_value: false, sensitive: true,
      }],
    });
  });

  it("把链接和 Action 元数据更新暂存到各自资源", async () => {
    const wrapper = mount(Branches);
    await flushPromises();
    const linkTab = wrapper.findAll(".resource-kind-tabs button").find((button) => button.text() === "链接");
    await linkTab!.trigger("click");
    await wrapper.get('[aria-label="链接操作模式"]').setValue("edit");
    await wrapper.get('[aria-label="选择待修改链接"]').setValue("customer_site");
    await wrapper.get('[aria-label="链接显示名称"]').setValue("客户服务站点");
    await wrapper.get(".branch-edit-form").trigger("submit");
    await flushPromises();

    const actionTab = wrapper.findAll(".resource-kind-tabs button").find((button) => button.text() === "Action");
    await actionTab!.trigger("click");
    await wrapper.get('[aria-label="Action 操作模式"]').setValue("edit");
    await wrapper.get('[aria-label="选择待修改 Action"]').setValue("rename_customer");
    await wrapper.get('[aria-label="Action 显示名称"]').setValue("更新客户名称");
    await wrapper.get('[aria-label="启用此 Action"]').setValue(false);
    await wrapper.get(".branch-edit-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/branches/branch-1/changes", {
      changes: [{ op: "update_link_type", api_name: "customer_site", display_name: "客户服务站点", description: "原说明" }],
    });
    const actionCall = apiMock.post.mock.calls.find((call) => call[1]?.changes?.[0]?.op === "update_action");
    expect(actionCall?.[1].changes[0]).toMatchObject({
      op: "update_action", api_name: "rename_customer", display_name: "更新客户名称", enabled: false,
    });
  });

  it("按对象属性配置 Action 并暂存参数约束和提交条件", async () => {
    const wrapper = mount(Branches);
    await flushPromises();
    const actionTab = wrapper.findAll(".resource-kind-tabs button").find((button) => button.text() === "Action");
    expect(actionTab).toBeDefined();
    await actionTab!.trigger("click");
    await wrapper.get('[aria-label="Action API 名称"]').setValue("rename_customer");
    await wrapper.get('[aria-label="Action 显示名称"]').setValue("重命名客户");
    await wrapper.get('[aria-label="Action 目标对象类型"]').setValue("customer");
    await wrapper.get('[aria-label="Action 可修改属性 name"]').setValue(true);
    await wrapper.get('[aria-label="Action 提交条件 JSON"]').setValue('{"property":"name","operator":"not_empty"}');
    await wrapper.get(".branch-edit-form").trigger("submit");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/branches/branch-1/changes", {
      changes: [{
        op: "add_action",
        api_name: "rename_customer",
        display_name: "重命名客户",
        description: "",
        object_type_api_name: "customer",
        allowed_properties: ["name"],
        parameters_schema: { name: { type: "string", required: true } },
        submission_criteria: { property: "name", operator: "not_empty" },
        enabled: true,
      }],
    });
  });

  it("用服务端校验结果更新当前分支", async () => {
    apiMock.post.mockResolvedValueOnce({ errors: [], warnings: [], valid: true });
    const wrapper = mount(Branches);
    await flushPromises();
    await wrapper.get('[aria-label="校验本体分支"]').trigger("click");
    await flushPromises();

    expect(apiMock.post).toHaveBeenCalledWith("/api/branches/branch-1/validate");
  });
});
