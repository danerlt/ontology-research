<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-objects -->
<!-- 研读状态：已完成 -->

# List Scenario Edited Objects • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-scenarios
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:18Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Returns the list of objects that have been edited within a given scenario for a specific object type.”

## 摘录译文

返回特定对象类型下，在给定情景中被编辑的对象。

## 中文要点

- 响应是情景内已编辑对象的列表，仅包含当前用户有权查看的对象。
- 接口支持 pageSize 与 pageToken；每页返回量可能小于请求值，需按 nextPageToken 继续读取。
- 端点为 Preview，需启用 `preview=true`；OAuth 应用需要读取权限范围。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Edited objects | 已编辑对象 | 情景数据分支中发生修改的实例 |
| Object visibility | 对象可见性 | 结果遵循当前用户的对象查看权限 |
| Pagination token | 分页令牌 | 继续读取情景对象变更 |

## 疑问与待验证项

- 结果条目是否能直接提供前后值对比，或需要针对每个对象再读取 base 与 scenario 版本，页面未说明。
- 权限裁剪会造成评审者看到的变更数量不同，评审统计需标出当前用户可见范围。

## 复刻启示

- 以对象主键为稳定键对比 baseline 与 scenario 两份读模型，显示字段级差异并保留权限边界。
- 分页时将视图锚定到同一 scenario RID 和基线版本，避免分页过程中合并/变基造成混合快照。
