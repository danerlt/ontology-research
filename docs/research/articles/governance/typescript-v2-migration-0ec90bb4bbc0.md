<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/typescript-v2-migration -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v2 • Migrate from TypeScript v1 to TypeScript v2 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/typescript-v2-migration)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:52Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “This guide describes the syntax and structure differences you may encounter while migrating existing TypeScript functions from v1 to v2.”

## 摘录译文

本指南介绍从 v1 迁移至 v2 时可能遇到的语法和结构差异。

## 中文要点

- TSv1 函数通常是带 `@Function()` 装饰器的类方法，并从仓库根 `index.ts` 导出；TSv2 每个函数位于 `src/functions` 下的文件中，以 `export default` 声明。
- 基础类型包从 `@foundry/functions-api` 迁到 `@osdk/functions`；Ontology 资源访问采用 OSDK，链接访问方式和对象集 API 与 TSv1 有明显差别。
- TSv2 用对象 `$link` 容器和 `pivotTo()` 遍历链接；单链接 `fetchOne()` 在无匹配对象时会抛错，而 TSv1 `.get()` 可返回 undefined。多链接已是对象集，可链式迭代。
- 聚合的 group-by 表达方式以及精确分桶默认上限也有变化；TSv2 某些响应的 approximate 状态 SDK 不一定暴露，迁移需检查结果准确性与语义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| TypeScript v1 / v2 | TypeScript v1 / v2 | 两代函数模板和运行时/API。 |
| pivotTo() | 链接透视 | 沿对象集中的指定 link API name 遍历关联对象。 |
| fetchOne() | 读取单个链接对象 | TSv2 的单链接读取方法，无匹配与异常行为需显式处理。 |
| groupBy strategy | 分组策略 | 对象集聚合时决定分桶/范围的配置。 |

## 疑问与待验证项

- 迁移不只是语法替换；函数标识、资源导入、空结果错误和聚合近似性均可能改变。
- 页面指出 TSv2 SDK 不暴露部分聚合 approximate 字段；如果业务要求精确值，需设置桶上限或先过滤集合并验证。

## 复刻启示

- 在本体管理系统的规则执行引擎中把函数语言运行时/API 版本写入定义，不隐式升级执行语义。
- 提供迁移预览：列出函数导出、类型包、链接基数、空值处理、分页/聚合精度变化，并要求回归案例确认。
