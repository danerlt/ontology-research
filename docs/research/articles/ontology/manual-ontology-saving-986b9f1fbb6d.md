<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/time-series/manual-ontology-saving -->
<!-- 研读状态：已完成 -->

# 时间序列 • Derived series • 手动保存派生序列至Ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/time-series/manual-ontology-saving)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/time-series/manual-ontology-saving)
- 页面语言：中文
- 主题栏目：time-series
- 相关性：direct；Ontology 时间序列数据文档
- 官方更新时间：2026-11-12T17:46:46.929Z
- 目录核对时间：2026-11-14T15:01:29Z
- 产品状态：文档提供自动与手动保存入口；权限和当前支持方式需查派生序列配置页核实。

## 英文原文短摘录（每个来源不超过 25 词）

> “The derived series creation documentation describes the process of preparing the logic resource used to manage the derived series.”

## 摘录译文

派生序列创建文档介绍了准备逻辑资源以管理派生序列的流程。

## 中文要点

- 本页说明手动把 Derived Series 挂到 Ontology 的旧式/显式配置路径；若创建对话框已选择自动保存，则不需要该流程。派生逻辑存为模板资源，绑定对象类型的时间序列属性引用模板 RID。
- 模板只能从派生序列设置时指定的绑定对象类型求值。TSP 属性值使用模板资源 RID 而不是原始 Series ID；需要固定逻辑版本时可同时指定 `templateVersion`。
- 绑定可选根对象类型或传感器对象类型。绑定到根类型时，将模板 RID 填入该对象类型的数据源字符串列并映射到 TSP；绑定到传感器类型时，每个根对象需创建对应 sensor object，再将模板 RID 写入其 TSP 数据列。
- 派生序列不需要列在 TSP 的数据源清单中，但该时间序列属性自身仍必须列出一个数据源；文档建议可用所需类型的任意时间序列同步满足配置要求。
- 这是时间序列派生资产的绑定机制，不是通用对象属性的链接路径推理；需与用户已确认的 1–3 跳属性派生推理分开建模。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| derived series | 派生序列 | 基于模板化逻辑生成、可供应用消费的时间序列。 |
| Codex template RID | Codex 模板 RID | 标识派生逻辑模板并写入 TSP 绑定字段的资源 ID。 |
| time series property (TSP) | 时间序列属性 | 将对象类型与原始或派生序列引用关联的属性。 |
| bound object type | 绑定对象类型 | 模板允许解析该派生逻辑的对象类型。 |

## 疑问与待验证项

- 文档示例中模板称为 Codex template，字段为 Logic RID；手动绑定在创建对话框已有自动保存选项之后是否仍为推荐主流程，需查看当前 Derived Series permissions/管理文档和环境实际 UI。
- “仍须列一个数据源”的兼容性 workaround 需要关注后续产品变更，不能把无关同步当作长期数据架构方案。

## 复刻启示

- 本体属性模型应能区分静态/链接派生属性与时间序列模板引用，分别定义计算引擎、输入绑定、版本固定和刷新语义。
- 在时间序列画布上把派生逻辑资产作为独立节点，以 TSP 绑定边连接对象类型；标注允许求值的根/传感器类型和逻辑版本。
- 保存前验证模板 RID 存在、类型绑定唯一、底层列已映射、TSP 数据源配置完整，并检查用户对绑定对象和数据源的编辑权限。
