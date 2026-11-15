<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/python-osdk-migration -->
<!-- 研读状态：已完成 -->

# Ontology SDK • Python • Python OSDK migration guide • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/python-osdk-migration)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:37Z
- 产品状态：指南列出 V2 Beta 能力并要求显式启用；迁移前需在 Developer Console 核对生成器和 SDK 版本

## 英文原文短摘录（每个来源不超过 25 词）

> “This guide is intended to help you migrate applications using Python OSDK 1.x to Python OSDK 2.x.”

## 摘录译文

本指南聚焦 Python OSDK 1.x 到 2.x 的接口与返回类型迁移，并建议在 Developer Console 选定 2.x 文档/生成器版本。

## 中文要点

- 2.x 把 Platform SDK 与 OSDK 纳入同一个客户端，提供公开的 `Config` 配置类；不再需要通过保留的私有 `_session` 修改请求配置。
- 查询函数的返回类型从对象主键/RID等标识值转向真实类型实例；2.x 还支持二维、三维聚合和 map 类型返回。
- 链接返回值按关系基数改变：一对一/多对一为 `Optional[Object]`，一对多/多对多为 `ObjectSet`；后者因此可直接使用 `.page`、`.where`、`.group_by` 等集合方法。
- 聚合从 `dict[str, Any]` 改为类型化 `AggregateObjectsResponse`，但可通过 `.to_dict()` 取得旧式字典形状。范围分组输入由 `start_value`/`end_value` 字典列表改为二元组集合；附件上传由 `AttachmentMetadata` 改为 `Attachment`。
- V2 的过滤语法要求通过 `.object_type` 引用筛选属性；`.is_member_of` 更名为 `.in_`。指南标注字符串 `starts_with` 已在 2.75.0 移除，应使用 `contains_all_terms_in_order(..., prefix_last_term=True)` 做前缀匹配。
- 派生属性、近邻对象集过滤、markings、vector 和 Struct 等列入 Beta 能力，必须显式启用；迁移成功不等同于所有 Beta 特性都适合生产。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Python OSDK 1.x / 2.x` | Python OSDK 1.x / 2.x | 同一 SDK 的旧版和新版生成/运行时接口。 |
| `AggregateObjectsResponse` | 对象聚合响应 | V2 的类型化聚合结果；`.to_dict()` 提供兼容字典视图。 |
| `Optional[Object]` | 可空对象 | 单目标关系未链接时可以返回 `None` 的对象引用。 |
| `Config` | 客户端配置 | V2 提供的 HTTP 默认头、代理、超时、TLS 校验等配置入口。 |
| `prefix_last_term` | 前缀匹配最后词项 | 在迁移指南推荐的新字符串过滤方法中启用前缀语义。 |

## 疑问与待验证项

- 迁移指南里的 SDK 版本是文档撰写时点信息；当前应用可生成的 V2 版本和具体签名需在 Developer Console 版本选择器确认。
- 返回类型和链接基数变化会影响应用业务逻辑（判空、遍历、序列化、分页）；只替换导入路径不足以完成迁移。
- 官方中文配对目前为多个候选（包括 Python OSDK 与 TypeScript 迁移页），无法确认该指南有专属中文译本；本卡根据英文官方页面独立研读。
- 指南列出的 Beta API 语法和稳定性可变；升级流程需要按项目运行环境验证，并准备回滚到已锁定的 SDK 依赖版本。

## 复刻启示

- 复刻系统的 SDK 与外部 API 需要语义化版本、生成器版本、schema 版本及迁移指南；升级可输出按类型列出的破坏性改动。
- 对象链接在 API 形状上应尊重基数：单对象关系可空，多对象关系返回对象集。UI 画布也应把基数标在连线上，SDK 和图模型保持同一契约。
- 聚合响应使用有名字段和明确类型，同时提供可选字典序列化兼容层；对老客户端保留可检测、可弃用而非立即删除的过渡路径。
- Beta 推理能力应在定义、试算和发布界面标明状态；需版本锁定、显式开关、错误可见与评审记录，避免实验语义在没有通知时进入稳定工作流。
