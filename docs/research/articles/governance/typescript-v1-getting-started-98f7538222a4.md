<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/typescript-v1-getting-started -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v1 • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/typescript-v1-getting-started)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:00Z
- 产品状态：TSv1 入门页明确建议需要 OSDK/资源请求能力的项目迁移至 TSv2。

## 英文原文短摘录（每个来源不超过 25 词）

> “For more robust capabilities, including support for Ontology SDK and configurable resource requests, we recommend migrating to TypeScript v2.”

## 摘录译文

若需要更完善能力（包括 OSDK 支持和可配置资源请求），文档建议迁移到 TypeScript v2。

## 中文要点

- TSv1 函数是 `@Function()` 装饰器标记的类方法，类须从 `functions-typescript/src/index.ts` 导出；需声明所有输入和返回类型。
- Functions helper 的 Live Preview 用于运行验证，提交代码后再 Tag version；tag 会发布仓库中所有函数。
- 发布检查通过后函数可能仍要等待权限传播，才会出现在 Workshop 或函数注册表搜索中。
- 该教程明确建议需要 OSDK 和可配置资源请求的项目迁移 TSv2；两代模板的函数发现、SDK 和运行能力不同。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| TypeScript v1 | TypeScript v1 | 以装饰器和类方法声明函数的模板/运行时。 |
| @Function() | 函数装饰器 | TSv1 中将类方法登记为函数的装饰器。 |
| index.ts | 入口文件 | 仓库导出函数类的模块。 |

## 疑问与待验证项

- 教程示例的目录和 `master` 分支依赖生成模板；应对照目标仓库结构。
- 当前新项目仍否适合 TSv1，需要参考最新 feature support 矩阵和组织的部署依赖。

## 复刻启示

- 将函数语言、运行时版本和 SDK schema 版本写入本体函数节点的可追溯元数据。
- 将代码检查、全仓发布和资源权限传播分步展示，提示一次 tag 的真实发布范围。
