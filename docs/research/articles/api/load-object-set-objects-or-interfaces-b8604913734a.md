<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/load-object-set-objects-or-interfaces -->
<!-- 研读状态：已完成 -->

# Load Object Set Objects Or Interfaces • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/load-object-set-objects-or-interfaces)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:23Z
- 产品状态：预览接口；必须传 `preview=true`；分支与事务也有实验性限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Load the ontology objects present in the `ObjectSet` from the provided object set definition.”

## 摘录译文

根据给定 Object Set 定义加载集合中的 Ontology 对象。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/loadObjectsOrInterfaces` 按对象能否视为接口决定返回接口属性或对象类型属性；调用需 `preview=true`。
- 一次结果集不能混合接口属性对象与对象类型属性对象。若对象可视为多个接口，接口会以 `UnsupportedObjectSet` 失败；文档建议这类情况改用 `loadObjectsMultipleObjectTypes`。
- 响应包含对象类型属性以及接口属性到对象类型属性的映射；OSv1 有 10,000 条上限，OSv2 无此上限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| interface view | 接口视图 | 对象以其实现的接口形态参与读取。 |
| UnsupportedObjectSet | 不支持的对象集合 | 混合对象/接口属性或接口视图歧义时的错误。 |
| property mapping | 属性映射 | 接口属性到具体对象属性的对应关系。 |

## 疑问与待验证项

- 当一个对象实现多个接口时，API 会失败而不会自动选择；调用端需先判断集合边界。
- 预览端点与接口多重实现语义可能演进，需持续核对当前 schema。

## 复刻启示

- 跨对象类型画布可选择按共同接口查看；当集合存在多接口歧义时，提示用户选定接口或采用多类型投影。
- 将预览 API 与标准查询实现解耦，内部对象统一成带来源类型、接口视图和属性映射的结果结构。
