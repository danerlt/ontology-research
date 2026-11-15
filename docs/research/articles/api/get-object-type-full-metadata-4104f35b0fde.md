<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-object-type-full-metadata -->
<!-- 研读状态：已完成 -->

# Get Object Type Full Metadata • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-object-type-full-metadata)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:58Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets the full metadata for a specific object type with the given API name.”

## 摘录译文

按 API 名称获取指定对象类型的完整元数据。

## 中文要点

- 这是对象类型的扩展元数据读取接口；响应除 `objectType` 外，还可返回链接类型、实现的接口及共享属性类型到本地属性的映射。
- 可选择填充数据源、生成 SDK 的包 RID 与版本，并按 branch 读取定义；数据源默认不返回。
- 该接口处于 Preview，需显式设置 `preview=true`；OAuth 应用需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Full metadata | 完整元数据 | 对象定义与关联类型扩展信息 |
| Implements interfaces | 实现接口 | 对象类型对接口的实现关系 |
| Shared property mapping | 共享属性映射 | 共享属性类型到本地属性的对应关系 |

## 疑问与待验证项

- “完整”元数据是否包含所有展示配置、权限策略和来源血缘，页面列举的响应结构不足以证明覆盖这些管理面。
- 当 `includeDatasources=true` 时，数据源是否继续按当前用户访问权限过滤，应对照来源字段的详细 schema 与权限文档确认。

## 复刻启示

- 画布可把该接口作为对象类型详情面板或同步任务的扩展读取来源，并将对象类型与链接、接口、属性映射分层展示。
- 由于接口为 Preview，应在本地适配层隔离其响应结构，避免前端直接依赖可能变化的字段。
