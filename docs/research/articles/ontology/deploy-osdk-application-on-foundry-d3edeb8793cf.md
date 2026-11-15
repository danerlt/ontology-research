<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/deploy-osdk-application-on-foundry -->
<!-- 研读状态：已完成 -->

# OSDK • 在 Foundry 上部署一个 Ontology SDK 应用 • Palantir

- 英文原文：[迁移后的英文页面](https://www.palantir.com/docs/foundry/developer-console/deploy-custom-application-on-foundry)
- 官方中文来源：[中文原文](https://www.palantir.com/docs/zh/foundry/ontology-sdk/deploy-osdk-application-on-foundry)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；OSDK 前端应用的静态网站托管与发布流程
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:43Z
- 产品状态：托管功能范围与域名审批依 Foundry enrollment/管理员策略

## 英文原文短摘录（每个来源不超过 25 词）

> “Web hosting only supports serving static assets and does not support running a server.”

## 摘录译文

网页托管只支持提供静态资源，不支持运行服务器。

## 中文要点

- Developer Console 网站托管面向仅含前端的 OSDK 应用，不需要额外网站服务器；只能托管静态构建产物，不能运行后端进程。当前英文对应页支持 Foundry enrollment 子域或自有域名，旧中文路由重点描述子域申请。
- 部署前准备 SPA 路由/404 处理和认证回调 URL；打包 `dist/` 等构建目录中的文件，不要把目录本身包进压缩文件。
- 在 Developer Console 申请托管域名并按组织审批要求等待域名就绪；可通过 UI 上传 ZIP 或 `@osdk/cli` 上传资产，先预览再发布生产版本。
- 网站访问要求 Foundry 登录凭证；默认仅有 Developer Console 应用权限的人可访问，可在 Sharing & Tokens 中添加用户。页面也提供 CSP 配置，但放宽规则会增加 XSS/数据注入风险。
- 中文内容提醒其为 AIP 机器翻译且准确性未验证；旧 OSDK 路由现重定向到新的 Developer Console 托管文档。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Static assets | 静态资源 | 托管服务可发布的网页构建文件 |
| Hosted subdomain | 托管子域 | Foundry 注册域下应用访问地址 |
| Redirect URL | 重定向 URL | OAuth 登录完成后的应用回调地址 |
| Content Security Policy | 内容安全策略 | 控制应用可加载脚本/资源的浏览器策略 |

## 疑问与待验证项

- Foundry stack 域名不以 `.palantirfoundry.com` 结尾时，文档称需联系支持协调配置；自托管和私有部署情况需另查。
- 域名请求审批和分享权限可由不同管理员角色处理，具体授权由当前 enrollment 决定。
- CSP 页面警告自定义策略未验证，需在部署前按具体外部 API/图像资源做安全审查。

## 复刻启示

- 静态 OSDK 前端与 Python/FastAPI 微服务应拆分部署：前端托管服务只提供静态资源，服务端 API 使用独立容器/域名和认证策略。
- 发布流水线支持预览、审批、正式发布与回滚，并将子域、OAuth 回调、CSP 和应用访问名单作为可审计配置。
- 多项目管理中，网站身份与本体访问权限应绑定同一个应用/项目边界；SPA 无服务端不等于可以把敏感凭证写入前端。
