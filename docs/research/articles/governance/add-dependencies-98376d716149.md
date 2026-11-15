<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/add-dependencies -->
<!-- 研读状态：已完成 -->

# Functions • 添加 npm 依赖 • Add npm dependencies • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/add-dependencies)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/add-dependencies)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:07Z
- 产品状态：本文针对 TypeScript v1；运行时只支持纯 JavaScript 库，文档建议迁移到 TypeScript v2 获得更完整能力。

## 英文原文短摘录（每个来源不超过 25 词）

> “The functions runtime only supports pure JavaScript libraries.”

## 摘录译文

Functions 运行时只支持纯 JavaScript 库。

## 中文要点

- Functions 仓库使用 npm 管理依赖；可用于数值/日期处理、统计和 XML 等数据格式。
- 默认不从公共 npm registry 拉取依赖，需先在 Code Repositories 为仓库启用；随后可在 Libraries 侧栏选择依赖和 dependencies/devDependencies。
- 若依赖仓库尚未导入，添加依赖的流程会提示导入资源，并同步更新 package.json 与 package-lock.json。
- 依赖若依赖 Node.js 运行时或系统调用则不受支持；官方明确说明这是 TypeScript v1 专页，并推荐转向 v2。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| npm dependency | npm 依赖 | Functions 仓库声明并安装的第三方/平台包 |
| Public npm registry | 公共 npm 注册表 | 外部依赖下载源，默认未启用 |
| Pure JavaScript library | 纯 JavaScript 库 | 不依赖 Node 运行时或系统调用的库 |

## 疑问与待验证项

- 允许公共 npm 下载会改变仓库供应链边界，组织如何审批与锁定版本需结合安全配置确认。
- 若包依赖原生扩展或系统调用，当前运行时限制如何表现、部署时何处报错需实测。

## 复刻启示

- 依赖管理应在应用构建前执行许可/运行时兼容校验，并保存锁文件与可复现依赖快照。
- 把平台能力按函数版本显式标注；TSv1 的限制和新能力优先路线不可混为一套运行时。
