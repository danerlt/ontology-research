<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/api-ontology-edits -->
<!-- 研读状态：已完成 -->

# Functions • 本体编辑（TypeScript v1） • Ontology edits • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/api-ontology-edits)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/api-ontology-edits)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:04Z
- 产品状态：TSv1 编辑函数仅在由 Action 承载时才会产生实际数据修改，且声明其编辑对象范围。

## 英文原文短摘录（每个来源不超过 25 词）

> “running an edit function outside of an Action will not actually modify any object data.”

## 摘录译文

脱离 Action 运行编辑函数并不会真正修改对象数据。

## 中文要点

- 本体编辑函数可修改对象属性和链接、创建或删除对象；页面是 TypeScript v1 参考，并推荐迁移到 TSv2 使用 OSDK 和可配置资源请求。
- 要用于实际写入，函数必须被配置为 function-backed Action；运行在 Action 之外不会直接改动本体。
- 函数须使用 @OntologyEditFunction() 与 @Edits([object type]) 声明，并显式返回 void；本体编辑由运行环境捕获为编辑列表。
- 赋值后在同一函数执行内再次读取该属性会看到新值；数组属性应复制后整体赋值。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology edit function | 本体编辑函数 | 以函数逻辑产生对象/链接修改的函数 |
| @Edits | 编辑范围声明 | 声明函数可编辑的对象类型范围 |
| Function-backed Action | 函数支持的动作 | 提供实际授权与操作入口的动作定义 |

## 疑问与待验证项

- 运行函数但未通过 Action 调用没有实际写入副作用，如何区分 Query/Preview 与真实 Action 执行需在应用入口清楚表达。
- 属性编辑后的同次执行读取行为不代表其他请求可见性；跨请求读写时序还要看一致性和材料化文档。

## 复刻启示

- 写入函数必须通过 Action 边界统一做权限、提交条件、审计和本体编辑落库，避免函数直接绕过操作治理。
- 函数发布时静态检查声明的可写对象类型，试算返回明确的对象/链接编辑集合。
