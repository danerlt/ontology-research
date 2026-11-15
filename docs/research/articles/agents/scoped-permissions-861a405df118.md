<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/scoped-permissions -->
<!-- 研读状态：已完成 -->

# Pro-code agents • Core concepts • Scoped permissions for pro-code agents • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/scoped-permissions)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:16Z
- 产品状态：当前文档描述模板代理对 OSDK、OMCP 与 Palantir MCP 的托管式范围权限。实际范围受发布时的本体绑定及底层应用限制共同约束。

## 英文原文短摘录（每个来源不超过 25 词）

> “The pro-code agent only has access to the resources permitted by its scope.”

## 摘录译文

Pro-code Agent 只能访问其权限范围允许的资源。

## 中文要点

- 使用 Agent 模板时，平台会配置调用 OSDK、OMCP、Palantir MCP 所需的运行时凭据和连接信息；业务代码无需自行提供 client ID、secret 或 Foundry token。
- 发布配置中的 Ontology binding 决定 Agent 连接的本体；底层客户端的 application restrictions 会继续约束资源访问，不能把“已连通”理解成默认全权限。
- 该托管身份路径不同于普通应用 OAuth 客户端或独立用户授权。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| scoped permissions | 范围权限 | 把 Agent 可调用的资源限制在明确范围内。 |
| Ontology binding | 本体绑定 | 发布时选择 Agent 读写的本体，并参与决定权限范围。 |
| application restrictions | 应用限制 | 施加在底层客户端上的额外访问限制。 |

## 疑问与待验证项

- - 页面没有列出每种 MCP 工具所需的完整应用限制；实现不能只靠前端工具列表做授权。
- - 凭据轮换、撤销与审计未在本页展开，应由身份和凭据子系统补充。

## 复刻启示

- - Agent 记录应绑定 project、ontology、服务身份和允许的工具；每次工具调用都需在后端执行资源级鉴权。
- - 将本体绑定及 API scope 纳入发布审阅，审计记录操作者、调用工具与资源，不记录密钥值。
