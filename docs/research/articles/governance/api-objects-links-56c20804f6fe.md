<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/api-objects-links -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • API: Object和链接 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/api-objects-links)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/api-objects-links)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:51Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “This page covers TSv1.”

## 摘录译文

本页介绍 TSv1。

## 中文要点

- 本页描述 TSv1 API：本体 API Name 转为生成接口字段；未赋值属性可能返回 `undefined`，数组属性和多链接结果为只读数组。
- `SingleLink` 用于单侧关系，可通过 `get()`/`getAsync()` 获取目标；`MultiLink` 用 `all()`/`allAsync()` 读多目标。无目标时单链接可能是 undefined，多链接返回空数组。
- 链接遍历会触发后端对象加载，可能较昂贵；可使用 ObjectSet/Search Around 组合查询以避免将所有关联对象载入内存。
- TSv2/Python 的访问方式是 OSDK，本页旧 TSv1 路由不应当作为新代码的当前 SDK 指引；中文页面为未经验证的 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| API name | API 名称 | 由本体资源映射到 SDK 字段/方法的稳定技术名。 |
| SingleLink | 单链接 | 指向至多一个对象的链接访问器。 |
| MultiLink | 多链接 | 面向多个目标对象的链接访问器。 |

## 疑问与待验证项

- 关系缺失时各端返回 undefined、null 或空数组的差异应在 SDK 版本化参考中统一。
- 大规模多链接是否可分页、是否使用快照及 ObjectSet 遍历的限制需查 TSv1 ObjectSet API。

## 复刻启示

- 代码生成器必须保留对象/API 名、属性类型、空值和链接基数语义；生成类型帮助暴露关系建模错误。
- 提供分页对象集查询与链接遍历成本提示，避免 UI/API 将高基数链接一次性展开。
