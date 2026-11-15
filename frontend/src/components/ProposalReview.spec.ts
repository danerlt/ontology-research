import { describe, expect, it } from "vitest";
import { mount } from "@vue/test-utils";
import ProposalReview from "./ProposalReview.vue";

const proposal = {
  id: "proposal-1",
  title: "增加设备对象",
  status: "submitted",
  author: "editor@example.com",
};

describe("提案审阅", () => {
  it("viewer 看不到批准和驳回按钮", () => {
    const wrapper = mount(ProposalReview, { props: { role: "viewer", proposal } });

    expect(wrapper.find("button[data-action='merge']").exists()).toBe(false);
    expect(wrapper.find("button[data-action='reject']").exists()).toBe(false);
  });

  it("管理员可以看到批准和驳回按钮", () => {
    const wrapper = mount(ProposalReview, { props: { role: "admin", proposal } });

    expect(wrapper.find("button[data-action='merge']").exists()).toBe(true);
    expect(wrapper.find("button[data-action='reject']").exists()).toBe(true);
  });

  it("资源没有全部批准时禁止合并并提供逐资源批准控件", async () => {
    const wrapper = mount(ProposalReview, {
      props: {
        role: "admin",
        proposal: {
          ...proposal,
          resource_reviews: [
            { id: "review-1", resource_key: "object_type:customer", status: "pending", reviewer_id: null, comment: "" },
            { id: "review-2", resource_key: "property:customer.name", status: "approved", reviewer_id: "admin-1", comment: "已确认" },
          ],
        },
      },
    });

    expect((wrapper.find("button[data-action='merge']").element as HTMLButtonElement).disabled).toBe(true);
    expect(wrapper.findAll("[data-action='resource-review']")).toHaveLength(2);
    await wrapper.find("button[data-action='approve-resource']").trigger("click");

    expect(wrapper.emitted("review")?.[0]).toEqual([{
      proposal_id: "proposal-1",
      resource_key: "object_type:customer",
      status: "approved",
      comment: "",
    }]);
  });
});
