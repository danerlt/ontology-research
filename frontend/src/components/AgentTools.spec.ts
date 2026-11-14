import { describe, expect, it } from "vitest";
import { mount } from "@vue/test-utils";
import AgentTools from "./AgentTools.vue";

describe("Agent 工具授权界面", () => {
  it("未获授权的工具不能触发", async () => {
    const wrapper = mount(AgentTools, {
      props: { allowedTools: ["search_objects"] },
    });

    const button = wrapper.find("button[data-tool='execute_action']");
    expect((button.element as HTMLButtonElement).disabled).toBe(true);
    await button.trigger("click");
    expect(wrapper.emitted("call-tool")).toBeUndefined();
  });
});
