from typing import Any, Protocol

import httpx


class ModelProviderError(Exception):
    """安全的模型运行时错误，不包含请求凭据或响应正文。"""


class AgentModelProvider(Protocol):
    def complete(self, *, model: str, messages: list[dict[str, Any]], tools: list[dict[str, Any]]) -> dict[str, Any]:
        """请求一次模型补全并返回标准化消息。"""


class OpenAICompatibleProvider:
    def __init__(self, *, base_url: str, api_key: str, timeout_seconds: int = 60) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout_seconds = timeout_seconds

    def complete(self, *, model: str, messages: list[dict[str, Any]], tools: list[dict[str, Any]]) -> dict[str, Any]:
        url = self.base_url
        if not url.endswith("/chat/completions"):
            url += "/chat/completions"
        payload: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "tool_choice": "auto" if tools else "none",
        }
        if tools:
            payload["tools"] = tools
        try:
            response = httpx.post(
                url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=payload,
                timeout=self.timeout_seconds,
            )
        except httpx.HTTPError as exc:
            raise ModelProviderError("模型服务连接失败") from exc
        if not response.is_success:
            raise ModelProviderError(f"模型服务返回 HTTP {response.status_code}")
        try:
            data = response.json()
            message = data["choices"][0]["message"]
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            raise ModelProviderError("模型服务返回了无法读取的响应") from exc
        return {
            "request_id": data.get("id"),
            "model": data.get("model", model),
            "message": {
                "content": message.get("content"),
                "tool_calls": message.get("tool_calls") or [],
            },
            "usage": data.get("usage") or {},
        }
