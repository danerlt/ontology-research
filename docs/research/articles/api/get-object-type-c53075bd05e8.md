<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-object-type -->
<!-- 研读状态：已完成 -->

# Get Object Type (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-object-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:55Z
- 产品状态：正式 API（页面未标注 Preview；branch 能力为实验性）

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific object type with the given API name.”

## 摘录译文

按 API 名称获取指定对象类型。

## 中文要点

- 端点按本体 API 名称或 RID，以及对象类型 API 名称读取定义；可指定 branch 读取分支定义，但分支能力属实验性且并非所有工作流均支持。
- 响应包括发布状态、名称与图标、主键、属性映射、RID、标题属性、建议可见性；v2 的 `primaryKey` 字段为字符串，`titleProperty` 单独指定对象展示标题字段。
- `includeDatasources=true` 才填充 backing datasources，默认 false；aliases 仅在 get-by-RID 读取路径填充，列表接口始终为空。需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Primary key | 主键 | v2 响应为属性 API 名称 |
| Title property | 标题属性 | 用于对象标题展示的属性 |
| Visibility | 建议可见性 | NORMAL、PROMINENT 或 HIDDEN |
| Datasource | 数据源 | 需请求参数显式展开 |

## 疑问与待验证项

- 主键能否由多列组成以及复合主键的序列化规则，需要以 v2 schema 的 PropertyApiName 定义确认；API 描述只显示 string。
- includeDatasources 的响应是否对每个 datasource 都按用户授权裁剪，需结合字段级权限文档验证。

## 复刻启示

- 画布节点优先用 `titleProperty` 取对象标题，`displayName`/`pluralDisplayName`/icon/status 控制节点样式；API 名和 RID 作为技术身份。
- 详情面板可按需读取数据源血缘；列表摘要与扩展详情分开获取，且把 branch、项目、本体作为请求作用域。
- 不要假设别名由普通按 API 名读取返回；如产品需要搜索同义词，应单独加载支持的 RID 读取路径或建本地索引。
