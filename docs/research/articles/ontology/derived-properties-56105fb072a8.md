<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/derived-properties -->
<!-- 研读状态：已完成 -->

# Derived properties • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/derived-properties)
- 官方中文来源：未确认对应页
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：本体定义的派生属性为 Beta；运行时定义的派生属性为 Generally available。

## 英文原文短摘录（每个来源不超过 25 词）

> “Derived properties are properties whose values are calculated at query time from other properties or from linked objects.”

## 摘录译文

派生属性的值是在查询时根据其他属性或关联对象计算得出的。

## 中文要点

- 派生属性不存入对象存储；查询时可沿链接选取单个对象的属性、聚合多个关联对象，或组合值进行算术/日期表达式。
- Ontology Manager 中定义的属性可供对象类型的各个消费者使用，最多遍历三条链接，但只支持链接选择与聚合，不支持表达式。运行时定义的属性属于声明它的请求或模块；表达式可用，不同客户端的遍历上限不同。
- 计算值继承路径中每个源对象及中间对象的访问约束，因此同一对象可能因用户权限不同而得到不同结果；性能取决于候选对象、关联数量、聚合和遍历跳数。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| derived property | 派生属性 | 查询时计算、只读的对象属性。 |
| link traversal | 链接遍历 | 沿本体链接到关联对象并读取其属性。 |
| runtime-defined | 运行时定义 | 在具体查询、模块或 SDK 请求中声明的派生属性。 |

## 疑问与待验证项

- 文档说明了计算与权限语义，但本地系统应如何给复杂路径配置最大扇出与超时，需要按数据规模另行压测。
- 三跳约束针对 Ontology-defined 路线；SDK runtime-defined 没有固定跳数上限，不能把两者的限制混为一谈。

## 复刻启示

- 定义受限的类型化计算 AST，禁止任意 Python/SQL 执行；将属性选择、聚合和遍历深度作为显式节点。
- 试算结果逐跳返回对象 ID、链接 ID、取值和访问过滤原因；先执行每层授权，再聚合。保存定义与即时试算分离，并在分支评审后发布。
