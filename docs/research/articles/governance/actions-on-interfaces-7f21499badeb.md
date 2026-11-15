<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/actions-on-interfaces -->
<!-- 研读状态：已完成 -->

# Action types • Actions on interfaces • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/actions-on-interfaces)
- 官方中文来源：未找到确定的一对一官方中文页（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:01Z
- 产品状态：细粒度接口动作权限仍在开发；支持的应用与服务有限，动作日志和 Functions 暂不支持。

## 英文原文短摘录（每个来源不超过 25 词）

> “Interface action submission criteria apply uniformly to all object types that implement the interface.”

## 摘录译文

接口动作的提交标准一致作用于所有实现该接口的对象类型，因此不能在同一个接口动作内按具体对象类型分别授权。

## 中文要点

- 接口动作把对象接口作为通用动作目标，可定义接口规则（创建、修改、删除、链接）和接口引用参数；接口动作约束则是接口级能力契约，具体 Action Type 承担实际编辑规则。
- 通用规则只能操作实现类型共同拥有的共享属性或删除对象，不能写某个实现类独有属性。创建时需保证接口和 Create 规则提供可作为各实现对象主键的属性。
- 提交条件对接口全部实现类一致，且用户仍需对具体对象拥有编辑权限。若要禁用某实现类继承的接口动作，需要在 Ontology Manager 对该对象类型作单独控制。
- 当前支持面有限：建模/映射约束在 Ontology Manager 配置；接口动作在 Object Explorer/Object Views 呈现；动作日志尚不支持，接口动作不能使用 Functions，更细粒度授权仍在开发中。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| interface action | 接口动作 | 面向接口实现对象类型的通用 Action Type。 |
| interface reference parameter | 接口引用参数 | 可选择任意实现该接口对象的引用参数。 |
| interface action type constraint | 接口动作类型约束 | 声明接口实现对象应满足的动作能力契约。 |

## 疑问与待验证项

- 文档区分了 Ontology Manager 中的“接口动作类型约束”和面向终端应用的动作调用能力；不能把建模契约误当作 SDK 可调用 API。
- 支持应用清单及限制会随平台扩展变化；复刻前应重新核对是否仍没有接口动作日志和函数支持。

## 复刻启示

- 数据模型中将接口能力约束与具体动作规则分层；派生/实现对象节点通过实现边共享契约，画布检查器展示可继承动作和具体实现差异。
- 保存动作前展开其覆盖的所有实现对象类型并做权限影响评估；对例外类型提供显式禁用项，默认禁止对接口共享动作做逐类授权假设。
- 校验接口属性到实现类型主键、共享字段和动作约束的完整映射；未支持的日志/函数能力要在 UI 标成平台范围限制，而非静默成功。
