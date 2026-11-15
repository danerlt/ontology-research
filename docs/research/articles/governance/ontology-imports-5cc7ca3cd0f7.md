<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/ontology-imports -->
<!-- 研读状态：已完成 -->

# Functions • Functions on objects • Import object, interface, and link types • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/ontology-imports)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/ontology-imports)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:13Z
- 产品状态：当前函数指南说明同一 Project 暂不支持导入多个 Ontology。

## 英文原文短摘录（每个来源不超过 25 词）

> “Any object, interface, or link types you want to use in your function must be imported into the Project that contains your repository.”

## 摘录译文

函数中要使用的对象、接口或链接类型，必须导入包含该仓库的 Project。

## 中文要点

- 先通过 Resource Imports 选择 Ontology，再选择对象、链接和接口类型；保存后 Code Assist 会重启并按新 schema 重新生成绑定。
- TSv1 从 `@foundry/ontology-api`（私有 Ontology 使用对应命名空间）引用；TSv2 需生成 OSDK 后从 `@ontology/sdk` 引用；Python 从 `ontology_sdk.ontology.objects/object_sets` 引用。
- 要使用接口必须通过 Interfaces 单独导入；链接资源应与其端点对象类型配套导入。
- 当前同一个 Project 只能选择一个 Ontology；其导入资源可能是项目级共享配置，不是完全独立的单仓依赖。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Resource Imports | 资源导入面板 | 选择、查看和删除本体类型资源的仓库界面。 |
| Ontology binding | 本体绑定 | 为导入的 schema 生成语言类型和 SDK 引用。 |
| Ontology interface | 本体接口 | 可在函数中导入并作为共享语义类型引用的接口。 |

## 疑问与待验证项

- 单项目仅一个 Ontology 的限制会影响跨本体应用拆分；页面未给出多本体统一导入的迁移方案。
- 同项目仓库间导入联动意味着变更可能影响其他仓库，应检查 repository access/权限传播。

## 复刻启示

- 数据模型需支持一个项目/代码库绑定多个本体，或显式记录当前产品限制并在导入阶段阻止歧义。
- 为每个函数保存对象、接口、链接和生成 SDK 版本依赖，检测 schema 变化并生成重新编译预览。
