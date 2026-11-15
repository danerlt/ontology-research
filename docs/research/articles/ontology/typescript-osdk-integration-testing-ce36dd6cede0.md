<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-integration-testing -->
<!-- 研读状态：已完成 -->

# Ontology SDK • TypeScript • Integration testing TypeScript OSDK code • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-integration-testing)
- 官方中文来源：尚未确认（目录配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；在本地本体服务上验证 TypeScript OSDK 行为
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:41Z
- 产品状态：`@osdk/integration-testing` 标记为 experimental，API 与功能可能变化

## 英文原文短摘录（不超过 25 词）

> “The `@osdk/integration-testing` package allows you to test TypeScript Ontology SDK (OSDK) code against a local Ontology server.”

## 摘录译文

`@osdk/integration-testing` 包可以让你在本地 Ontology server 上测试 TypeScript OSDK 代码。

## 中文要点

- 集成测试使用本地 Ontology server、Ontology 元数据和测试数据，让真正的 OSDK Client 请求本地服务执行对象查询。
- 主要组件：`IntegrationServer` 管理本地服务进程，`SeedClient` 创建/修改测试数据，`IntegrationClient` 发送 OSDK 请求并支持对 Function 查询设 stub。
- 适合验证过滤、对象读取、链接和聚合在一起时的实际行为；若要逐个 client 调用指定返回值，使用 unit test 与 stub 更合适。
- 该包运行于 Node 环境，会启动本地进程，不适用于浏览器测试；需要兼容版本的 `@osdk/api`、`@osdk/client` 和生成 TypeScript SDK。
- 文档以 Vitest 展示 setup/teardown、种子数据和测试隔离，也允许使用具有等价生命周期钩子的其他 Node 测试运行器。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| IntegrationServer | 集成测试服务 | 启动与关闭本地 Ontology 服务 |
| SeedClient | 测试数据种子客户端 | 在本地服务创建/更改测试对象 |
| IntegrationClient | 集成测试客户端 | 使用 OSDK 对本地服务发起真实请求 |
| stub function query | 桩化函数查询 | 隔离 Function 响应以控制测试输入 |

## 疑问与待验证项

- 文档明确标为 experimental；依赖更新时需核对 API、种子数据和元数据格式变动。
- 测试服务能否覆盖 Action 写入的全部权限/冲突语义，本文未作完整承诺。
- 与普通 mocks 相比，启动本地进程会增加测试时间；应按模块区分快速单元测试与较慢集成验证。

## 复刻启示

- 本体 DSL/API 可配套本地执行器和可重复种子数据，验证过滤、关系遍历与聚合的真实组合语义。
- 测试工具提供 server/client/seed 分层，允许测试显式设置版本化 schema 与资源权限。
- Beta/实验包需隔离为可替换适配层，不能作为生产 API 稳定性承诺。