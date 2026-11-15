<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/python-functions-advanced-usage -->
<!-- 研读状态：已完成 -->

# 函数 • Python functions • 高级用法 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/query-functions)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/python-functions-advanced-usage)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:31Z
- 产品状态：中文旧路由“Python 函数高级用法”已重定向至现行 Query 文档；Query 可经 API Gateway 暴露，但不能修改 Ontology 或外部系统。

## 原文短摘录与翻译

> “Queries are the read-only subsets of functions that may be optionally exposed through the API gateway.”

## 摘录译文

Query 是函数的只读子集，可选择通过 API Gateway 暴露。

## 中文要点

- Query 是无副作用的只读函数；如需经 API Gateway 执行 Ontology 写入或改变外部系统，应定义 Action/写操作路径，而不是 Query。
- TSv1、TSv2 和 Python 均提供 Query 定义方式；API 名称用于对外标识，Python/TSv1 的 decorator 接受 API name 参数，TSv2 使用导出的配置对象。
- 示例通过对象搜索做过滤与 count，再向 API 客户端返回结果，说明 Query 可以封装业务检索而不暴露底层查询拼装。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query | 查询函数 | 只读且可通过 API Gateway 发布的函数子集 |
| API gateway | API 网关 | 向应用或外部调用方暴露已发布 Query 的平台入口 |
| apiName | API 名称 | 查询函数面向 API 的稳定调用标识 |
| side effect | 副作用 | 修改本体或外部系统状态的操作 |

## 疑问与待验证项

- 旧中文路由映射到通用 Query 文档而非专属 Python 高级教程；迁移过程中是否丢失额外示例需检查当前官方页版本。
- API Gateway 的认证、scope、限流、分页与响应 schema 约束不由 Query 概念页完整说明，需结合网关页面确认。
- 即使 Query 只读，仍需按调用者权限过滤对象，并防止函数返回字段形成敏感数据旁路。

## 复刻启示

- 将查询函数与 Action 命令分离：Query 契约只读、可缓存并有输入/输出 schema；写入必须提交可审计 Action。
- API 网关仅公开管理员注册、版本固定且经权限评估的 Query；对外稳定 API 名与内部实现版本分离。
- Agent 只读工具调用映射到 Query，写操作映射到带用户确认和授权策略的 Action，并记录函数版本、参数摘要和对象来源。
