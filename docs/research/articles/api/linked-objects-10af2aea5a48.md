<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects -->
<!-- 研读状态：已完成 -->

# Linked Object basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/linked-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:43Z
- 产品状态：按当前 API 参考整理；列表一致性、分支和部分媒体能力有明确限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “A Linked Object describes a object that is linked to another object.”

## 摘录译文

Linked Object 描述的是与另一个对象关联的对象。

## 中文要点

- 目录路由重定向到带版本号的 `/linked-objects/linked-object-basics` 规范页。
- 这句基础定义说明 API 读取的是本体链接关系所指向的另一对象；具体单条读取和列表读取由单独端点完成。
- 原文基础页有语法错误，本卡在中文译文中按预期含义翻译，不把原句误读为特殊资源差异。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Linked Object | 链接对象 | 通过链接类型从源对象定位到的目标对象。 |
| link type | 链接类型 | 定义源/目标对象之间关系的类型。 |
| canonical route | 规范路由 | API 文档版本化后的最终页面地址。 |

## 疑问与待验证项

- 基础页没有定义方向、多对多语义或访问控制细节，需结合 link type 和具体端点。

## 复刻启示

- 图上把链接类型作为边，目标节点对应真实对象类型；运行时每条边应能解释源主键与目标主键。
- 导航目录 alias 指向规范页，避免把同一概念重复建模。
