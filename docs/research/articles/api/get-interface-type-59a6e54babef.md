<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-interfaces/get-interface-type -->
<!-- 研读状态：已完成 -->

# Get Interface Type • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-interfaces/get-interface-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:14Z
- 产品状态：Preview；调用需传 `preview=true`，且不能假定所有工作流已支持分支

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific interface type with the given API name.”

## 摘录译文

获取指定 API 名对应的接口类型。

## 中文要点

`GET /api/v2/ontologies/{ontology}/interfaceTypes/{interfaceType}` 按本体标识和接口 API 名获取单个接口。请求需要 `preview=true`；可选分支（默认分支，否则受实验性分支支持范围限制）以及 SDK 包 RID/版本。OAuth2 第三方应用需申请 `api:ontologies-read`。响应包含接口 RID、API 名、显示名、描述、声明属性、含直接/间接继承内容的 `allPropertiesV2`、父接口、实现该接口的对象类型及链接。旧 `properties` 只涵盖基于 shared property types 的属性，`propertiesV2` 还能表示直接定义在接口上的属性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `interfaceType` | 接口类型 API 名 | 读取目标，使用 UpperCamelCase 命名 |
| `allPropertiesV2` | 全量属性 | 包含直接及间接扩展接口继承的解析后属性 |
| `implementedByObjectTypes` | 实现对象类型 | 声明实现当前接口的对象类型 API 名列表 |
| Preview | 预览功能 | 调用需显式传 `preview=true`，API 可能变更或移除 |

## 疑问与待验证项

- 分支参数文档提示“实验性且并非所有工作流都支持”；未说明不支持时的错误码、版本一致性和跨分支继承解析策略。
- 响应同时出现 legacy `properties` 与 `propertiesV2`；需按 SDK/API 版本确认客户端应优先消费哪个字段，不能简单合并后忽略来源。

## 复刻启示

- 本地接口详情检查器应区分自有属性与继承的解析属性，并显示继承链、实现者、来源分支和 API 版本。
- 画布和试算结果为接口抽象展开对象类型时，必须保留每个属性的类型来源与访问权限；缺少权限时不能通过 `allPropertiesV2` 绕过字段授权。
