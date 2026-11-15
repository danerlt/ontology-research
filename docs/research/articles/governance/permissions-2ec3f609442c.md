<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/permissions -->
<!-- 研读状态：已完成 -->

# Functions • Function management • Permissions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/permissions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/permissions)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:33Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “Repository permissions must be explicitly granted, and are not the same as the permissions granted to your user account.”

## 摘录译文

仓库权限必须显式授予，并且不同于授予给用户账户的权限。

## 中文要点

- 函数开发权限覆盖代码绑定、资源导入、实时预览和发布运行等不同环节；仓库所需权限不会因为操作者个人有权而自动成立。
- Ontology、分支、对象类型、链接类型及支持数据源通过项目级导入配置提供给仓库；项目内的导入变化可能影响同项目其他仓库，当前单个项目不支持导入多个 Ontology。
- 函数读取对象时遵循实际执行用户的数据权限；不同用户调用同一函数可能得到不同对象集。Restricted View、对象/属性安全策略属于读取时过滤，不自动约束函数输出，应结合 marking 或 CBAC 防止下游泄露。
- 发布函数通常要求用户可查看发布仓库；函数还需注册在 Developer Console。Function-backed Action 可由 Action 权限决定终端用户能否调用，但配置 Action 的管理者须具备相应函数权限。扩展执行另受管理员 allowlist 控制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| repository permissions | 仓库权限 | 给代码仓库绑定/加载资源及执行函数的授权。 |
| live preview | 实时预览 | 代码作者在仓库环境中试运行函数。 |
| read-time enforcement | 读取时强制执行 | 对象/行/列策略在函数读取数据时生效。 |
| extended execution | 扩展执行 | 允许函数使用更高权限能力的受控运行模式。 |

## 疑问与待验证项

- 同项目导入配置会跨仓库生效，项目边界因此既是授权范围也是依赖隔离边界；多 Ontology 工作区需用多个项目拆分。
- 函数读取时过滤不等同于输出数据标记传播；需要核查函数返回内容、日志、导出和 Agent 工具结果的保护策略。

## 复刻启示

- 将作者权限、服务执行权限、对象读取策略、应用调用权限和扩展执行 allowlist 分开建模，并在部署前给出逐项授权检查结果。
- 函数/Agent 若把受限数据返回给下游，需做数据标签传播或显式脱敏；仅在查询入口校验一次不足以保护派生结果。
