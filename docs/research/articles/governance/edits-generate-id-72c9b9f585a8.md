<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/edits-generate-id -->
<!-- 研读状态：已完成 -->

# 函数 • Ontology edits • 为新Objects生成唯一ID • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/edits-generate-id)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/edits-generate-id)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:08Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “When writing an Ontology edit function that creates objects, you may want to generate a unique ID for the newly created object.”

## 摘录译文

编写用于创建对象的 Ontology 编辑函数时，可能需要为新对象生成唯一 ID。

## 中文要点

- 创建 Ontology 对象时必须提供主键；TSv1 示例使用 `@foundry/functions-utils` 的 `Uuid.random()`，该包通常随模板预装。
- TSv2 没有平台专属 UUID 生成器，文档建议从 npm 安装标准 `uuid` 库；新增依赖还要考虑运行时兼容性。
- 生成 ID 与创建对象属于同一编辑工作流；不要在同一动作重试时意外为同一业务实体重复创建多条记录。
- 中文官方页提示 AIP 机器翻译准确性未经验证；代码模板和依赖需按当前语言版本确认。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Unique ID | 唯一 ID | 新建对象使用的标识/主键值。 |
| Primary key | 主键 | 对象实例在其类型范围内用于识别的键。 |
| UUID | 通用唯一标识符 | 可用作新对象 ID 的标准标识符格式。 |

## 疑问与待验证项

- 平台是否要求主键全局唯一、租户内唯一或对象类型内唯一应以对象类型 schema 约束为准。
- 有业务自然键时是否仍需随机 UUID、重试和幂等创建如何协同需设计检查。

## 复刻启示

- 创建 API 支持调用方提供幂等键或使用服务端 ID 生成器，避免网络重试导致重复本体对象。
- ID 策略按对象类型配置，并将唯一性约束落到持久层；随机 ID 不替代业务去重规则。
