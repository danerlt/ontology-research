<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/python-osdk -->
<!-- 研读状态：已完成 -->

# Ontology SDK • Python • Python OSDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/python-osdk)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/python-osdk)（配对状态：matched；页面声明 AIP 机器翻译且准确性未验证）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:37Z
- 产品状态：派生属性、属性修饰、异步方法、markings 与 vector 能力在本页标为 Beta；文档列出的 Python 版本为 3.10–3.14

## 英文原文短摘录（每个来源不超过 25 词）

> “The Python OSDK supports Python versions 3.10 through 3.14.”

## 摘录译文

文档所述 Python OSDK 版本支持 Python 3.10 至 3.14；实际部署仍应以应用 Developer Console 当前生成版本为准。

## 中文要点

- 本页为 Python OSDK 2.x 的通用参考，以示例餐馆类型展示生成 SDK 的对象、对象集、链接、查询、聚合、Action、函数查询及附件操作；真实对象类和包名由 Developer Console 生成。
- Foundry 内的 Python 函数、笔记本和模型适配器可使用运行环境注入的 hostname 与凭据；独立应用需使用 Developer Console 提供的私有包索引和凭据，并配置 `FoundryClient`。服务端应区别用户身份和应用身份。
- 单对象通过主键获取；对象集可按需选择属性、过滤、排序、分页或迭代。完整迭代使用一致快照（流式数据源除外），而 `page()`/`take()` 在没有快照时跨页可能出现重复或遗漏；长时间迭代可能因快照过期失败。
- Python OSDK 支持类型化过滤、链接遍历、聚合与分组。聚合响应包含指标和 `excludedItems`。链接属性的返回形态与基数相关；many-to-one/one-to-one 与多目标链接的 API 不同。
- OSDK 2.x 的派生属性可在对象集运行时计算，例子包含通过链接取值、添加派生列、过滤空值、按派生列分组；文档把派生属性标为 Beta，需要显式启用 Beta 上下文。邻居检索、标记和向量属性等也标为 Beta。
- 上传附件后，如一小时内没有通过 Action 写入对象附件属性，附件及其内容会被删除；写入对象之前仅上传者可读取。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `FoundryClient` | Foundry 客户端 | 访问平台 API 与本体 SDK 的统一客户端。 |
| `ObjectSet` | 对象集 | 可继续过滤、链接遍历、分页、迭代与聚合的惰性集合。 |
| `Derived property` | 派生属性 | 根据对象属性或链接在运行时计算出的值；文档标注 Beta。 |
| `Snapshot` | 快照 | 多页迭代保持同一时间点视图的机制；是否可用取决于读取方法和数据源。 |
| `AllowBetaFeatures` | Beta 功能启用上下文 | 在代码中显式启用 Beta API/属性的上下文或装饰器。 |

## 疑问与待验证项

- Python 版本支持区间、Beta 清单和附件保留时间都可能随 SDK 文档更新；实现前须核对当日 Developer Console 生成版本。
- 异步读取方法属于 Beta，文档明确其快照行为可能不同于同步方法；不能把 `iterate()` 的一致性保证直接应用到 `async_take()`。
- 派生属性的成本模型、跨链接权限传播、错误/空值语义与物化策略没有在此 API 概览中完整展开，需结合派生属性专题页和权限文档研读。
- Python 中文配对页自述为 AIP 机器翻译且未验证；本卡以英文页为 API 能力依据，中文页面只作为阅读辅助。

## 复刻启示

- 将推理配置定义为显式表达式图：节点记录属性/链接操作、数据类型、空值处理、聚合函数与权限上下文；发布前静态校验跳数、基数和成本。
- 运行试算应返回值之外的计算轨迹（对象、链接、筛选和聚合步骤），并对每步做字段授权检查；不能因为 SDK 能加载链接就推定用户有权读取目标字段。
- 分页 API 应提供稳定快照令牌或明确可能重复/遗漏的弱一致语义；大集合允许使用聚合、窄属性投影和过滤降低快照过期风险。
- 附件上传采用临时态与对象绑定两个阶段，并记录到期清理、读权限和 Action 写入结果，避免孤立附件永久保留。
