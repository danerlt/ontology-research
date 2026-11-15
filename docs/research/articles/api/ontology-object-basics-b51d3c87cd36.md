<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/ontology-object-basics -->
<!-- 研读状态：已完成 -->

# Ontology Object basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/ontology-object-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:26Z
- 产品状态：v2 对象基础页，无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An Object is a data container for a specific instance of an Object Type.”

## 摘录译文

Object 是某个 Object Type 具体实例的数据容器。

## 中文要点

v2 Ontology API 的 Object 基础页定义运行时对象实例为 Object Type 的单个数据容器。它链接对象类型概念，但本身不重述 v1 页面给出的过滤运算符表；v2 查询行为应参考 v2 List/Search Objects 操作文档。Object Set 则是由多个实例组成的集合，属于不同资源概念。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object | 对象实例 | Object Type 下的具体数据记录 |
| Object Type | 对象类型 | 对象实例所遵循的 schema |
| Object Set | 对象集合 | 多个对象实例组成的集合 |
| API v2 | API v2 | 当前页面的 API 版本上下文 |

## 疑问与待验证项

- 本页未涉及对象权限和过滤参数；二者分别需查权限与具体查询端点。
- v1/v2 名词定义相同不能推出底层存储、读一致性或返回 envelope 相同。

## 复刻启示

- 画布的数据模型层只显示对象类型与连接定义；单个对象实例放入可切换的运行时图视图。
- schema 节点到对象实例视图需要明确关联本体、类型 API 名和具体主键，且读取接口服从字段权限。
