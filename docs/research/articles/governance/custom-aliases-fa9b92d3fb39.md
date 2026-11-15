<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/custom-aliases -->
<!-- 研读状态：已完成 -->

# Functions • 自定义别名 • Custom aliases • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/custom-aliases)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:20Z
- 产品状态：TypeScript v2/Python 函数可读取命名配置别名，并在 Marketplace 安装时按环境重新映射。

## 英文原文短摘录（每个来源不超过 25 词）

> “Custom aliases are named references that store string values such as configuration parameters, feature flags, or environment-specific settings.”

## 摘录译文

自定义别名是存储配置参数、功能标志或环境专属设置等字符串值的命名引用。

## 中文要点

- 别名将函数逻辑与配置值解耦，适用于配置参数、功能开关和环境设置；key 在同一仓库必须唯一。
- 目前该教程给出 TypeScript v2 与 Python 用法，函数通过 alias key 读取配置值。
- 函数进入 Marketplace 产品后，别名自动成为可配置安装输入；安装者可在目标环境填写值或选预设，不用修改源码。
- 可为别名加入说明和允许的预设值，安装界面帮助使用者做出正确环境配置。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Custom alias | 自定义别名 | 按名称从环境配置读取的字符串值 |
| Alias key | 别名键 | 函数代码中用于解析配置的稳定唯一名称 |
| Marketplace preset | Marketplace 预设 | 安装者可选择的别名候选配置值 |

## 疑问与待验证项

- 别名值为字符串，敏感密钥能否以明文安全保存需确认；不应把别名等同于 Secret Store。
- 不同环境自定义别名的缺省值、校验和变更审计由安装资源策略决定，需另行核实。

## 复刻启示

- 函数源码只引用稳定 alias key，环境值由部署输入注入；区分普通配置、Feature Flag 和高敏凭据。
- Marketplace 安装表单展示参数说明、可用预设及值来源，并在修改配置后记录审计版本。
