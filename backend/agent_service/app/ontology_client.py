from typing import Any

import httpx


class OntologyApiClient:
    def __init__(self, base_url: str) -> None:
        self.client = httpx.Client(base_url=base_url, timeout=10.0)

    def search_objects(self, token: str, arguments: dict[str, Any]) -> Any:
        response = self.client.get(
            "/api/objects",
            params=arguments,
            headers=self._headers(token),
        )
        return self._result(response)

    def get_object(self, token: str, object_id: str) -> Any:
        response = self.client.get(f"/api/objects/{object_id}", headers=self._headers(token))
        return self._result(response)

    def execute_action(self, token: str, action_api_name: str, arguments: dict[str, Any]) -> Any:
        response = self.client.post(
            f"/api/actions/{action_api_name}/execute",
            json=arguments,
            headers=self._headers(token),
        )
        return self._result(response)

    @staticmethod
    def _headers(token: str) -> dict[str, str]:
        return {"Authorization": f"Bearer {token}"}

    @staticmethod
    def _result(response: httpx.Response) -> Any:
        if response.is_error:
            raise httpx.HTTPStatusError(
                "本体 API 调用失败",
                request=response.request,
                response=response,
            )
        return response.json()
