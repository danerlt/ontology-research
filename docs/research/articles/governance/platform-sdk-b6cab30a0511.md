<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/platform-sdk -->
<!-- 研读状态：已完成 -->

# Functions • Language-agnostic features • Use platform APIs with the Foundry platform SDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/platform-sdk)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:45Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “First-class authentication is not supported for TypeScript v1 functions.”

## 摘录译文

TypeScript v1 函数不支持一等身份认证。

## 中文要点

- Foundry Platform SDK 允许函数调用平台 API，可用于治理工作流、计划/构建管理、媒体集访问等；Ontology 查询和平台 API 可使用不同客户端。
- 函数需初始化经过认证的客户端。当前文档建议此类工作流使用 Python 或 TypeScript v2；TypeScript v1 不支持一等认证。Python SDK 要求 Python 3.9+，Python 3.14 需要 foundry-platform-sdk 1.93.0 或更高版本。
- 函数运行时客户端只有有限 API scope（如 admin-read、functions-read、ontologies-read、orchestration-read 和部分媒体/本体写范围）；函数不支持直接以 datasets-read scope 读取数据集。
- 本地实时预览可能使用用户身份与更广 scope，部署函数则受限；预览成功不等于部署执行权限满足。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Foundry Platform SDK | Foundry 平台 SDK | 在函数中调用 Foundry REST/API 能力的客户端库。 |
| scope | 权限范围 | OAuth token 可调用的 API 权限集合。 |
| live preview | 实时预览 | 开发时执行环境，权限上下文可能不同于部署运行时。 |
| first-class authentication | 一等身份认证 | 平台原生注入/管理认证上下文的能力。 |

## 疑问与待验证项

- 客户端实际可用 scope 随平台 endpoint 与 SDK 版本变化；需查 API reference 的单端点授权要求。
- 数据集在预览可读而部署不可读，是开发和运行时权限上下文不同的典型风险。

## 复刻启示

- 统一集成外部/平台 API 的凭据注入和 scope 声明；工具运行时只发放最小权限 token。
- 在本地试算和生产部署复用真实主体/权限模拟，并在发布前报告预览与运行身份差异。
