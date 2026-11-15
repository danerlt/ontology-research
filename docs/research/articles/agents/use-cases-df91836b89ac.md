<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/use-cases -->
<!-- 研读状态：已完成 -->

# Pro-code agents • Use cases for pro-code agents • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/use-cases)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:15Z
- 产品状态：页面将常见模式分为本体数据 Agent、平台资源 Agent、迁移 Agent，并要求预先确定最少数据/工具及人工复核点。

## 英文原文短摘录（每个来源不超过 25 词）

> “Pro-code agents combine a large language model with the Ontology SDK (OSDK).”

## 摘录译文

Pro-code Agent 将大语言模型与 Ontology SDK（OSDK）结合。

## 中文要点

- 本体数据 Agent 由本体变更触发，经 OSDK/OMCP 读取对象、推理并写回；Automate 可配置对象变化触发。
- 平台资源 Agent 由平台事件触发，通过 Palantir MCP 检查或修改仓库、transform 等资源；示例以 pull request 交给开发者审阅。
- 迁移 Agent 组合前两类：将旧源码导入本体，分析既有逻辑，再创建 transform、function 与本体资源。
- 设计阶段需确定 Agent 目的、最少数据/工具及要求人工复核的输出/操作，并考虑隐私影响。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ontology data agent | 本体数据 Agent | 通过本体对象读写执行业务推理的 Agent。 |
| platform resource agent | 平台资源 Agent | 通过平台工具管理代码和数据资源的 Agent。 |
| human review | 人工复核 | 对高影响输出或变更加入人工审阅步骤。 |

## 疑问与待验证项

- - 这些模式是能力组合范式，不代表平台自动保证安全；每类工具仍需最小权限、审批和回滚。
- - 页面未为所有用例定义评估阈值，需按业务增加离线评估与运行监控。

## 复刻启示

- - 将本体工具与平台管理工具分组授权；支持事件触发、自动化编排、人审队列及 PR/提案式评审。
- - 为用例登记目的、数据/工具范围、风险级别、审批人和结果对象；高风险操作先生成变更提案。
