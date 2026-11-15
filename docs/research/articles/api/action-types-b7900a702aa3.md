<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types -->
<!-- 研读状态：已完成 -->

# Action Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:11Z
- 产品状态：v2 Action Type 基础概念页，无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An action type represents a set of changes and logic that can be applied in the Ontology.”

## 摘录译文

Action Type 表示一组可应用于本体的变更与逻辑。

## 中文要点

v2 基础页把 Action Type 定义为可应用于 Ontology 的一组变更与逻辑，并指出其在 Ontology Manager 创建。类型本身是操作模型，执行实例、参数校验和实际写入分别由相关 API 负责。此路由是 v2 的 Action Type 基础页入口，目录 canonical 路径带 `/action-type-basics`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 本体变更与逻辑的可复用定义 |
| Ontology Manager | 本体管理器 | 维护动作类型的管理工具 |
| API v2 | API v2 | 当前 Action Type 接口文档版本 |

## 疑问与待验证项

- 本页未给出 v2 响应 schema、参数表达式、对象目标关系和执行约束；需查详情端点及 Action 用户指南。
- 概念文案与 v1 相同，不能说明跨版本 API 数据结构完全兼容。

## 复刻启示

- 画布保留动作定义到目标对象/参数的关系，版本适配仅发生在 API 接入层。
- Agent tool registry 按项目和本体读取动作定义，依据权限和类型状态过滤可执行操作。
