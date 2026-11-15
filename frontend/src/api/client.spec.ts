import { describe, expect, it, vi } from "vitest";
import { ApiClient, readableError } from "./client";

describe("API 错误提示", () => {
  it("网络故障时给出中文处理建议", () => {
    expect(readableError(new Error("Network Error"))).toBe("服务暂不可用，请检查网络后重试");
  });

  it("每次业务请求都附带当前项目上下文", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      status: 200,
      ok: true,
      json: async () => [],
    });
    vi.stubGlobal("fetch", fetchMock);
    const client = new ApiClient();
    client.configure({
      tokenProvider: () => "token-1",
      projectProvider: () => "project-1",
      onUnauthorized: () => undefined,
    });

    await client.get("/api/ontology");

    const request = fetchMock.mock.calls[0][1] as RequestInit;
    expect(new Headers(request.headers).get("X-Project-ID")).toBe("project-1");
    vi.unstubAllGlobals();
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
