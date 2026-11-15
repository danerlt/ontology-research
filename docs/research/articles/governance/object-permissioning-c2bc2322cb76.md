<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/object-permissioning -->
<!-- 研读状态：已完成 -->

# 对象权限管理 • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning)（中文路由译文以英文原文复核）
- 页面语言：中文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T14:59:57Z
- 产品状态：官方中文路由的译文准确性未逐句验证；术语和规则按英文原文复核。

## 原文短摘录与翻译

> “We can conceptualize the Ontology's authorization structure on these two levels: ontology resources, and objects and links.”

## 摘录译文

本体的授权结构可概括为两个层次：本体资源，以及对象和链接。

## 中文要点

- 该页把 Foundry 本体授权拆成资源层与数据层：对象类型、链接类型、动作类型等资源定义 schema；对象和链接承载主键与属性值。
- 资源权限决定能否查看或管理类型定义，实例数据权限决定能否读取具体对象/链接。二者不能合并成单一的“本体可见”布尔值。
- 页面是权限体系的概览，具体的资源角色、对象安全策略和数据源策略需继续查阅相邻专题页。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ontology resource | 本体资源 | 定义类型、链接或动作 schema 的资源。 |
| object-level permission | 对象级权限 | 控制对象/链接实例数据访问的权限层。 |
| schema | 模式定义 | 类型名称、属性名、属性类型等结构信息。 |

## 疑问与待验证项

- 资源级权限与对象级策略可能由不同授权系统配置；复刻时需验证权限继承、缓存刷新和撤销生效时延。

## 复刻启示

- 将 schema 资源授权与实例数据授权建模为两条独立检查链；API、画布元数据和对象查询分别执行最小权限校验。
- 在权限检查结果中记录主体、资源、对象范围、策略来源与拒绝原因，便于审计及排障。
