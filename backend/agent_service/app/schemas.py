from datetime import datetime
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, model_validator


class AgentInputDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1, max_length=80, pattern=r"^[a-z][a-z0-9_]*$")
    display_name: str = Field(min_length=1, max_length=160)
    type: Literal["string", "number", "integer", "boolean"] = "string"
    required: bool = True
    sensitive: bool = False


class AgentVariableDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1, max_length=80, pattern=r"^[a-z][a-z0-9_]*$")
    expression: str = Field(min_length=1, max_length=2000)


class AgentCompletionConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mode: Literal["stays_open", "ends_after_first_valid_output"] = "stays_open"
    output_schema: dict[str, Any] = Field(default_factory=dict)


class AgentConfiguration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model_provider: Literal["local", "openai-compatible"] = "local"
    model_name: str = Field(default="确定性本地预览", min_length=1, max_length=160)
    system_prompt: str = Field(default="", max_length=20000)
    initial_user_message: str = Field(default="", max_length=10000)
    inputs: list[AgentInputDefinition] = Field(default_factory=list, max_length=64)
    precomputed_variables: list[AgentVariableDefinition] = Field(default_factory=list, max_length=64)
    allowed_tools: list[Literal["search_objects", "get_object", "execute_action"]] = Field(
        default_factory=list, max_length=32
    )
    allowed_actions: list[str] = Field(default_factory=list, max_length=128)
    session_completion: AgentCompletionConfig = Field(default_factory=AgentCompletionConfig)

    @model_validator(mode="after")
    def validate_unique_names_and_completion(self) -> "AgentConfiguration":
        input_names = [item.name for item in self.inputs]
        variable_names = [item.name for item in self.precomputed_variables]
        if len(input_names) != len(set(input_names)):
            raise ValueError("Agent 输入名称不能重复")
        if len(variable_names) != len(set(variable_names)):
            raise ValueError("预计算变量名称不能重复")
        if set(input_names) & set(variable_names):
            raise ValueError("Agent 输入和预计算变量不能重名")
        if len(self.allowed_tools) != len(set(self.allowed_tools)):
            raise ValueError("工具授权不能重复")
        if len(self.allowed_actions) != len(set(self.allowed_actions)):
            raise ValueError("Action 授权不能重复")
        if any(not name or len(name) > 120 for name in self.allowed_actions):
            raise ValueError("Action API 名无效")
        if self.session_completion.mode == "ends_after_first_valid_output":
            if not self.initial_user_message.strip():
                raise ValueError("首个有效输出模式必须配置初始用户消息")
            if not self.session_completion.output_schema:
                raise ValueError("首个有效输出模式必须配置输出结构")
        return self


class AgentCreate(BaseModel):
    api_name: str = Field(min_length=2, max_length=80, pattern=r"^[a-z][a-z0-9_]*$")
    display_name: str = Field(min_length=1, max_length=160)
    description: str = Field(default="", max_length=2000)
    allowed_tools: list[str] = Field(min_length=1)
    allowed_actions: list[str] = Field(default_factory=list)
    draft_config: AgentConfiguration | None = None


class AgentDraftUpdate(BaseModel):
    draft_config: AgentConfiguration


class AgentResponse(BaseModel):
    id: UUID
    api_name: str
    display_name: str
    description: str
    allowed_tools: list[str]
    allowed_actions: list[str]
    enabled: bool
    draft_config: AgentConfiguration
    latest_version_number: int | None


class AgentVersionResponse(BaseModel):
    id: UUID
    agent_id: UUID
    version_number: int
    config: AgentConfiguration
    created_by: UUID | None
    published_at: datetime


class AgentPreviewRequest(BaseModel):
    inputs: dict[str, Any] = Field(default_factory=dict)


class AgentPreviewResponse(BaseModel):
    mode: Literal["deterministic_dry_run"]
    model_provider: str
    model_name: str
    rendered_prompt: str
    initial_user_message: str
    variables: list[dict[str, str]]
    allowed_tools: list[str]
    allowed_actions: list[str]
    notices: list[str]


class AgentSessionResponse(BaseModel):
    id: UUID
    agent_id: UUID
    agent_version_id: UUID
    version_number: int
    status: str
    inputs: dict[str, Any]
    origin_resource: str
    created_at: datetime
    closed_at: datetime | None


class AgentSessionCreate(BaseModel):
    inputs: dict[str, Any] = Field(default_factory=dict)
    version_number: int | None = Field(default=None, ge=1)
    origin_resource: str = Field(default="local-workbench", min_length=1, max_length=255)


class AgentSessionListResponse(BaseModel):
    items: list[AgentSessionResponse]
    total: int
    page: int
    page_size: int


class AgentSessionDetailResponse(AgentSessionResponse):
    config: AgentConfiguration
    events: list[dict[str, Any]]


class AgentMessageRequest(BaseModel):
    content: str = Field(default="", max_length=20000)


class AgentMessageResponse(BaseModel):
    session_id: UUID
    assistant_message: str
    tool_calls: list[str]
    status: str


class ToolCallRequest(BaseModel):
    arguments: dict[str, Any] = Field(default_factory=dict)


class ToolCallResponse(BaseModel):
    session_id: UUID
    tool_name: str
    status: str
    result: Any


class AgentEventResponse(BaseModel):
    id: UUID
    sequence: int
    event_type: str
    tool_name: str | None
    status: str
    details: dict[str, Any]
    created_at: datetime


class AgentEventListResponse(BaseModel):
    items: list[AgentEventResponse]
