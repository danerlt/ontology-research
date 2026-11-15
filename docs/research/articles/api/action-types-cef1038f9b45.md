<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/action-types -->
<!-- 研读状态：已完成 -->

# Action Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/action-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/action-types
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:54:55Z
- 产品状态：v1 Action Type 基础页兼容路由，无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An action type represents a set of changes and logic that can be applied in the Ontology.”

## 摘录译文

Action Type 表示一组可应用于本体的变更与逻辑。

## 中文要点

此 v1 兼容路由指向动作类型概念页，而不是动作类型列表端点。动作类型由 Ontology Manager 创建，描述对本体的一组可复用变更与逻辑；如需发现类型需调用 List Action Types，如需读取字段则调用 Get Action Type。canonical 路由为 `/api/v1/ontology-resources/action-types/action-type-basics`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 可应用于本体的变更/逻辑定义 |
| API route alias | API 路由别名 | 目录中映射到 v1 canonical 基础页的入口 |
| List Action Types | 列出动作类型 | 另一项单独的分页 API 操作 |

## 疑问与待验证项

- 兼容别名本身不暴露新的 schema；以 canonical 页面和独立端点的字段定义为准。
- 本页没有讨论动作执行权限、约束验证和副作用。

## 复刻启示

- 模型画布中动作定义与动作发现 API 分离；同义文档路由通过 canonical 关系去重。
- Agent 的动作工具提供发现、详情、预验证、确认与执行的独立步骤。
