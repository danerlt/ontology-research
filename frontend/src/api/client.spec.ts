import { describe, expect, it, vi } from "vitest";
import { ApiClient, readableError } from "./client";

describe("API 错误提示", () => {
  it("网络故障时给出中文处理建议", () => {
    expect(readableError(new Error("Network Error"))).toBe("服务暂不可用，请检查网络后重试");
  });

  it("优先展示服务端的中文说明", () => {
    expect(readableError({ detail: "当前账号没有此操作权限" })).toBe("当前账号没有此操作权限");
  });

  it("展示冲突响应中的结构化说明", () => {
    expect(readableError({ detail: { message: "分支与 main 存在资源冲突", conflicts: [] } })).toBe(
      "分支与 main 存在资源冲突",
    );
  });

  it("PUT 请求发送 JSON 配置并解析保存响应", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      status: 200,
      ok: true,
      json: async () => ({ saved: true }),
    });
    vi.stubGlobal("fetch", fetchMock);
    const client = new ApiClient();

    const response = await client.put("/api/data-sources/source-1/mappings", { object_type_api_name: "customer" });

    expect(fetchMock).toHaveBeenCalledWith("/api/data-sources/source-1/mappings", expect.objectContaining({
      method: "PUT",
      body: JSON.stringify({ object_type_api_name: "customer" }),
    }));
    expect(response).toEqual({ saved: true });
    vi.unstubAllGlobals();
  });
});
