<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/unit-test-users-groups -->
<!-- 研读状态：已完成 -->

# Functions • Unit testing (TSv1) • Mock users and groups • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-users-groups)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-users-groups)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:27Z
- 产品状态：TSv1 Jest 测试辅助；createUser 仅要求 id 和 username，createGroup 仅要求 id。

## 英文原文短摘录（每个来源不超过 25 词）

> “You are able to create a partial mock of a user using `createUser`”

## 摘录译文

可使用 createUser 创建部分用户 mock。

## 中文要点

- `createUser` 可构造用户部分 mock，必填字段为 id 和 username；其余属性可省略。`createGroup` 的必填字段只有 id。
- 使用 mock 可验证查询用户/组的函数如何过滤缺失主体、组合 Principal 返回集合或写入编辑，不依赖真实目录数据。
- 这些对象是测试输入/返回值，不会为测试调用者授予 Foundry 用户或组权限，也不验证真实授权目录响应。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| createUser | 创建用户 mock | 构造测试用部分用户主体对象。 |
| createGroup | 创建组 mock | 构造测试用部分组主体对象。 |
| Principal | 主体 | Foundry 用户或组可共同返回的抽象类型。 |

## 疑问与待验证项

- 仅有 id/name 的部分 mock 不覆盖用户属性、标记和组织成员关系；访问这些字段时需要补齐样例。
- 单测通过不能证明生产环境当前用户对某对象/Action 的权限。

## 复刻启示

- 权限测试同时包含 user/group 主体对象、项目成员关系和对象策略结果；不把身份数据 mock 当授权验证。
- Agent/Action 的授权拒绝用例需分别验证 user、service user、group membership 与 token resource scope。
