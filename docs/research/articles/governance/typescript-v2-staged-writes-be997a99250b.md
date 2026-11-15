<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/typescript-v2-staged-writes -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v2 • Staged writes • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/typescript-v2-staged-writes)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:53Z
- 产品状态：Beta；可能未在所有 enrollment 启用，且预览只支持 Code Repositories。

## 英文原文短摘录（每个来源不超过 25 词）

> “Staged writes provide a read-after-write guarantee for Ontology edits applied in the function.”

## 摘录译文

Staged writes 为函数内应用的本体编辑提供写后可读保证。

## 中文要点

- 同次 Action 执行中的编辑先暂存；本函数和嵌套 staged-write 函数的查询/聚合能看到此前写入，其他执行上下文在提交前不可见。
- 函数成功结束后整批提交；任一调用失败则整批丢弃，并由 Action 流程重试。函数可返回业务数据，不必返回编辑数组。
- 签名用 `WriteableClient<Edits...>` 声明可修改实体。页面说明接口编辑不受支持，链接写入聚焦多对多 link/unlink。
- 能力处于 Beta；live preview 和已发布函数预览只支持 Code Repositories，不支持本地开发或 VS Code workspace。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| staged writes | 分阶段写入 | 执行期暂存编辑，成功后整体提交。 |
| WriteableClient | 可写客户端 | 用于创建、更新、删除和链接对象的运行时客户端。 |
| atomic execution | 原子执行 | 全部编辑一起提交或整体丢弃。 |

## 疑问与待验证项

- 外部副作用是否会随 Action 重试重复执行，需分别实现幂等键或补偿。
- Beta 支持范围和版本应按目标 enrollment 确认。

## 复刻启示

- 推理工作流若需要读回刚创建/修改的对象，可使用执行局部事务并对外展示提交与回滚轨迹。
- 事务不覆盖 webhook 等外部系统；将外部副作用与本体事务分阶段并记录幂等键。
