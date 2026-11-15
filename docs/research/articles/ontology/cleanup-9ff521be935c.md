<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-manager/cleanup -->
<!-- 研读状态：已完成 -->

# Ontology Manager • Ontology cleanup • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/cleanup)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-manager/cleanup)
- 页面语言：英文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：Ontology cleanup 工具；页面描述其清理队列与标记规则。

## 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology cleanup tool is a safe way to delete object types.”

## 摘录译文

Ontology cleanup 工具用于更安全地删除对象类型。

## 中文要点

- 清理队列按可配置标记发现疑似过期对象类型，可按标记和类型分组筛选并按优先级排序。
- 处理方式包括仅对当前操作者隐藏一段时间的 snooze、设置全局 deprecated 状态及可选期限，或删除对象类型；清理决策按普通本体变更暂存并提交/提案评审。
- 标记示例包括弃用日期已过、来源数据集被删除、来源长期未更新、缺少描述、名称命中特定正则等。自定义标记设置是个人配置。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| snooze | 暂缓提醒 | 只影响当前用户清理队列的暂时隐藏。 |
| deprecate | 标记弃用 | 提示使用方迁移，可带预定删除日期。 |
| cleanup flag | 清理标记 | 检测潜在维护问题并排序的规则。 |

## 疑问与待验证项

- 删除会移除对象存储中的相关数据；执行前需要确认对象是否有用户编辑、动作或应用依赖。
- 若选择自定义标记，今后新增的默认规则不会自动启用，因此需要清理规则版本和治理责任人。

## 复刻启示

- 建立只读的清理建议队列，先展示命中规则、依赖数量、数据状态和潜在破坏影响。
- 弃用与删除分成两步，删除前检查引用并生成资源级变更单；暂缓提醒按用户而非全局保存。
