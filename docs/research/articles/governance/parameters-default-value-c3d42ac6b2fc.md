<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/parameters-default-value -->
<!-- 研读状态：已完成 -->

# 动作类型 • Parameters • 设置参数默认值 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameters-default-value)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/parameters-default-value)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:19Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Default values for action type parameters are used to prefill parameters in the action form.”

## 摘录译文

操作类型参数的默认值用于预填操作表单。

## 中文要点

- 默认值在参数层配置，可供 Workshop、Object Explorer、Object Views、Quiver 和 Slate 等消费者共享，避免每个应用重复配置。
- 默认值可为固定值，也可取当前选中对象的属性。应用侧的本地变量/环境变量默认值优先于全局动作参数默认值。
- 迁移到全局默认值时须移除本地覆盖，否则仍会由局部默认值决定实际表单预填值。
- 英文原文明确了优先级规则；官方中文页面的机器翻译准确性未验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Default value | 默认值 | 打开动作表单时预填参数的值。 |
| Global default | 全局默认值 | 定义在 Action Type 参数上的可复用默认配置。 |
| Local override | 本地覆盖 | 由具体应用/动作实例提供并优先生效的参数值。 |

## 疑问与待验证项

- 默认属性值在对象缺字段、空值或用户没有属性读取权限时如何处理，文档本页未展开。
- 各消费端是否都允许相同的默认值表达式/环境变量，需按每个集成页面核对。

## 复刻启示

- 区分动作级默认值与消费端局部 override，清楚展示“最终生效值来自哪里”，并在迁移时检测覆盖。
- 默认值只负责表单预填，不应被当成权限边界；服务端仍须独立校验输入值和对象授权。
