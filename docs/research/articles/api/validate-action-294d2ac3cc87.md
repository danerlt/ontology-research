<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions/validate-action -->
<!-- 研读状态：已完成 -->

# Validate Action • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions/validate-action)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:35Z
- 产品状态：v1 只读预验证 API；未通过不会应用变更

## 英文原文短摘录（每个来源不超过 25 词）

> “Validates if an action can be run with the given set of parameters.”

## 摘录译文

验证给定参数能否用于运行某个动作。

## 中文要点

`POST /api/v1/ontologies/{ontologyRid}/actions/{actionType}/validate` 会评估参数与 submission criteria，返回整体 `VALID`/`INVALID`、标准结果和逐参数评估。它是预检查，不应用动作变更。为性能考虑，它不读取 Foundry 现有对象或其他数据，因此不会检查主键唯一性、用户 ID 是否存在等；参数默认值当前不受支持，未提供的参数按 null 处理。第三方 OAuth2 调用反常规地使用只读范围 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Validate Action | 验证动作 | 执行前评估输入参数与提交条件 |
| Submission criteria | 提交条件 | 定义动作是否可提交的附加评估规则 |
| `VALID` / `INVALID` | 有效 / 无效 | 总体验证结果枚举 |
| Parameter evaluation | 参数评估 | 返回每个参数的校验结果和约束信息 |

## 疑问与待验证项

- 验证故意不检查实时对象状态，因此 `VALID` 不保证执行时仍满足唯一键或引用存在条件，也不保证提交成功。
- 文档说明参数默认值不支持、未指定参数为 null；需确认本地动作模型是否遵循此行为及如何向用户提示。

## 复刻启示

- 交互流程把“试算/验证”和“提交/执行”分成两个状态；UI 显示静态约束通过仍需运行时检查的提示。
- Agent 执行写操作前先调用验证工具并让用户确认；验证工具不能替代服务端最终授权和事务校验。
