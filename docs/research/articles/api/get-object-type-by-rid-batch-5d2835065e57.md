<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-object-type-by-rid-batch -->
<!-- 研读状态：已完成 -->

# Get Object Type By Rid Batch • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-object-type-by-rid-batch)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:56Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a list of object types by RID in bulk.”

## 摘录译文

按 RID 批量获取对象类型列表。

## 中文要点

- 这是按对象类型资源标识符批量读取定义的只读接口，面向一次加载多个对象类型元数据的调用场景。
- 单次请求最多 100 个 RID；不存在或当前令牌无权限的对象类型会从响应中被过滤，调用方不能把“未返回”简单等同为“不存在”。
- 该接口处于 Preview，必须显式传 `preview=true`；可选 `branch` 指定读取的定义分支，OAuth 应用需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| RID | 资源标识符 | 用于稳定指向对象类型资源 |
| Preview | 预览功能 | 接口可能调整或移除，需显式启用 |
| Branch | 分支 | 选择对象类型定义的读取版本 |

## 疑问与待验证项

- 权限过滤与不存在资源共用“未出现在响应中”的行为，客户端是否能通过其他授权诊断接口区分两者？
- 文档未说明批量响应是否保持输入顺序，界面需自行按 RID 关联结果。

## 复刻启示

- 画布首次打开多个对象类型时可用批量元数据读取减少请求数，但必须按 RID 做结果映射并显示无权/缺失的未决状态。
- 本地复刻应把 Preview 能力做成版本化 API 能力标记；不可将批量接口误当成稳定发布契约。
