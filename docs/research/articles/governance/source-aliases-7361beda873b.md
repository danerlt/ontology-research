<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/source-aliases -->
<!-- 研读状态：已完成 -->

# Functions • Aliases • Source aliases • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/source-aliases)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:23Z
- 产品状态：页面覆盖 TypeScript v2 和 Python 的 source alias。

## 英文原文短摘录（每个来源不超过 25 词）

> “Source aliases are named, portable references to Data Connection sources.”

## 摘录译文

Source alias 是指向 Data Connection source 的具名、可移植引用。

## 中文要点

- Source alias 以仓库内唯一 key 引用 Data Connection source，让函数代码与具体环境的 source RID 解耦。
- 导入 source 后添加 alias，在函数配置 `sources` 中声明 key，再用 `getSource`（TSv2）或 `get_source`（Python）获取 source 和认证客户端。
- 若需诊断解析结果，可通过 TypeScript v2 的 `Aliases.source` 或 Python 的 `source` 读取实际 source RID。
- Marketplace 安装时由安装者将 alias 映射至目标环境已有 source，函数代码无需改动；alias 可附描述帮助安装者选连接。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| source alias | 来源别名 | 以稳定 key 代替具体 Data Connection source 的引用。 |
| source RID | 来源资源标识 | 当前环境中实际连接资源的 RID。 |
| Marketplace remapping | Marketplace 来源重映射 | 安装时将别名映射到目标环境 source。 |

## 疑问与待验证项

- 别名跨环境可移植，但实际 source 的权限、连接配置和凭据仍需由目标环境单独治理。
- alias key 在仓库内唯一，重命名会影响函数 config 与安装映射，需版本化。

## 复刻启示

- 为多项目/多系统 Ontology 连接器使用稳定逻辑别名，环境部署时绑定 dev/test/prod 实际连接。
- 凭据由连接资源管理，函数引用 alias 和最小 scope，不将主机地址、token 写死在规则中。
