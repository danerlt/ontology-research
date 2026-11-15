<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/action-types/action-type-basics -->
<!-- 研读状态：已完成 -->

# Action Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/action-types/action-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/action-types
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:54:55Z
- 产品状态：v1 Action Type 基础页兼容入口，canonical 页面无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An action type represents a set of changes and logic that can be applied in the Ontology.”

## 摘录译文

Action Type 表示一组可应用于本体的变更与逻辑。

## 中文要点

此 API v1 兼容路由对应 Action Type 基础页：动作类型由 Ontology Manager 创建，代表可作用于本体的一组变更与逻辑。具体执行、参数验证与权限由相关 Actions API 和治理配置决定。目录将此路由 canonical 到 `/api/v1/ontology-resources/action-types/action-type-basics`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 可复用的本体变更定义 |
| Ontology Manager | 本体管理器 | 创建和管理动作类型的工具 |
| Canonical URL | 规范地址 | 目录归一后的主要 v1 路由 |

## 疑问与待验证项

- 本页不含参数/提交标准字段详情；应读取 Get Action Type 响应和治理文档。
- 兼容路径与规范路径同义，不代表两套动作模型。

## 复刻启示

- 类型模型应保存动作定义的稳定 API 名/RID、输入参数和目标对象；运行事件另存并审计。
- 在多项目画布里把动作节点绑定所属本体，Agent 不可越过项目与本体授权调用。
