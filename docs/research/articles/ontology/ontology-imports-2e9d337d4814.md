<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/code-repositories/ontology-imports -->
<!-- 研读状态：已完成 -->

# 代码库 • Administer repositories • Ontology 导入 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/code-repositories/ontology-imports)
- 官方中文来源：[中文原文](https://www.palantir.com/docs/zh/foundry/code-repositories/ontology-imports)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：code-repositories
- 相关性：direct；标题或简介提及本体、对象、动作、权限或 Agent 主题
- 官方更新时间：2026-11-12T17:46:46.928Z
- 目录核对时间：2026-11-14T14:58:34Z
- 产品状态：Code Repositories 中导入本体类型、供 Functions on Objects 使用的入口说明

<!-- 研读状态：已完成 -->
# 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology tab in Code Repositories is used to import object and link types for use in Functions on Objects.”

## 摘录译文

代码库中的 Ontology 标签页用于导入对象类型和链接类型，供 Objects 函数使用。

## 中文要点

- Code Repositories 的 Ontology 标签页把对象类型和链接类型导入代码仓库，供 Functions on Objects 使用；本页只说明入口和用途，详细导入行为指向 Functions 文档。
- 导入的是代码中的本体资源引用，不是复制对象实例数据，也不是发布本体定义；代码函数应显式声明依赖。
- 函数代码与本体数据仍由不同平台资源管理，代码仓库里的类型引用不等于对象数据副本。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology imports | 本体导入 | 将对象类型和链接类型引入代码仓库的依赖配置 |
| Functions on Objects | 对象函数 | 通过代码函数读取或操作本体对象 |
| Code Repositories | 代码仓库 | Foundry 中托管和管理函数代码的资源 |

## 疑问与待验证项

- 本页未解释依赖如何锁定版本、同步 schema 变更、处理已删除类型或导入权限；需核对 Functions 的 Ontology imports 专页。
- 中文页面明示机器翻译未经准确性验证；实现依据以当前英文页为准。

## 复刻启示

- 将代码项目的 Ontology 依赖记录为资源清单，包含本体、对象/链接类型及 schema 版本。
- 依赖导入、SDK 生成、函数发布和运行权限应拆成可追踪步骤。