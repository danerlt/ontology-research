<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/websocket-subscriptions -->
<!-- 研读状态：已完成 -->

# Ontology SDK • Subscribe to Ontology changes via WebSocket • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/websocket-subscriptions)
- 官方中文来源：尚未确认（目录配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；对象集的实时变更订阅
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:44Z
- 产品状态：Object Set Watcher WebSocket；join 构造的对象集和重连具有明确限制

## 英文原文短摘录（不超过 25 词）

> “Subscriptions do not persist across server restarts. Implement reconnection logic in your client.”

## 摘录译文

订阅不会跨服务器重启保留；客户端需要实现重新连接逻辑。

## 中文要点

- TypeScript OSDK 的 `.subscribe` 使用 WebSocket 推送对象集变化；也可以直连 Object Set Watcher v2 `streamSubscriptions` 端点。
- 客户端以 JSON 请求订阅对象集、属性和引用属性；可选请求对象 RID（默认不返回，启用会增加延迟），服务端返回订阅确认、错误或更新事件。
- `objectSetChanged` 汇报对象新增/更新/移除；若对象删除或不再匹配过滤条件，状态为 REMOVED。无法增量推送时，服务端发出 `refreshObjectSet`，客户端应回退为普通 HTTP 对象集加载。
- `qos` 响应表示服务负载高，文档建议用带随机抖动的指数退避重试；订阅因用户移除、资源超限或错误可关闭。
- Join 构造的对象集订阅不保证完整；订阅有内存上限，部分高级全文检索过滤器不支持。Interface 对象集的更新会以具体对象类型返回，客户端需用元数据映射回接口属性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object Set Watcher | 对象集观察服务 | 对对象集变化建立 WebSocket 流订阅的服务 |
| referenceSet | 引用属性集合 | 请求额外监听的引用/时空序列属性 |
| `refreshObjectSet` | 刷新对象集事件 | 增量订阅无法完整给出变化时的全量重读提示 |
| QoS response | 服务质量响应 | 表示高负载的订阅响应，需要退避重试 |

## 疑问与待验证项

- 此接口提供变化通知但 join 集合不保证完整；事件流不应作为强一致 CDC 日志或唯一审计来源。
- 服务器重启、订阅内存耗尽或收到刷新事件后，客户端需要重新取快照并重建订阅。
- Interface 属性映射示例依赖另一个标为 Beta 的完整元数据端点；需在目标环境确认其可用性。

## 复刻启示

- 实时对象流采用“初始查询快照 + 增量事件 + refresh 重读 + 断线重订阅”的客户端状态机。
- 事件载荷区分 object/reference、类型、主键、字段和增删状态，并对字段投影与 RID 请求增加访问控制。
- 不完整 join 事件仅用于界面增量更新，不将其作为审计事实或保证无遗漏的数据同步通道。