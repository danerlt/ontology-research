<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-permissioning/managing-object-security -->
<!-- 研读状态：已完成 -->

# Object permissioning • Managing object security • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/managing-object-security)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning/managing-object-security)（配对状态：matched）
- 页面语言：英文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:22Z
- 产品状态：当前页面比较对象/属性策略与数据源策略，说明源数据权限、底层资源、下游输出和媒体引用的安全边界。

## 英文原文短摘录（每个来源不超过 25 词）

> “Both approaches support cell-level security, which is a combination of row and column level security.”

## 摘录译文

两种方式都支持单元格级安全，它由行级与列级安全组合而成。

## 中文要点

- 本体数据可由 object/property policies 或 datasource policies 保护；对象策略管行、属性策略管列，组合后形成 cell-level security。
- 对象策略直接配置于类型并独立于数据源权限，通常更统一；接近即时生效，并支持 streams 与 Global Branching。若原始数据集也在本体之外被使用，仍可能需要 restricted view 等数据源策略。
- 对象/属性 granular row/column controls 仅在读取时过滤，不自动保护导出或下游数据；需要 markings 或 Classification-based Access Control 维持传播保护。
- media reference 等属性可能指向本体外部的资源；用户即使看不到引用字段，如果 media set 本身授权过宽仍可能直接读取资源。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| data source policy | 数据源策略 | 由底层 dataset、stream 或 restricted view 权限决定对象可见性。 |
| cell-level security | 单元格级安全 | 根据行和列条件限制具体属性值可见性。 |
| restricted view | 受限视图 | 在 dataset 层对行进行访问控制的资源。 |

## 疑问与待验证项

- - 安全是否随 materialization、导出和外部资源传播需要分开验证；元数据读权限不代表底层文件/媒体授权也正确。
- - 选择 object policy 还是 datasource policy取决于源数据是否有本体外消费者，以及是否要保护原始 dataset。

## 复刻启示

- - 为项目、Ontology 对象类型、原始系统数据集、derived values、materialization 和附件媒体分别建权限边界及传播关系图。
- - 安全设计需展示数据流下游和旁路资源链接；测试对象/属性读取、导出、下载、外部媒体读取以及不同用户组的实际结果。
