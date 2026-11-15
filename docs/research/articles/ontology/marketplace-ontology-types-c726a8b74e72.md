<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/object-link-types/marketplace-ontology-types -->
<!-- 研读状态：已完成 -->

# 对象链接类型 • 将Object和链接类型添加到Marketplace产品 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-link-types/marketplace-ontology-types)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-link-types/marketplace-ontology-types)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：object-link-types
- 相关性：direct；本体对象链接类型文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:57Z
- 产品状态：Marketplace 本体类型打包能力说明；存在未支持的属性类型清单

<!-- 研读状态：已完成 -->
# 英文原文短摘录（每个来源不超过 25 词）

> “Objects themselves cannot be packaged with Marketplace.”

## 英文原文短摘录（每个来源不超过 25 词）

> “Use Foundry DevOps to include your object and link types in Marketplace products for other users to install and reuse.”

## 摘录译文

可使用 Foundry DevOps 将对象类型和链接类型纳入 Marketplace 产品，供其他用户安装和复用。

## 中文要点

- Foundry DevOps 的 Marketplace 产品可打包对象类型、链接类型、共享属性类型和接口，供其他用户安装复用。
- 对象实例和 Action 产生的编辑数据不会打入产品；数据集与对象类型可以打包，让安装后再创建对象。
- 当前英文页列出 Cipher、Geo time、Vector 属性类型尚不支持；无数据源对象类型可以被打包。
- 可直接添加链接类型，但官方建议先加对象类型，再从信息面板选择相关链接，便于管理资源依赖。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Marketplace product | Marketplace 产品 | 可分发、供其他用户安装的资源包 |
| Ontology entities | 本体实体 | 可打包的对象类型、链接类型等 schema |
| Shared property type | 共享属性类型 | 可供多个对象类型复用的属性定义 |
| Backing datasource | 后端数据源 | 支撑对象类型实例化的数据集或来源 |

## 疑问与待验证项

- 不支持清单随产品更新；Cipher、Geo time 和 Vector 是否已在目标 enrollment 开放需核验。
- 本页未详述跨环境 RID 重映射、版本升级冲突与实例数据迁移策略。

## 复刻启示

- 区分可分发的模型定义与运行对象数据，产品包不自动复制实例。
- 打包前执行依赖闭包检查：对象类型、链接、共享属性、接口与数据源应列入可审查清单。