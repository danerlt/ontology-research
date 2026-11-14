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
});
