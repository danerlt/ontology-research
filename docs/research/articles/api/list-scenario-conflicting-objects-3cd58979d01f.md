<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-scenarios/list-scenario-conflicting-objects -->
<!-- 研读状态：已完成 -->

# List Scenario Conflicting Objects • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-scenarios/list-scenario-conflicting-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-scenarios
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:12Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “A conflict occurs when an object has been edited both within the scenario and on the scenario's base after the scenario was created.”

## 摘录译文

若对象在情景内和情景创建后的基线中都被编辑，就会产生冲突。

## 中文要点

- 接口按指定对象类型列出与情景基线编辑冲突的对象；只返回当前用户有权查看的对象。
- 检测会使用未体现在用户可见对象数据中的变化，因此可能误报：对象数据看起来未变，也可能被列为冲突。
- `pageSize` 限制每次调用为查找冲突而检查的对象数，不保证返回同样数量的冲突项；端点为 Preview 且需要 `preview=true`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Conflicting object | 冲突对象 | 情景和情景基线均发生编辑的对象 |
| False positive | 误报 | 技术检测提示冲突但可见数据未变 |
| Page size | 页大小 | 限制检查工作量而非结果条数 |

## 疑问与待验证项

- 文档没有给出可消解冲突的逐字段三方合并 API；列表仅定位对象，不提供解决决策。
- 权限不可见对象是否会影响冲突计数或分页，需通过用户权限矩阵实测。

## 复刻启示

- 将冲突视作候选提示，提供逐对象并排比较与人工确认，不可自动覆盖或直接阻断所有发布。
- 结果分页可能短于 pageSize，读取必须依 nextPageToken；显示“已检查数量”和“已发现数量”两种统计以免误读。
