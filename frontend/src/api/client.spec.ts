import { describe, expect, it } from "vitest";
import { readableError } from "./client";

describe("API 错误提示", () => {
  it("网络故障时给出中文处理建议", () => {
    expect(readableError(new Error("Network Error"))).toBe("服务暂不可用，请检查网络后重试");
  });

  it("优先展示服务端的中文说明", () => {
    expect(readableError({ detail: "当前账号没有此操作权限" })).toBe("当前账号没有此操作权限");
  });
});
