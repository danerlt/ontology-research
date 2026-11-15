<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/api-ontology-edits -->
<!-- 研读状态：已完成 -->

# 函数 • Ontology edits • API: Ontology编辑 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/api-ontology-edits)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:52Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：Ontology edit functions must be configured as an Action, known as a function-backed Action.

> 中文译文：本体编辑函数必须配置为 Action，也称函数支持的 Action，才能在操作环境中使用。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- TSv1 编辑函数需使用 `@OntologyEditFunction()`、声明 `void` 返回值，并用 `@Edits([object type])` 指明写入对象类型；仅运行编辑函数而不经 Action 不会修改对象数据。
- 可直接重新赋值属性；数组属性必须复制后整体替换；现有对象主键不可更改。SingleLink/MultiLink 提供 set/clear/add/remove 等链接更新操作。
- 创建对象必须指定主键；函数内应用编辑后再读取同一属性/链接可以观察到变更，但搜索结果可能受索引/一致性时序影响。
- 本页为 TSv1 专属 API；新实现应对照 TSv2 页面和 OSDK。本体写入的权限与操作化入口来自 Action。中文机翻未验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OntologyEditFunction | 本体编辑函数 | 在函数中构造本体对象/关系变更的专用函数声明。 |
| Edits decorator | 编辑对象声明装饰器 | 标记编辑函数计划触及的对象类型。 |
| Function-backed Action | 函数支持的 Action | 将编辑函数纳入操作权限、元数据和应用入口的动作类型。 |

## 疑问与待验证项

- TSv1 和 TSv2 的暂存写、读后写及失败原子性有差异；迁移时需查新版 staged writes 与 Action 隔离文档。
- 执行编辑后立即搜索可能返回旧数据，需区分对象编辑提交、搜索索引传播和读取快照。

## 复刻启示

- 禁止绕过 Action 直接写对象；将函数作为逻辑实现、Action 作为授权/校验/审计外壳。
- 写集 schema 标明目标对象类型、属性与关系；编辑数组采取整值替换并禁止主键变更，发布前校验兼容性。
