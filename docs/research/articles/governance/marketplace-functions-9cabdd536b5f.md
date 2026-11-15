<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/marketplace-functions -->
<!-- 研读状态：已完成 -->

# Functions • Function management • Functions in Marketplace • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/marketplace-functions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/marketplace-functions)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:31Z
- 产品状态：Stable mode 为 Beta；扩展函数执行需目标项目获管理员许可。

## 英文原文短摘录（每个来源不超过 25 词）

> You can use Foundry DevOps to include your functions in Marketplace products for other users to install and reuse.

## 摘录译文

可通过 Foundry DevOps 将函数加入 Marketplace 产品，供其他用户安装和复用。

## 中文要点

- 打包函数时选择函数与版本；模型函数会携带模型版本/部署依赖，目标环境部署必须处于运行状态才能处理推理请求。
- 代码仓库默认作为函数依赖输出，但产品通常不需要附带源码执行；需要扩展执行能力（例如函数内调用 Action 或取长时令牌）时，管理员须把目标项目加入 allowlist。
- Marketplace 有历史默认的去重模式，以及 Beta 的 stable mode；两者对函数版本/API 名冲突的处理不同。已发布函数版本不可变，API 名在 Ontology 内唯一。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Marketplace product | Marketplace 产品 | 可安装、升级及复用的一组发布资源。 |
| Deduplication mode | 去重模式 | 安装冲突时递增版本或对 API 名添加序号的默认策略。 |
| Stable mode | 稳定模式 | Beta 安装策略，保留打包版本与 API 名；冲突可能导致安装失败。 |

## 疑问与待验证项

- stable mode 当前处于 Beta 且可能需平台支持启用；每个 enrollment 的可用状态需单独确认。
- 打包模型部署、仓库源码和执行环境配置的具体要求随产品类型而异，安装前应按依赖逐项预检。

## 复刻启示

- 为本体/函数包记录不可变版本、依赖闭包、目标环境资源映射与安装冲突策略，安装前出具差异预览。
- 把高权限执行能力做成管理员显式许可的项目 allowlist，并审计授权人、安装实例及调用范围。
