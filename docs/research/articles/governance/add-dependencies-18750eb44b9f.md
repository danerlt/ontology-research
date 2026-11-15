<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/add-dependencies -->
<!-- 研读状态：已完成 -->

# 函数 • TypeScript basics • 添加 npm 依赖项 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/add-dependencies)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/add-dependencies)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:43Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “The following documentation is specific to TypeScript v1 functions.”

## 摘录译文

以下文档专门介绍 TypeScript v1 函数。

## 中文要点

- 本页针对 TypeScript v1 函数仓库；仓库用 npm 管理依赖，但函数运行时不支持依赖 Node.js 运行时或系统调用的包。
- 默认不允许从公共 npm registry 获取依赖，管理员/仓库需先启用；Code Repositories Libraries 面板会更新 `package.json` 与 lockfile，并可导入支持仓库资源。
- 旧模板版本可能不能通过 task runner 安装，需手动修改版本、提交并重启 Code Assist。文档建议迁移 TSv2 获得更完整的 Node.js/OSDK 能力。
- 官方中文页标注为未经验证的 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Pure JavaScript library | 纯 JavaScript 库 | 运行时可加载且不依赖 Node.js 系统调用的库。 |
| npm registry | npm 注册表 | 外部 JavaScript 包分发源。 |
| Lockfile | 锁文件 | 固定依赖解析结果的文件。 |

## 疑问与待验证项

- 公共 registry 开放策略、允许的依赖源和安全扫描要求取决于平台管理员设置，本文未给出统一配置。
- “纯 JavaScript”兼容边界需要逐包验证；安装成功不保证运行时可用。

## 复刻启示

- 依赖安装流程应支持来源白名单、版本固定、锁文件与漏洞扫描，并在构建环境隔离外部网络访问。
- 函数语言/运行时要声明可用系统能力，CI 对含原生扩展或系统调用的依赖提前失败并给出原因。
