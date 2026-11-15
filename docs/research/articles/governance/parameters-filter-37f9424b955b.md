<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/parameters-filter -->
<!-- 研读状态：已完成 -->

# 动作类型 • Parameters • 筛选参数下拉菜单的结果 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameters-filter)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/parameters-filter)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:21Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Adding filters to non-object reference multiple choice or single object reference parameters will determine the allowed values that are selectable in the parameter's dropdown menu.”

## 摘录译文

为非对象引用的多选参数或单个对象引用参数添加筛选条件，可以限定下拉菜单中可选择的值。

## 中文要点

- 多选参数的选项可以从对象集中某个属性取值；生成选项时只使用当前用户有权查看的对象。若仅有一个可见关联对象且参数必填，系统可自动预填该属性值。
- 对象引用下拉可配置过滤条件和 Search Around，限定所有动作入口可选对象；提交前会再次验证选中值。下拉标题/显著属性展示服从对象类型可见性和用户对象权限。
- 静态属性过滤值存在元数据泄露风险：即使用户看不到对象，仍可能从动作定义或请求推断值；参数化筛选可以减少静态值暴露。
- 官方中文页标注为未经验证的 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object reference parameter | 对象引用参数 | 以本体对象作为动作输入。 |
| Search Around | 邻近搜索 | 按对象链接关系扩展可选对象集合的查询。 |
| Prominent property | 显著属性 | 对象选择项中用于辅助识别和搜索的属性。 |

## 疑问与待验证项

- 过滤值比较支持的类型、多个候选值的 OR/AND 语义及属性/参数来源需进一步核对同页“支持的操作”表格。
- 对象可见性之外的属性级权限如何应用到搜索结果排序/高亮，需结合安全文档和目标租户确认。

## 复刻启示

- 参数候选项必须服务端按用户权限计算，并在选择与最终提交时分别校验，防止客户端篡改 RID。
- 静态筛选中的敏感常量应触发风险提示；区分对象不可见与过滤元数据可见两个授权面。
