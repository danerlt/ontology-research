<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/object-permissioning/overview -->
<!-- 研读状态：已完成 -->

# 对象权限管理 • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning/overview)
- 页面语言：中文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：2026-11-12T17:46:46.936Z
- 目录核对时间：2026-11-14T15:00:03Z
- 产品状态：官方中文路由的译文准确性未逐句验证；术语和规则按英文原文复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “The Foundry Ontology allows for granular, robust, and flexible security controls for all ontology entities.”

## 摘录译文

Foundry Ontology 为所有本体实体提供细粒度、稳健且灵活的安全控制。

## 中文要点

- 本页把“资源 schema”与“实例数据”分开说明：对象/链接类型中的名称、属性名称和数据类型属于资源；对象主键与属性值属于数据。
- 这意味着拥有类型元数据的浏览权限，不等于拥有其所有对象或属性值的读取权限；对象、链接数据需单独依据安全策略授权。
- 本卡与目录中的 `/object-permissioning` 路由规范化到同一英文 canonical 页面，分别保留是为了逐条覆盖编目 URL。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ontology resource | 本体资源 | schema 定义所在的资源对象。 |
| primary key | 主键 | 对象实例的标识值，属于对象数据而非类型定义。 |
| property value | 属性值 | 某个对象实例上的实际字段内容。 |

## 疑问与待验证项

- 本页仅概览权限的两个层级；属性级隐藏、数据源权限映射和动作写权限的完整组合需与对象安全专题一并核实。
- 此路由与根路由 canonical 相同，是否为旧导航别名仍需结合页面版本历史确认。

## 复刻启示

- 前端可在画布上显示用户有权查看的类型结构，同时对受限属性和值做独立裁剪；禁止因隐藏对象数据而错误隐藏合法 schema。
- 权限服务应分别回答“可发现 schema”“可读取实例”“可编辑实例”三个问题，并允许针对对象/链接精细化策略。
