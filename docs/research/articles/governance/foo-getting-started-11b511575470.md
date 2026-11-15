<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/foo-getting-started -->
<!-- 研读状态：已完成 -->

# Functions • 对象函数入门 • Getting started with functions on objects • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/foo-getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/foo-getting-started)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:11Z
- 产品状态：对象函数通过项目资源导入生成本体类型绑定；TypeScript v1 与 v2 使用不同包和实例类型。

## 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology provides semantic modeling of data for your organization.”

## 摘录译文

Ontology 为组织数据提供语义建模。

## 中文要点

- TypeScript 函数仓库先导入要使用的对象、接口和链接类型；如未指定 Ontology，资源导入器可根据已导入类型推定。
- 导入后 Code Assist 重启并生成类型绑定；TSv1 从 @foundry/ontology-api（私有本体加 API 名子包）导入，TSv2 需先生成安装本地 OSDK，再从 @ontology/sdk 使用。
- 示例以 Airport 与 Flight 对象及二者链接为输入，帮助开发者通过自动补全访问 schema 属性。
- Live Preview 运行对象函数前需导入底层数据源；预览 runtime 与已发布函数在 CPU、内存和超时上不同。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Resource import | 资源导入 | 把本体对象/链接/接口纳入函数项目依赖 |
| Generated binding | 生成类型绑定 | 根据本体 schema 生成的代码 API |
| Backing datasource | 底层数据源 | 支撑对象类型数据读取的资源 |

## 疑问与待验证项

- 私有 Ontology 的 package 名称包含 API 名；重命名会影响依赖路径，应通过 schema/SDK 版本化迁移。
- Live Preview 的资源和执行配额不同于已发布函数，不应只在预览通过就认定生产行为一致。

## 复刻启示

- 函数依赖应显式导入对象类型和关系；schema 更新后重新生成绑定并在分支审查 API 变化。
- 本地预览有权限的数据源依赖也需要声明，输出卡片标识模拟环境与发布运行环境差异。
