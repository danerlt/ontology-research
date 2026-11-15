<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-testing -->
<!-- 研读状态：已完成 -->

# Ontology SDK • TypeScript • Unit testing TypeScript OSDK code • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-testing)
- 官方中文来源：尚未确认（目录配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；在不访问 Foundry 时对 OSDK client 代码做单元测试
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:41Z
- 产品状态：`@osdk/unit-testing` 为 Experimental；仅从 `/experimental` 子路径导出

## 英文原文短摘录（不超过 25 词）

> “The `@osdk/unit-testing` package is experimental.”

## 摘录译文

`@osdk/unit-testing` 包目前处于 Experimental 阶段。

## 中文要点

- 此包测试接收 OSDK Client 的代码和 Foundry Functions，不向 Foundry 发出真实请求；若要在本地 Ontology server 上带种子数据验证真实请求，应使用 integration testing。
- `createMockClient` 可对 fetch、object set 和 query 调用配置 fluent stub；`createMockOsdkObject` 生成包含 primary key、title、RID、links 等属性的完整实例。
- `createMockObjectSet` 可作为对象集或多链接聚合目标；`createMockAttachment` 产生函数输入所需的附件占位对象。
- 所有导出从 `@osdk/unit-testing/experimental` 引入；文档要求与项目的 `@osdk/api`、`@osdk/client` 和 `@osdk/functions` peer dependency 兼容。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| mock client | 模拟客户端 | 通过预设 stub 响应隔离网络和平台依赖 |
| fluent matcher | 链式匹配器 | 按 OSDK 查询/对象集/Function 调用配置返回值 |
| peer dependency | 同伴依赖 | 单元测试包必须与应用 OSDK 运行时版本兼容 |
| experimental subpath | 实验性导出子路径 | API 尚未稳定的显式导入入口 |

## 疑问与待验证项

- Experimental 包 API 可能变化，不应把其 mock 输出形状当作稳定的生产数据契约。
- 模拟客户端适合验证业务分支，但不会验证 Foundry 授权、服务端查询限制或关系数据正确性。
- 文档以 Vitest 展示样例，但声明可使用其他测试 runner；具体是否兼容需依赖生命周期钩子行为。

## 复刻启示

- OSDK client 使用接口注入便于业务逻辑单元测试，mock 需覆盖对象、集合、Action、Function 和附件形状。
- 测试工具应标注适用边界：stub 测试与本地 server 集成测试不可相互替代。
- 实验性 SDK 支持模块与生产客户端隔离，版本升级时通过适配层降低调用方耦合。