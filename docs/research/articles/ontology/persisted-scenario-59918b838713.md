<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/persisted-scenario -->
<!-- 研读状态：已完成 -->

# Store scenario metadata as objects • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/persisted-scenario)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:06Z
- 产品状态：页面标注 Beta；通过 Ontology Scenario interface 把 scenario reference 存为对象主键，可持久化、共享、审批并沿用对象权限。

## 英文原文短摘录（每个来源不超过 25 词）

> “When stored in the Ontology, scenarios are shareable and collaborative.”

## 摘录译文

Scenario 元数据存储在本体后，场景即可共享与协作。

## 中文要点

- 每个持久 Scenario 对应一个 Ontology 对象；配置对象类型时实现 Ontology Scenario interface，并把 Scenario Reference 映射为主键。可添加描述、作者、状态、审核人等元数据。
- Scenario 的 Expiration Time 最多只能延至当前时间后 31 天；未设置时使用默认生命周期。
- 可把临时场景保存成对象，再以对象列表管理和选择场景；对象安全策略与 Action submission criteria 用于控制查看、提交、批准和拒绝。
- 文档给出 Draft、In review、Approved、Rejected 状态流程；创建者提交，审批组审核，也可在批准 Action 中同时应用场景编辑。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| persisted scenario | 持久场景 | Scenario reference 和协作元数据存入本体对象。 |
| Scenario Reference | 场景引用 | 标识 scenario 的值类型，可映射为对象主键。 |
| object security policy | 对象安全策略 | 按创建者/审批组等条件控制场景对象的访问。 |

## 疑问与待验证项

- - 本体对象存的是 Scenario reference 和元数据；scenario 的隔离编辑生命周期仍受场景本身 TTL 管理，不能把对象永久性误当作场景数据永久保留。
- - 多租户复刻需把 project、scenario 对象 ACL 和可应用目标统一校验，并设置过期/归档动作。

## 复刻启示

- - 持久场景可作为可分享的工作对象，保留 owner、描述、基线、过期时间、审批状态、reviewer 和关联领域对象。
- - 评审状态变更通过受控 Action 进行；审批操作可和场景 merge 组合，但必须使用服务端 submission criteria 和对象级权限。
