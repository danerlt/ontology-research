<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/foo-getting-started -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • 入门 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/foo-getting-started)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:18Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：One of the core features of functions is they can easily access data that has been integrated into the Foundry Ontology.

> 中文译文：函数的核心特性之一，是能够便捷访问已集成到 Foundry 本体中的数据。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- TSv1/TSv2 函数仓库导入对象、链接和接口后自动生成绑定；导入资源属于所在项目，仓库可以选择本体及需使用的类型。
- TSv1 从 `@foundry/ontology-api` 使用类型；TSv2 需生成/安装 OSDK 后从 SDK 包导入，类型实例包装方式也有版本差异。
- 对象可作为函数入参，也可通过对象集查询；TSv2/Python 以 OSDK client 访问。代码补全以本体 API Name 与导入 schema 为基础。
- 本页为双语页面的中文机翻路由；本体权限、项目隔离和资源绑定仍需由实际 SDK 权限传播规则验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Functions on objects (FOO) | 面向本体对象的函数 | 泛指读取/查询或编辑对象数据的函数，不是平台中的独立函数类别。 |
| Resource import | 资源导入 | 把某本体对象、链接、接口纳入代码仓库依赖。 |
| Code binding | 代码绑定 | 由本体资源 schema 自动生成的类型和 API。 |

## 疑问与待验证项

- 私有 Ontology 的包命名、跨项目授权和撤回资源导入如何传播需结合 OSDK 文档确认。
- 函数参数传入对象与函数内部对象查询是否应用相同的行级权限上下文，应在 SDK/应用身份模式中验证。

## 复刻启示

- 本体资源导入作为有作用域的依赖，需绑定项目、Ontology 和 schema 版本，并自动生成强类型客户端。
- 区分函数对对象的只读访问和经 Action 授权的写入访问；绑定的可见性遵循项目权限。
