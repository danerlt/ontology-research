<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/marketplace-installation -->
<!-- 研读状态：已完成 -->

# Developer Console • Core concepts • Install an application with Marketplace • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/marketplace-installation)
- 官方中文来源：尚未发现直接对应页面（目录配对状态：missing）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；自定义应用与本体资源跨环境安装
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:05Z
- 产品状态：Compass-managed permissions 和源码模板化当前标注 Beta；安装兼容范围含限制

## 英文原文短摘录（不超过 25 词）

> “Installing an application from Marketplace automatically creates the Developer Console resource and configures OAuth.”

## 摘录译文

从 Marketplace 安装应用会自动创建 Developer Console 资源并配置 OAuth。

## 中文要点

- 分发有两种不同包型：应用包携带 Developer Console 配置和 OAuth client，适合交付已部署站点；源码包交付代码仓库，适合模板化或在目标环境新建应用。
- 应用包包含网站资产/CSP、元数据、OAuth client 和资源限制；Ontology 资源及 Compass 项目、子域名和安全 marking 作为安装依赖或参数。
- 安装会创建应用并配置 OAuth，但 Bootstrap 模式可能为避免冲突改写对象类型 API name；保持源 API name 可避免应用代码引用失效。子域托管通常仍需安全审批。
- 部分应用参数（Foundry URL、client ID、redirect URL、Ontology RID/API name）可由 meta tag 自动映射；对象类型和 Action 类型自身的 API name 不会自动映射。
- Compass-managed permissions 与源码模板化均为 Beta；独立 OAuth 客户端不可打包；应用 OSDK 中函数版本固定时当前不兼容；confidential client 在目标环境需重新生成 secret。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| application packaging | 应用打包 | 将 Developer Console 应用及其运行配置作为产品分发 |
| source code packaging | 源代码打包 | 把代码仓库作为模板或代码资产分发 |
| Bootstrap mode | 引导模式 | 安装产品时创建/初始化资源的模式 |
| parameter remapping | 参数映射 | 将源环境主机、ID 和本体标识替换为目标环境值 |

## 疑问与待验证项

- API name 的自动改写可能发生在 Bootstrap 模式；用户应对比当前目标本体冲突状态并评估代码是否硬编码 API name。
- 自动替换依赖 `index.html` meta tags 和脚手架版本；旧项目需按指南修改客户端初始化代码。
- Beta 可用范围、固定版本函数限制和 credential 轮换策略都可能变化；应在打包时查询目标 enrollment 能力。

## 复刻启示

- 发布产品包时保留两种安装工件：可部署应用包与源码模板包，分别声明依赖和升级行为。
- 安装前做跨环境 diff：资源 RID/API name、项目位置、OAuth 回调/类型、域名、分类和凭据逐项验证。
- 对映射失败、API name 冲突、需要重新生成 secret、人工域名审批和 Beta 权限迁移给出明确待办，安装不应静默部分成功。