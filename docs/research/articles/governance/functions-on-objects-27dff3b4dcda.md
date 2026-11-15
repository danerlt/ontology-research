<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/functions-on-objects -->
<!-- 研读状态：已完成 -->

# Functions • 对象函数概述 • Functions on objects (FOO) • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/functions-on-objects)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/functions-on-objects)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:11Z
- 产品状态：对象函数是利用本体对象/关系的函数模式，不是独立的函数类型；语言不同，查询 SDK 也不同。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions in Foundry natively support accessing and modifying data from objects and links in the Ontology.”

## 摘录译文

Foundry 函数原生支持访问和修改 Ontology 中对象与链接的数据。

## 中文要点

- 导入本体类型可自动生成代码绑定，支持把对象/对象集作为输入、按需搜索集合以及提交对象编辑。
- “Functions on objects/FOO”只是对读取对象数据函数的宽泛称呼，平台没有将其定义为与其他函数不同的正式资源类型。
- TSv1 通过 @foundry/ontology-api 的 Objects.search() 搜索；TSv2 与 Python 通过 Ontology SDK 查询。
- 这类函数相较通用 FaaS 直接提供存储、读取、修改能力，并沿用 Foundry 数据安全、血缘与透明性保证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Functions on objects (FOO) | 对象函数 | 读取本体对象数据的函数模式称呼 |
| Object set search | 对象集搜索 | 从本体检索对象集合的查询操作 |
| Ontology SDK | 本体 SDK | TSv2/Python 读取和遍历本体的客户端 |

## 疑问与待验证项

- 函数类型的宽泛称谓不构成独立 schema 类型；系统目录不应因此新增一个与通用函数冲突的 kind。
- 语言 API 不同，查询/编辑语义要按 SDK 版本确认；TSv1 示例不应直接套给新项目。

## 复刻启示

- 给函数资源建立对象与链接读取/写入依赖边，并由权限、血缘与 lineage 服务统一处理。
- 画布显示函数对本体的真实输入、查询依赖与编辑输出，不把“对象函数”建模成新的本体实体类型。
