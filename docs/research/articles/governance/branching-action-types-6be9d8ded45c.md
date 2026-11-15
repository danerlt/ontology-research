<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/branching-action-types -->
<!-- 研读状态：已完成 -->

# Action types • Branching action types • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/branching-action-types)
- 官方中文来源：未找到确定的一对一官方中文页（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体分支与动作治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:20Z
- 产品状态：需 Global Branching；动作分支编辑仅用于测试，不会合并回 main。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology actions integrate with Global Branching, enabling you to test action types on a branch without affecting your production environment.”

## 摘录译文

Ontology 动作与 Global Branching 集成，可在隔离分支中测试动作类型而不修改生产环境。

## 中文要点

- 可在分支的 Workshop 模块运行 Action 并检查动作配置；被动作编辑的所有对象类型都必须先在分支上完成索引，媒体动作还要求 media set 也加入该分支。未索引时对象只读，动作可能验证通过但不会落编辑。
- 分支上的 Action 对象编辑仅用于测试，不会合并回 main。Branch-aware 函数可以读取分支 schema；非 branch-aware 函数读取 main schema，但两类函数型动作都只对分支写入。
- 分支默认阻止 Webhook、外部调用函数及通知，以免测试触及外部系统或真实收件人。管理员可以显式允许；一旦启用，Webhook/外部函数会按 main 配置执行，仍可能访问生产端点。通知可定向给分支所有者或默认收件人。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Global Branching | 全局分支 | 为本体定义和动作提供隔离的变更/测试上下文。 |
| branch-aware function | 感知分支的函数 | 能在分支上修改并读取该分支 schema 的函数。 |
| side effect | 副作用 | Webhook、外部调用和通知等动作附带效果。 |

## 疑问与待验证项

- “不影响生产环境”描述的是分支对象编辑隔离；管理员打开副作用分支开关后仍可直连外部生产环境，不能把分支当作完整沙箱。
- 页面没有说明动作定义合并与动作测试产生的对象编辑如何共同治理；复刻中应分离 schema proposal merge 和测试数据处理。

## 复刻启示

- 每个分支维护独立 schema 版本、对象类型索引状态和试算数据；分支编辑数据与定义变更分别展示，禁止测试结果暗中写回主干。
- 对 webhook、外部函数和通知实现 fail-closed 默认；启用时要求明确确认目标环境、显示外部副作用清单，并默认把通知收件人限制为分支所有者。
- 发布前检查所有动作目标类型已同步索引，记录 schema commit 与对象快照版本；对象画布可展示当前分支相对主干的变更差异。
