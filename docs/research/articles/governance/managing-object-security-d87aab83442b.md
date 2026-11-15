<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/object-permissioning/managing-object-security -->
<!-- 研读状态：已完成 -->

# 对象权限管理 • 管理Object类型和Object实例安全性 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/managing-object-security)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning/managing-object-security)（目录记录为官方中文页）
- 页面语言：中文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：2026-11-12T17:46:46.936Z
- 目录核对时间：2026-11-14T15:00:01Z
- 产品状态：中文页标注为未经验证的机器翻译，重点仍是数据源、RVs 和 MDOs；英文现行文档还推荐对象/属性安全策略用于多数本体内访问控制。

## 原文短摘录与翻译

> “Foundry受限视图（RVs）提供行级访问控制，MDOs则为列或属性级别访问控制提供解决方案。”

## 摘录译文

**英文对应原文：** “Both approaches support cell-level security, which is a combination of row and column level security.”

## 中文要点

- 中文页将安全说明分为输入数据源权限与细粒度访问控制：dataset/stream 权限影响实例可见性，restricted view 用于行级策略，MDO 用于按来源列控制属性值。
- 多来源数据的对象实例可以共享同一类型；没有相关来源权限时，用户无法访问该来源映射的属性。
- 英文现行页面补充 object/property policies 的 cell-level 管理、read-time only 范围、branching 和 streaming 支持，并建议在本体内大多数场景优先考虑该方式。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| multi-datasource object type | 多数据源对象类型 | 多个来源数据集向一个对象类型提供字段。 |
| restricted view | 受限视图 | 在来源数据集层执行行级访问控制。 |
| object/property security policy | 对象/属性安全策略 | 在本体类型层执行行级、列级权限检查。 |

## 疑问与待验证项

- 中文页面内容与英文现行文档的推荐路线并不完全同步；本项目应按英文页核对新策略，同时保留旧式 MDO/RV 作为原始数据在本体外复用的选择。
- 对 media reference 等外部资源，字段权限不能代替媒体存储自身的访问控制。

## 复刻启示

- 权限边界需要分开建模：原始 dataset/stream、对象行、属性列、derived path、导出结果和附件存储。
- 在配置界面提示权限检查的阶段、失败后对调用方呈现 null 还是隐藏对象，以及下游传播范围；为多来源字段提供可审计策略链。
