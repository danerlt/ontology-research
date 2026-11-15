<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/typescript-subscriptions -->
<!-- 研读状态：已完成 -->

# Ontology SDK • TypeScript • Subscribe to Ontology changes with the TypeScript OSDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-subscriptions)
- 官方中文来源：尚未确认（目录配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；TypeScript OSDK 对象集的实时事件
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:42Z
- 产品状态：GA；功能要求 OSDK 2.1 或更高版本，且 `@osdk/client` 匹配版本

## 英文原文短摘录（不超过 25 词）

> “Only one subscription may be active per query at a time.”

## 摘录译文

每个查询同一时间只能有一个活动订阅。

## 中文要点

- TypeScript OSDK 2.1 引入对象集订阅；Developer Console 中需生成 2.1.x 或更新 SDK，并安装匹配的 `@osdk/client`。
- 在对象集查询后调用 `.subscribe`，为对象新增/修改/删除、订阅成功、过期和错误注册回调；返回对象提供 `unsubscribe()`。
- 可对订阅对象集使用过滤器缩小事件范围，并通过 `properties` 数组只接收需要的字段，减少网络负载。
- `.pivotTo` 构造的对象集不支持订阅；同一查询只能有一个活动订阅，因此两个 React 组件不能重复创建独立订阅监听同一查询。
- 如果需要跨语言或更底层的连接控制，应使用对应 WebSocket API 文档，而不是把 TS SDK 包装层误当通用协议。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `.subscribe` | 对象集订阅方法 | 在查询对象集上注册生命周期回调 |
| `onChange` | 变更回调 | 接收对象变化与新增/更新/删除状态 |
| `onOutOfDate` | 订阅过期回调 | 通知调用方当前订阅需刷新/重新同步 |
| property projection | 属性投影 | 控制增量对象载荷返回哪些字段 |

## 疑问与待验证项

- 单查询单订阅约束影响多组件共享；需核验 React 应用应将订阅提升到公共父级还是使用查询缓存复用。
- 文档指出 `onOutOfDate` 事件但未在本页片段完整说明所有触发条件，需结合订阅协议/SDK 版本参考。
- GA 状态只表明功能发布成熟度，不承诺事件流无遗漏；断线、刷新和快照同步仍应参考底层协议文档。

## 复刻启示

- UI 订阅按 query identity 复用单一连接，在组件卸载或查询范围变化时停止旧订阅。
- 属性投影、过滤条件和订阅状态纳入缓存键，避免不同访问范围共用错误事件。
- 实时数据采用 onOutOfDate/错误回调触发重新加载，并把订阅服务断线状态明显呈现。