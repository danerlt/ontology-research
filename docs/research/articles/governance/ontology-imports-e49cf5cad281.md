<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/ontology-imports -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • 导入Object和链接类型 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/ontology-imports)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/ontology-imports)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:26Z
- 产品状态：函数仓库通过 Project 级资源导入获得对象/接口/链接类型，并按语言模板生成或刷新代码绑定；当前单个 Project 导入多个 Ontology 不受支持。

## 原文短摘录与翻译

> “Any object, interface, or link types you want to use in your function must be imported into the Project that contains your repository.”

## 摘录译文

函数要使用的对象、接口或链接类型，必须导入包含该代码仓库的 Project。

## 中文要点

- 在 Resource Imports 中选择 Ontology，再挑选函数所需的对象类型、关联链接类型或接口；这些资源授权作用于包含仓库的 Project。
- 保存导入后 Code Assist 会更新代码绑定；TSv1 从 `@foundry/ontology-api` 导入，TSv2/Python 需生成对应 Ontology SDK 并安装。
- 当前文档明确一个 Project 不能同时导入多个 Ontology；同 Project 内多个仓库会共享 Project 级导入变化。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Resource Imports | 资源导入 | 为 Project 引入函数可用的 Ontology 资源 |
| code bindings | 代码绑定 | 由本体类型生成的静态类型和 SDK 引用 |
| Ontology SDK (OSDK) | Ontology SDK | 从导入的对象、链接等资源生成的语言 SDK |

## 疑问与待验证项

- 多个代码仓库共享同一 Project 导入配置，会带来何种资源可见性及变更传播边界，需结合 Project 权限与函数仓库权限文档确认。
- 页面未说明跨 Project 复用同一 ontology schema 的具体 SDK 发布策略；本系统需自行定义项目隔离和共享本体授权模型。

## 复刻启示

- 将项目资源导入建模为依赖清单，记录本体版本、对象类型、链接类型、接口及所需字段；生成 SDK 前冻结依赖快照。
- 本体 schema 变更后生成新 SDK 版本并提示仓库重新构建，不应静默改变历史代码生成结果。
- 多项目和多系统设计无需照搬单 Project 限制；但资源引用必须显式带 project/ontology scope 并做授权检查。
