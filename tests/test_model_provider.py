import unittest
from unittest.mock import Mock, patch

import httpx

from backend.agent_service.app.model_provider import ModelProviderError, OpenAICompatibleProvider


class OpenAICompatibleProviderTests(unittest.TestCase):
    def test_sends_tool_call_request_and_normalizes_assistant_response(self) -> None:
        response = Mock()
        response.is_success = True
        response.json.return_value = {
            "id": "request-42",
            "model": "model-v2",
            "choices": [{"message": {
                "content": None,
                "tool_calls": [{"id": "call-1", "type": "function", "function": {"name": "search_objects", "arguments": "{}"}}],
            }}],
            "usage": {"prompt_tokens": 12, "completion_tokens": 3},
        }
        provider = OpenAICompatibleProvider(base_url="https://model.example/v1/", api_key="never-log-this")

        with patch("backend.agent_service.app.model_provider.httpx.post", return_value=response) as request:
            result = provider.complete(
                model="model-v1",
                messages=[{"role": "user", "content": "查询客户"}],
                tools=[{"type": "function", "function": {"name": "search_objects"}}],
            )

        self.assertEqual(request.call_args.args[0], "https://model.example/v1/chat/completions")
        self.assertEqual(request.call_args.kwargs["headers"]["Authorization"], "Bearer never-log-this")
        self.assertEqual(request.call_args.kwargs["json"]["tool_choice"], "auto")
        self.assertEqual(result["request_id"], "request-42")
        self.assertEqual(result["message"]["tool_calls"][0]["id"], "call-1")
        self.assertEqual(result["usage"]["prompt_tokens"], 12)

    def test_does_not_expose_provider_error_body_or_secret(self) -> None:
        response = Mock()
        response.is_success = False
        response.status_code = 401
        provider = OpenAICompatibleProvider(base_url="https://model.example/v1", api_key="never-log-this")

        with patch("backend.agent_service.app.model_provider.httpx.post", return_value=response):
            with self.assertRaises(ModelProviderError) as captured:
                provider.complete(model="model-v1", messages=[], tools=[])

        self.assertEqual(str(captured.exception), "模型服务返回 HTTP 401")
        self.assertNotIn("never-log-this", str(captured.exception))

    def test_redacts_transport_error_details(self) -> None:
        provider = OpenAICompatibleProvider(base_url="https://model.example/v1", api_key="never-log-this")

        with patch("backend.agent_service.app.model_provider.httpx.post", side_effect=httpx.ConnectTimeout("never-log-this")):
            with self.assertRaises(ModelProviderError) as captured:
                provider.complete(model="model-v1", messages=[], tools=[])

        self.assertEqual(str(captured.exception), "模型服务连接失败")
        self.assertNotIn("never-log-this", str(captured.exception))


if __name__ == "__main__":
    unittest.main()
