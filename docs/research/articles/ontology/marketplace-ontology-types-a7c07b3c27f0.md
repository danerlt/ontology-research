<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-link-types/marketplace-ontology-types -->
<!-- 研读状态：已完成 -->

# Object and link types • Add Ontology types to a Marketplace product • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-link-types/marketplace-ontology-types)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-link-types/marketplace-ontology-types)（目录配对状态：matched）
- 页面语言：英文
- 主题栏目：object-link-types
- 相关性：direct；本体对象、链接、共享属性和接口的产品化分发
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:49Z
- 产品状态：Marketplace 对部分属性值类型有限制；对象实例本身不随产品打包

## 英文原文短摘录（不超过 25 词）

> “Objects themselves cannot be packaged with Marketplace.”

## 摘录译文

Marketplace 不能直接打包对象实例本身。

## 中文要点

- 通过 Foundry DevOps 将对象类型和链接类型作为 Marketplace 产品内容；添加对象类型后，界面会推荐其相关链接类型。
- 产品还可包含 Shared property 和 Interface 类型；本体类型可连同数据集和依赖资源分发，以便安装后创建新对象。
- 对象实例和 Action 修改产生的具体编辑不随产品打包，因此产品发布的是 schema/资源能力而非某一时刻的业务记录快照。
- Cipher、Geo time 和 Vector 属性暂不支持 Marketplace 产品；无数据源 backing 的对象类型则支持。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| object type | 对象类型 | 定义对象实例字段和语义的本体类型 |
| link type | 链接类型 | 连接两类对象实例的关系 schema |
| shared property | 共享属性 | 可由多个对象类型复用的统一属性定义 |
| Marketplace product | Marketplace 产品 | 可安装复用的应用、资源和本体定义集合 |

## 疑问与待验证项

- 不支持的属性类型清单可能随产品升级而变化；发布时应检查最新限制。
- 文档只说明 schema 与实例打包边界，没有完整列出 backing datasource 的所有依赖闭包和安装顺序。
- Marketplace 安装后的对象创建依赖目标环境数据与 Action，不能把安装成功等同于实例数据已迁移。

## 复刻启示

- 产品包应区分 Ontology 定义、数据源/转换依赖、应用资源和运行时对象实例；默认不把业务记录嵌入 schema 包。
- 打包前执行类型能力兼容检查，逐属性指出 Vector、Cipher、Geo time 等限制，并解析链接/共享属性依赖。
- 安装后以目标环境实际数据创建对象，生成独立运行状态与来源记录。