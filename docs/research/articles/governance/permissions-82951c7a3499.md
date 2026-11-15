<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/permissions -->
<!-- 研读状态：已完成 -->

# OSDK • 权限 • Palantir

- 英文来源：[旧版英文路由（现为 404）](https://www.palantir.com/docs/foundry/ontology-sdk/permissions)；[现行 Developer Console 权限文档](https://www.palantir.com/docs/foundry/developer-console/permissions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/permissions)（中文路由译文以英文原文复核）
- 页面语言：中文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:01:03Z
- 产品状态：官方中文页面声明 AIP 机器翻译准确性未经验证；英文旧路由返回 404，当前英文规范已迁至 Developer Console。

## 原文短摘录与翻译

> “资源访问范围确保用户只能访问通过给定 OAuth 令牌批准的资源。”

本页中文摘录来自官方 AIP 机器翻译；英文旧路由已失效。

## 摘录译文

该摘录来自官方中文页面的 AIP 机器翻译；旧英文路由现返回 404，无法逐句核对。当前英文权限文档已迁至 Developer Console，并描述 Compass 管理的新权限模型。

## 中文要点

- 保留的中文页描述 Developer Console 应用 Viewer/Editor/Owner 角色，以及用户权限（授权码流程）与应用权限/服务用户（客户端凭据流程）的区别。
- 面向客户端的应用必须使用用户权限；应用权限使用生成的服务用户。前端客户端凭据不可存于客户端。
- SDK 配置内的对象、链接、动作和函数及其依赖会进入 OAuth 资源访问范围；依赖变化或 SDK 删除资源后，需要审查范围并安排清理。
- 旧英文 `/ontology-sdk/permissions` 已返回 404；当前英文页转为 Developer Console 权限说明，Compass 管理的用户权限标注 Beta，并明确应用继承项目权限。新旧角色/迁移行为不能混作同一版本。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| user permissions | 用户权限 | 按登录用户既有本体权限读取/写入。 |
| application permissions | 应用权限 | 由应用对应的服务用户授权访问。 |
| resource access restrictions | 资源访问范围 | 限定 OAuth 应用 token 可触达的资源及依赖。 |
| authorization code grant | 授权码授予 | 通常供面向用户的前端应用委托用户身份。 |
| client credentials grant | 客户端凭据授予 | 服务端应用以应用服务身份获取 token。 |

## 疑问与待验证项

- 官方中文页明确声明 AIP 机器翻译准确性未经验证；英文旧路由已失效，当前 Developer Console 文档的 Compass 用户权限属于 Beta，角色继承规则与本页旧版表述不同。
- 具体部署是否启用了 Compass 管理权限、资源依赖如何同步，以及服务用户的身份映射，需按 enrollment 和应用类型核实。

## 复刻启示

- 应用接入至少分为终端用户委托授权与后端服务身份两种模式；不向浏览器发放客户端密钥。
- 把 token 资源范围、依赖闭包和实际主体数据权限作为相交约束；SDK 生成资源变化时做差异预览和人工确认。
- 对文档保留版本/迁移状态，明确旧 API 路径和现行规范，避免以旧权限说明覆盖当前部署策略。
