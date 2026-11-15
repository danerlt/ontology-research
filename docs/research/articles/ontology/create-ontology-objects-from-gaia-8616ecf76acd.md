<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-link-types/create-ontology-objects-from-gaia -->
<!-- 研读状态：已完成 -->

# Object and link types • Object types • Create Ontology objects from Gaia • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-link-types/create-ontology-objects-from-gaia)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：object-link-types
- 相关性：direct；地理应用通过本体类型/接口创建对象的工作流
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:48Z
- 产品状态：页面含新旧接口迁移说明；Gaia Geocreatable 等旧接口已弃用

## 英文原文短摘录（每个来源不超过 25 词）

> “Gaia can discover object types backed by a dataset or restricted view after they implement the `Gaia Geoshape Creatable` interface.”

## 摘录译文

对象类型在实现 `Gaia Geoshape Creatable` 接口且由数据集或受限视图支持后，Gaia 才能发现它们。

## 中文要点

- 将地图绘制产生的形状/点转成 Ontology 对象，需要对象类型实现对应的可创建接口，并有 dataset 或 restricted view 作为后端；创建还需要满足接口约束的 Action type。
- Gaia 面向对象类型列出其实现的接口，并据接口能力显示点、形状或符号工具。对象字段示例包括 Geoshape 和 Object ID；受限视图场景还需 Classification 字段以支持分类访问。
- 文档区分 `Creatable Geoshape`/`Creatable Geopoint` 与 `Gaia Geoshape Creatable`/`Gaia Geopoint Creatable`：新接口支持 interface Action type constraint；旧 Gaia 专用接口在当前文档中处于计划弃用阶段，旧 `Gaia Geocreatable` 已弃用。旧接口不定义该约束时，类型和 Action 需要在 Gaia 管理应用或 Control Panel 扩展中手动注册。
- 安装 Marketplace 接口时要映射共享属性、配置权限/分类与 schema migration；仅在旧 Gaia 接口场景需要安装旧产品依赖。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Creatable interface | 可创建接口 | 使地理绘制工具能匹配特定对象类型 |
| Restricted view | 受限视图 | 支持按分类或 marking 控制数据访问的后端视图 |
| Interface action type constraint | 接口动作类型约束 | 使创建对象的 Action 满足接口要求 |
| Geoshape | 地理形状 | Gaia 绘制并写入对象的空间属性 |

## 疑问与待验证项

- 页面注明新 `Creatable` 接口按计划在 2026 年 11 月前取代旧 Gaia 专用接口；具体迁移日期、版本支持和部署 enrollment 的 Marketplace 可用性需在平台中确认。
- 跨国际日期变更线的对象形状创建存在限制；其他空间参考系统/几何有效性校验需查 Gaia 文档。
- 受限视图、classification 和 marking 的授权如何传递给地图编辑操作，应结合权限专题逐项验证。

## 复刻启示

- 画布可接入地图绘制器作为专用编辑视图：空间对象类型声明支持点/线/面能力，界面根据类型能力启用相应绘制工具。
- 通过可复用接口和 Action 约束声明对象创建能力，避免把 Gaia UI 行为硬编码到对象类型名称。
- 创建时同时校验对象主键、几何字段、分类字段、后端视图权限和动作约束，并将地图提交记录纳入本体对象编辑审计。
