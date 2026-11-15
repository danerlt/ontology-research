<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/upload-media -->
<!-- 研读状态：已完成 -->

# 动作类型 • 上传媒体 • Upload media • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/upload-media)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:11Z
- 产品状态：大规模媒体应使用 Media Reference/Media Set；写入授权依赖 Action，而非终端用户直接持有 Media Set 权限。

## 英文原文短摘录（每个来源不超过 25 词）

> “For most use cases in Foundry, uploading to media reference properties is the recommended method.”

## 摘录译文

对于 Foundry 中的大多数场景，推荐上传到媒体引用属性。

## 中文要点

- 媒体引用属性由 Media Set 支撑，适合规模化文件存储检索，并提供转换、丰富预览及专用地理/医学影像格式工作流。
- Action 表单或表格接收文件，只有 Action 成功提交后文件才持久化到 Media Set；格式转换在 Action 完成且媒体上传后发生。
- 上传授权由 Action 提交条件控制；通过 Action 有权的用户不需要直接拥有底层 Media Set 权限。首次把 Media Set 接入对象类型或 Action 时会检查其编辑权限，随后访问控制委托给 Ontology。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Media reference property | 媒体引用属性 | 对象上指向媒体集合资源的属性 |
| Media Set | 媒体集合 | 存储与检索媒体文件的资源 |
| Action submission criteria | Action 提交条件 | 控制是否允许通过动作上传媒体的授权/业务校验 |

## 疑问与待验证项

- “成功提交后持久化”与 Action 外部副作用失败的关系需结合各提交阶段确认。
- 媒体集合委托给 Ontology 后，谁能编辑 Action 等价于谁可发起上传；应审计管理动作的权限范围。

## 复刻启示

- 优先实现媒体引用属性和媒体集合，而非把大文件当普通属性；上传经过暂存、Action 条件检查、绑定和异步转换。
- 在连接 Media Set 时展示权限委托影响，并由服务端按 Action 授权校验最终绑定。
