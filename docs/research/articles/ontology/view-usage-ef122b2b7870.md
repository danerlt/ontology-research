<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-manager/view-usage -->
<!-- 研读状态：已完成 -->

# 本体管理器 • Ontology指标 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/view-usage)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-manager/view-usage)
- 页面语言：中文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；本卡对照英文原文整理。

## 英文原文短摘录（每个来源不超过 25 词）

> “One read represents one load request from Object Storage v1 or the Object Set Service.”

## 摘录译文

一次读取统计表示一次来自对象存储或对象集服务的加载请求。

## 中文要点

- 读取覆盖对象加载、搜索返回和属性聚合；批量加载多个对象仍计为一次读取请求。写入覆盖 Action、Function、表单、对象浏览器编辑或 API 引起的对象变更，批量编辑一次也可能只算一个写请求。
- 详情页提供近 30 天交互量（读+写）和活跃用户数；对象类型总览上的用量图帮助判断变更影响。
- 需要本体管理员开启指标，设置变更最多约 60 分钟后才反映；共享本体中只能统计已授权用户与已启用指标组织的用量。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| read | 读取 | 一次本体对象加载请求计数。 |
| write | 写入 | 一次对象编辑请求计数。 |
| active users | 活跃用户 | 30 天窗口内触发读写的去重用户数。 |

## 疑问与待验证项

- 指标以请求为单位，不等同于对象记录条数；界面应给出指标口径与覆盖范围。
- 页面提到内部表未配置会造成用量图为空，需要把“无数据”和“未启用”区分显示。

## 复刻启示

- 为类型、链接及动作提供 30 天使用趋势、调用应用和活跃用户信息，供变更评审估计影响。
- 在破坏性变更审查中引用真实依赖与最近调用，不以空白指标推断资源无人使用。
