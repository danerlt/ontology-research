<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/deploy-custom-application-on-foundry -->
<!-- 研读状态：已完成 -->

# Developer Console • Core concepts • Hosting an application on Foundry • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/deploy-custom-application-on-foundry)
- 官方中文来源：[候选中文页（旧 OSDK 部署路由，待人工确认）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/deploy-osdk-application-on-foundry)
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；本体 SDK 前端应用托管和发布
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:00Z
- 产品状态：托管受应用类型及 enrollment 支持范围限制；外部管理域名需额外配置和支持

## 英文原文短摘录（不超过 25 词）

> “Website hosting is only available for applications configured as a Client-facing application.”

## 摘录译文

网站托管仅适用于配置为面向客户端应用的应用。

## 中文要点

- 托管目标是 OSDK 前端应用；Backend service 会创建 confidential client，因此控制台不提供网站托管，面向客户端应用需使用 public client。
- 默认在 enrollment 域名下申请应用子域；申请后不能直接编辑，需取消旧请求再重新提交，并由有权限的安全负责人批准。
- 可申请自有域名，但需先配置域名证书；部分 enrollment 或合规环境不支持默认托管，需要支持团队、DNS、TLS 和网络入口协同配置。
- 网站资源可在 Developer Console UI 上传，也可用 `@osdk/cli` 部署；首次部署可能受站点资源扫描状态阻塞，等待扫描完成后重试。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Client-facing application | 面向客户端的应用 | 提供浏览器前端并采用公共 OAuth 客户端 |
| website hosting | 网站托管 | 为应用构建资产提供 Foundry 域名访问入口 |
| enrollment subdomain | enrollment 子域 | 在 Foundry enrollment 域名下分配的应用域名 |
| site asset scanning | 站点资源扫描 | 初次发布前对网站资产进行扫描的任务 |

## 疑问与待验证项

- 中文候选页使用旧 OSDK 路由；本文英文页已位于 Developer Console，需人工确认候选内容是否完整覆盖当前域名、CLI 和环境限制。
- 域名审批、证书、网络入口和支持范围取决于 enrollment；公开文档未保证所有环境可使用自定义域。
- 页面没有给出所有资产上传类型、最大包体和发布回滚策略，需结合 CLI/API 参考核对。

## 复刻启示

- 应用托管配置需校验应用类型、公私客户端、域名能力、TLS 证书和审批状态，并在发布前报告阻塞原因。
- 域名申请应采用不可变请求记录，修改域名走取消/重提并保留批准人、证书和生效状态。
- 将构建产物版本、发布扫描和生产指向关联到应用版本，首发失败可等待扫描或安全重试。