<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/create-embedded-ontology-application -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Create an offline-capable application with the embedded ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/create-embedded-ontology-application)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；OSDK 应用本地同步、离线操作与 PWA 部署
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:12Z
- 产品状态：使用 `@palantir/lohi-ts` 与 Embedded Ontology React 模板；具体 SDK 版本需查看仓库

## 英文原文短摘录（每个来源不超过 25 词）

> “The embedded Ontology enables applications to sync Ontology data locally, allowing users to interact with data without network connectivity.”

## 摘录译文

嵌入式本体可让应用在本地同步本体数据，使用户在没有网络连接时仍可与数据交互。

## 中文要点

- 指南以 `@palantir/lohi-ts` 和 Embedded Ontology React 模板创建离线应用。先配置 client-facing Developer Console 应用、本体/对象类型、SDK、托管域名与重定向地址，并在 CSP 允许 WebAssembly 执行。
- 在 `syncConfig.ts` 中用 `syncedObjectTypes` 选择离线可用对象类型，也可选择过滤后的 ObjectSet；只同步用户需要的数据，因为数据量会影响首次加载时长和本地存储空间。
- 模板通过 Lohi 本地缓存执行 OSDK 查询，Action 写入可乐观更新；`SyncProvider` 执行首次同步、成功后失效 OSDK cache，并可后台周期同步。`SyncGate` 首次同步结束前暂缓显示应用。
- 在线专用 Action 可切到标准 OSDK client 执行再重新同步。PWA 安装后离线使用已同步数据，恢复网络后自动同步；可配置 peering 以只同步差异并加速重复同步。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Embedded Ontology | 嵌入式本体 | 应用可本地同步和离线访问的本体数据能力 |
| `syncedObjectTypes` | 同步对象类型配置 | 决定本地可用的对象类型/过滤集合 |
| Optimistic write | 乐观写入 | 先更新本地缓存，再进行远端同步 |
| SyncGate | 同步门控 | 首次同步完成前不呈现依赖本地数据的 UI |
| Peering | 对等同步 | 根据前次同步差异增量同步数据 |

## 疑问与待验证项

- 离线同步中的冲突合并、Action 重试、删除传播和缓存加密细节不在本指南摘要中，需阅读 Lohi SDK 行为与安全文档。
- 只同步配置对象类型的说明意味着离线缓存不能被当作完整本体副本；缺少数据需提示为未同步，而非不存在。
- WebAssembly CSP、CORS、重定向与 PWA 安装支持受浏览器和 enrollment 配置影响。

## 复刻启示

- 本地复刻可构建限定对象类型/筛选表达式的离线缓存，让工作台支持断网查阅与排队动作；同步集合必须由权限和数据最小化共同约束。
- 用可见同步状态区分“本地暂存”“待提交”“远端确认”“冲突”；乐观写入必须有撤回/重试路径和审计记录。
- Agent 离线运行应只使用明确同步到本地、仍有有效授权的数据，并记录缓存版本/最后同步时间，恢复网络后在执行写动作前重新验证。
