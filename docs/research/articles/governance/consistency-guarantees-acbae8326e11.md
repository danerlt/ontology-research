<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/consistency-guarantees -->
<!-- 研读状态：已完成 -->

# Action types • Consistency and isolation • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/consistency-guarantees)
- 官方中文来源：未找到确定的一对一官方中文页（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:18Z
- 产品状态：页面提供 Legacy、Snapshot isolation、Read committed 三种级别；分阶段写入当前仅支持 Legacy。

## 英文原文短摘录（每个来源不超过 25 词）

> “All new action types that use batched writes are created with snapshot isolation by default.”

## 摘录译文

所有使用批量写入的新动作类型默认采用快照隔离；当前使用分阶段写入的动作类型只支持旧版隔离模式。

## 中文要点

- 隔离级别规定 Action 执行时每次读取看到的数据版本，以及并发修改何时使动作失败；更强隔离可避免更多异常但会拒绝更多冲突，较弱隔离提交更宽松但保证更少。
- Legacy 读取通常来自同一时间点但无保证；Snapshot isolation 保证本体读取都来自动作开始时的一个快照，且仅对双方都写入的对象做冲突检查；Read committed 每次读最新已提交值，并允许并发变更，重叠属性采用最后提交值。
- 快照隔离不检测只读对象与写入对象间的读写冲突，因此会发生 write skew；若业务不变量要求互斥，应让竞争动作写同一共享对象触发写写冲突。来源函数访问的数据可能在快照之外，原子性和冲突检查不覆盖来源侧操作。
- 新批量写入动作默认快照隔离；分阶段写入目前仅支持 Legacy。级别在 Ontology Manager 的 Capabilities 中配置，变更对后续执行生效。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| isolation level | 隔离级别 | 定义动作读取视图以及并发冲突检测范围。 |
| snapshot isolation | 快照隔离 | 动作内本体读取固定到开始执行时的一致视图。 |
| read committed | 读已提交 | 每次读取取当时最新已提交值；冲突覆盖可按最后提交获胜。 |
| write skew | 写偏斜 | 并发动作读取同一条件却写不同对象，均通过而破坏整体不变量。 |

## 疑问与待验证项

- 快照隔离只对被写对象做冲突校验，不能保证任意跨对象业务不变量；设计派生推理或动作规则时必须检查是否存在写偏斜。
- 文档明确来源函数读写不在 Action 的快照原子性范围内；若动作调用多系统连接器，需另行处理外部一致性、重试和补偿。

## 复刻启示

- 为动作配置显式隔离级别和写入模式；默认快照隔离，并在设计校验器中识别“读取集合谓词、却只写入不同对象”的潜在写偏斜，建议用共享锁/计数对象表达不变量。
- 实时试算结果应绑定快照版本和输入对象版本，提交时重新检查写集冲突并向用户展示冲突路径；外部来源的观测时间单独标注，不能伪装成统一快照。
- 针对弱隔离覆盖写、强隔离冲突重试和分阶段写入能力限制提供明确策略，不宣称跨来源操作具备统一事务原子性。
