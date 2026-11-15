<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontologies/get-ontology -->
<!-- 研读状态：已完成 -->

# Get Ontology (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontologies/get-ontology)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:00Z
- 产品状态：正式 API（v1/v2 页面均未标注 Preview）

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific ontology for a given Ontology API name or RID.”

## 摘录译文

按本体 API 名称或 RID 获取指定本体。

## 中文要点

- v1 接口为 `GET /api/v1/ontologies/{ontologyRid}`，路径只接受本体 RID；v2 为 `GET /api/v2/ontologies/{ontology}`，可使用 API 名称或 RID。
- 成功响应提供 `apiName`、`displayName`、`description` 与 `rid`，适合从列表项进入本体详情或校验资源身份。
- 该读取接口要求 OAuth scope `api:ontologies-read`；本页没有声明 branch 参数，因此不能把它当作读取分支定义的入口。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| API name | API 名称 | v2 支持用稳定机器名称定位本体 |
| RID | 资源标识符 | 全局资源身份 |
| Display name | 显示名称 | 供界面展示的友好名称 |
| Ontology read scope | 本体读取权限范围 | OAuth 应用读取本体所需的 scope |

## 疑问与待验证项

- RID 与 API 名称是否在重命名后保持同一映射，页面没有说明，应结合本体治理与命名规则核实。
- 响应不包含类型/对象数量或本体版本字段；这些数据需通过其他目录端点获取。

## 复刻启示

- 多项目本体选择器可同时保存 RID 与 API 名称：RID 用于资源身份，API 名称用于接口调用/展示映射，并记录当前用户授权结果。
- v1 与 v2 的路径参数差异放在 API 适配层，不应让 UI 拼接路径或猜测资源类型。
