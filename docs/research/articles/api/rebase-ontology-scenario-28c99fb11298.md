<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/rebase-ontology-scenario -->
<!-- 研读状态：已完成 -->

# Rebase Ontology Scenario • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/rebase-ontology-scenario)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:37Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Rebases all object types edited within the scenario onto the latest data from the scenario's base.”

## 摘录译文

将情景中已编辑的对象类型 rebase 到该情景基线的最新数据。

## 中文要点

- Rebase 把情景内已编辑的对象类型重新基于 scenario base 的最新数据；它不等于将情景改动合并回本体。
- 如果其他情景以同一基线编辑了相同对象类型，它们也可能观察到更新后的基线数据；调用者必须有编辑该情景的权限。
- 该端点为 Preview，需 `preview=true`；OAuth 应用需要读、写 scope。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Rebase | 变基 | 更新情景所基于的最新数据 |
| Scenario base | 情景基线 | 创建情景时选定的基础数据来源 |
| Edit permission | 编辑权限 | 允许执行 rebase 的授权条件 |

## 疑问与待验证项

- 多情景共享基线时，更新传播的时序、原子性与冲突重算边界未在 API 页面说明。
- 接口描述没有提到本次 rebase 的冲突清单或审计结果响应，需要与冲突检测接口结合验证。

## 复刻启示

- 评审 UI 应在 rebase 前提示共享基线影响，并完成冲突预览；rebase 后重新计算情景摘要与冲突状态。
- 把 Rebase、Merge、Publish 建成不同状态转换，审计记录保存操作者、时间、原始/新基线和影响资源。
