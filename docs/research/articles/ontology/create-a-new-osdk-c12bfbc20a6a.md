<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/create-a-new-osdk -->
<!-- 研读状态：已完成 -->

# OSDK • 创建一个新的 Developer Console 应用程序 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/create-application)（同主题但路由不同）
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/create-a-new-osdk)（与英文页人工确认对应）
- 页面语言：中文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:43Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 原文短摘录与翻译

> “默认情况下，通过 OAuth 2.0 流程获得的词元范围限定为所选实体集合。”

## 摘录译文

默认 OAuth 2.0 令牌只覆盖所选的 Ontology 资源。

## 中文要点

- 创建向导为应用选择类型、认证回调、一个 Ontology 与纳入 SDK 的对象类型/Action 类型；最后要显式生成第一个 SDK 版本。
- 所选资源不仅决定生成的类型和 API 文档，也默认限定 OAuth 令牌可访问的资源。访问 Platform API 需在 Platform SDK 页另行添加资源与操作；授权操作可能触及底层服务端点。
- 英文当前页补充：应用默认创建为 Restricted；如果确需跨项目或平台级广泛访问，创建后需显式改为 Unrestricted。生成 SDK 后不能更换关联 Ontology。
- 中文页面给出 client-facing、redirect URL、CORS、资源选择与生成首版流程。页面注明 AIP 机器翻译未验证；且部分限制细节在中文页缺失，应以英文页面为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Client-facing application | 面向客户端的应用 | 通过用户 OAuth 流程访问 Foundry 的应用类型。 |
| resource restrictions | 资源访问限制 | 默认把应用令牌范围限制到选定的本体资源和操作。 |
| Restricted application | 受限应用 | Developer Console 创建时的默认应用限制级别。 |
| Generate first version | 生成首个版本 | 发布创建应用时选定资源对应的初版 SDK。 |

## 疑问与待验证项

- 更换 Ontology 需要新建或迁移应用，当前页面没有提供原位替换 SDK 本体的流程。
- 中文页面与英文页面存在内容新旧差异；安全默认值应以英文当期文档复核，且扩大到 Unrestricted 应作为显式治理决策。

## 复刻启示

- 项目创建向导应先绑定一个 Ontology，再从资源选择生成 schema 类型和工具文档；每个应用或 Agent 的 token scope 默认最小化到其白名单资源。
- 以分支评审生成 SDK 版本并记录本体 RID、资源清单、操作 scope 和发布者；把解除资源限制作为独立审批操作。
