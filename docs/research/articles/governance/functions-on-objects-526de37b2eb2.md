<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/functions-on-objects -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/functions-on-objects)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/functions-on-objects)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:18Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions in Foundry natively support accessing and modifying data from objects and links in the Ontology.”

## 摘录译文

Foundry 函数原生支持访问和修改 Ontology 中的对象与链接数据。

## 中文要点

- “Functions on objects/FOO”是对访问本体对象数据函数的宽泛称呼，并非独立的函数类型；函数支持对象/对象集入参、按需搜索和本体编辑。
- API 根据语言而异：TSv1 用 `Objects.search()`；TSv2/Python 用 Ontology SDK client 查询。
- 本体原生支持让函数可以在平台中读取、遍历关系、编辑对象，并继承平台安全、数据来源追踪和可见性保证。
- 本体写操作的生产入口仍应封装到 Function-backed Action；中文页面为 AIP 机器翻译且未校验。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Functions on objects | 面向对象的函数 | 按业务口语描述访问本体对象的函数，不是正式不同运行时。 |
| ObjectSet | 对象集 | 惰性、可组合的本体对象查询集合。 |
| Data lineage | 数据血缘 | 记录数据生成/变更来源及影响关系。 |

## 疑问与待验证项

- 文档称安全保障原生继承；在服务用户、公共 API、Ontology 权限与跨项目情况下仍须核查执行身份和权限上下文。
- 支持修改数据并不意味着可以绕过 Action 提交/权限机制，具体编辑函数模式参照 Ontology edits 文档。

## 复刻启示

- 将对象查询绑定到 schema + principal 上下文，统一查询、关系遍历、编辑和血缘追踪 API。
- 画布可把对象关系及调用其数据的函数显示为依赖边，标出只读/写入和权限边界。
