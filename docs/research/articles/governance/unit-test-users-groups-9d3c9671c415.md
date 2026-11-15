<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/unit-test-users-groups -->
<!-- 研读状态：已完成 -->

# 函数 • Unit testing • 模拟用户和组 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-users-groups)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-users-groups)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:47Z
- 产品状态：TSv1 测试库提供 `createUser` 与 `createGroup` 构造部分 Principal mock；用户必需 ID 和 username，组必需 ID。

## 英文原文短摘录（每个来源不超过 25 词）

> “You are able to create a partial mock of a user using createUser, where all properties besides id and username are optional.”

## 摘录译文

可用 createUser 创建用户的部分 mock；除 id 和 username 外，其他属性都是可选的。

## 中文要点

- `createUser()` 和 `createGroup()` 来自 `@foundry/functions-testing-lib`；测试按需填写最少标识字段即可建立 Principal 夹具。
- 示例在函数中用 Users API 按 ID 查询用户/组，借助 Promise.all 并行取值，过滤不存在项后返回 Principal 列表。
- 模拟对象适合验证业务对用户、组身份对象的处理，不会真实查询组织目录。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Principal | 主体 | 用户或组等身份对象的统一类型 |
| `createUser` | 创建模拟用户 | 生成测试用 User 的 mock 工具 |
| `createGroup` | 创建模拟组 | 生成测试用 Group 的 mock 工具 |
| Users API | 用户目录 API | 通过 ID 查找 Foundry 用户和组的函数 API |

## 疑问与待验证项

- 单元测试模拟出的 User/Group 只覆盖指定属性，不验证真实组织目录同步、用户组成员关系或租户权限。
- 对象读取不同用户数据权限的行为需在权限集成测试中验证，不可由 Principal mock 推断。

## 复刻启示

- Agent 工具可在测试中模拟调用者 principal 和目标组，验证职责分配、通知收件人解析及访问策略分支。
- 持久化本体中把用户/组作为外部主体引用，避免复制账号凭据；身份同步和授权由独立身份服务提供。
- 审计记录使用稳定主体 ID，UI 仅展示用户可读名称且对无权查询的主体信息做脱敏。
