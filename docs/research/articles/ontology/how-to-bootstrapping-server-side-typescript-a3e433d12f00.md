<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-server-side-typescript -->
<!-- 研读状态：已完成 -->

# OSDK • 使用服务用户启动新的 Ontology SDK TypeScript 应用程序 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-server-side-typescript)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-server-side-typescript)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；服务用户、confidential OAuth client 与 OSDK
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:49Z
- 产品状态：后端服务示例；密钥轮换会中断仍使用旧密钥的应用

## 英文原文短摘录（不超过 25 词）

> “Developer Console will create a service user for this application based on the application name.”

## 摘录译文

Developer Console 会根据应用名称为该应用创建服务用户。

## 中文要点

- 在 Developer Console 创建 Backend service 应用，选择应用权限、生成 OSDK，并固定选择要包含的本体、对象类型和 Action 类型；生成 SDK 后不能再将关联本体切换成另一个本体。
- Developer Console 为应用创建服务用户；应用仍需显式获得对象读取权限和 Action submission criteria 所要求的权限。
- 示例使用 confidential OAuth client，以 client ID/secret 换取服务身份访问；Next.js 用来演示服务端取数，凭据不得写入仓库或浏览器端。
- 创建应用时 client secret 只显示一次；丢失后可轮换，但使用旧 secret 的现有应用会失效。通过 Marketplace 安装到目标环境后，需要在目标环境重新生成 secret。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| service user | 服务用户 | 代表应用执行后端读写的 Foundry 身份 |
| confidential client | 机密客户端 | 能在可信服务端安全持有 client secret 的 OAuth 客户端 |
| submission criteria | 提交条件 | Action 执行前需满足的授权条件 |
| client secret rotation | 客户端密钥轮换 | 生成新密钥并使旧密钥使用方需更新配置 |

## 疑问与待验证项

- 示例说明服务用户读取本体；实际写入仍取决于 Action 权限、提交条件和应用身份授权，不能从能读数据推断可写。
- 应用所选对象/Action 范围与服务用户权限是不同控制面，二者如何取交集需结合 Developer Console 权限页确认。
- 本页未描述密钥托管产品或无停机轮换策略；复刻实现需定义密钥版本与回滚机制。

## 复刻启示

- 后端服务应用应具有独立服务身份、OAuth 客户端凭据和显式资源清单；所有服务端调用均按服务身份做权限判定并记审计。
- 密钥仅在可信服务端存储，UI 只显示一次性凭据提示、轮换状态和依赖方影响，不回显现存 secret。
- OSDK 绑定本体后，将该绑定作为应用版本契约；改变本体需新版本或迁移提案，而非静默覆盖。