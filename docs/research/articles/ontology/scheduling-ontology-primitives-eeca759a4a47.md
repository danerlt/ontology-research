<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/dynamic-scheduling/scheduling-ontology-primitives -->
<!-- 研读状态：已完成 -->

# 动态调度 • Ontology 原语和数据模型配置 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-ontology-primitives)
- 官方中文来源：[中文原文](https://www.palantir.com/docs/zh/foundry/dynamic-scheduling/scheduling-ontology-primitives)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：dynamic-scheduling
- 相关性：direct；Ontology 数据模型配置文档
- 官方更新时间：2026-11-12T17:46:46.936Z
- 目录核对时间：2026-11-14T14:58:42Z
- 产品状态：Dynamic Scheduling Workshop 的模型配置说明

<!-- 研读状态：已完成 -->
# 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology primitives for dynamic scheduling are comprised of one Schedule object and one or more Resource objects.”

## 摘录译文

动态调度的本体原语由一个 Schedule 对象和一个或多个 Resource 对象组成。

## 中文要点

- 最小调度模型包含 Schedule 任务对象与 Resource 资源对象；高级配置可连接多类资源，例如把维修任务关联飞机和机械师。
- 当前英文页要求计划对象有资源外键字符串、开始时间和结束时间；中文机器翻译还列出毫秒计的持续时间字段，描述不完全一致。
- Schedule 与每类 Resource 建立链接；一对多或多对多基数由调度组件的 Resource Link Type 配置决定。
- Ontology Manager 向导帮助把对象属性和链接分类为调度原语；中文页还说明可通过类型类关联保存 Action，细节需按版本确认。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Schedule object | 计划对象 | 表示带时间约束的待执行任务 |
| Resource object | 资源对象 | 任务分配的人员、设备、地点等 |
| Resource Link Type | 资源链接类型 | 计划与资源关系的基数配置 |
| Schedulable save handler | 可调度保存处理器 | 调度向导关联保存 Action 的类型类 |

## 疑问与待验证项

- 英文页和中文机器翻译对持续时间字段是否必填的描述不同；模型应以目标环境 UI 与校验规则为准。
- 资源冲突、时区和重叠任务需结合 Suggestion Functions 与 Validation rules 文档确认。

## 复刻启示

- 通过对象、时间属性和带基数链接表达排程，资源冲突与时间窗由可解释规则校验。
- 画布从调度组件反向定位 Schedule、Resource、Action 和校验函数，而非只显示静态 schema。