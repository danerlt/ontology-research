<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk-react-applications/troubleshooting -->
<!-- 研读状态：已完成 -->

# 本体SDK React应用 • 故障排除 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/ontology-sdk-react-applications/troubleshooting)
- 官方中文来源：[官方中文页（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/ontology-sdk-react-applications/troubleshooting)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk-react-applications
- 相关性：direct；OSDK React 开发环境和依赖故障
- 官方更新时间：2026-11-12T17:46:46.930Z
- 目录核对时间：2026-11-14T15:00:41Z
- 产品状态：排障参考；网络和依赖仓库配置随 enrollment 而异

## 英文原文短摘录（不超过 25 词）

> “Code Repositories requires your dependencies to be explicitly declared.”

## 摘录译文

Code Repositories 要求显式声明项目依赖。

## 中文要点

- 页面聚焦在平台内 VS Code/Code Repositories 中开发 OSDK React 应用时的常见错误；排查 npm 命令问题时，可先删除 lock 文件和 `node_modules` 后重装，或暂停并恢复工作区。
- 默认 npm 仓库包含常见 OSDK 包、外部 npm 镜像和应用专属 SDK 制品仓库；依赖需要存在于其中一个后端仓库。
- 私有 npm 包需先作为 Artifact 出现在可用仓库中；否则安装会报找不到模块。
- `E401` 不一定是凭据错误：若工作区无法访问 npmjs.com，也可能表现为“密码缺失或错误”。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| dependency declaration | 依赖声明 | 仓库需要知道项目需要安装哪些包 |
| Artifact | 制品 | 私有包进入可安装仓库的分发单元 |
| npm mirror | npm 镜像 | Code Repositories 使用的外部公共包源 |
| `E401` | npm 认证错误码 | 也可能由公共 npm 服务网络不可达触发 |

## 疑问与待验证项

- 文档列举默认仓库，但未说明具体仓库在所有环境中的开放范围及其同步延迟。
- `E401` 的网络原因要结合 workspace 网络日志区分，不能仅凭错误码判定。
- 删除锁文件可能改变依赖解析结果；生产项目仍应检查锁文件变更并通过代码评审。

## 复刻启示

- 依赖管理界面应展示每个包实际解析到的 registry、版本与来源，并区分认证失败和网络不可达。
- 私有包发布与应用使用需建立制品可见性检查；不能把依赖解析问题笼统反馈为“安装失败”。
- 排障建议按低风险到高影响排列，并保留 lockfile 变化供审查。