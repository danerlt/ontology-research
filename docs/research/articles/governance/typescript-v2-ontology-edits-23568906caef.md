<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/typescript-v2-ontology-edits -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v2 • Ontology edits • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/typescript-v2-ontology-edits)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:53Z
- 产品状态：TSv2/Python staged writes 与 Python struct/DataFrame 部分为 Beta；其余能力以当前函数和仓库配置为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “For the edits created in a function to actually be applied, Ontology edit functions must be configured as a function-backed Action.”

## 摘录译文

函数创建的编辑只有在配置为函数支持的 Action 后才会真正应用。

## 中文要点

- TSv2 通过 `Edits` 类型声明函数可能改动的对象、接口和链接类型，再用 `createEditBatch` 收集创建、更新、删除及链接编辑。
- 函数需返回编辑批次；运行函数本身不等于写入，只有配置为 function-backed Action 并执行该 Action 才会应用数据变更。
- 标准 edit batch 不提供 read-after-write：更新批次后，同一函数中原始对象实例属性不会自动反映新值。要在写后继续查询改动结果，应评估 TSv2 staged writes（Beta）。
- 多对多链接需按类型/链接 API name 声明编辑范围；对象主键不可修改。struct 属性可编辑，但字段变更需要按文档约定重新赋回完整结构。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Edits | 编辑类型声明 | 静态列出本函数可修改的 Ontology 实体类型。 |
| createEditBatch | 创建编辑批次 | 生成并累计标准本体编辑操作的容器。 |
| function-backed Action | 函数支持的 Action | 通过 Action 权限和运行流程提交函数编辑。 |
| read-after-write | 写后可读 | 同一执行中后续查询可以看到刚写入的值。 |

## 疑问与待验证项

- 普通 TSv2 编辑批次和 staged writes 的可见性/原子性语义不同；若函数依赖刚写入值，不能凭“返回 edits”推断读回已更新。
- 写入后下游索引查询何时看到结果，还受对象存储与索引一致性影响，应区分执行上下文内读回和外部检索传播。

## 复刻启示

- 编辑函数的类型签名应声明可写实体白名单，并把实际写入绑定到有独立授权和审计的 Action。
- 画布预览显示对象/链接变更集、受影响节点和提交状态；将“函数计算出编辑”与“编辑已写入”作为不同运行阶段。
