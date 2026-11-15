<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/query-functions -->
<!-- 研读状态：已完成 -->

# 函数 • Functions called through the API gateway • 查询 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/query-functions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/query-functions)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:39Z
- 产品状态：Query 可发布为外部可调用的只读 API，适合封装受控的本体查询；具有写入副作用的操作应通过 Action 提供。

## 英文原文短摘录（每个来源不超过 25 词）

> “may be optionally exposed through the API gateway”

## 摘录译文

可以选择通过 API 网关公开

## 中文要点

- Query 的返回逻辑不能修改 Ontology 或外部系统；需要这些副作用时应通过 API Gateway 暴露相应 Action。
- TSv1 和 Python 在函数定义装饰器上声明 API 名；TSv2 通过导出配置对象设置 `apiName`。
- Query 可在函数内部组合对象搜索/过滤/聚合，仅向 API 消费方暴露稳定的参数和返回值契约。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query | 查询函数 | 可选经 API Gateway 暴露的只读函数类型 |
| API name | API 名称 | 外部调用时使用的函数标识 |
| API gateway | API 网关 | 负责对外公开已注册查询端点的平台入口 |
| side effect | 副作用 | 修改 Ontology 或外部系统状态的行为 |

## 疑问与待验证项

- 页面聚焦 Query 定义和发布；认证、OAuth scope、限流、schema 版本及分页等网关细节需查独立 API Gateway 文档。
- 不同语言的声明方式不同；TSv2 配置、Python `api_name` 和 TSv1 `apiName` 需在 SDK 生成/编译期校验。
- Query 只读并不意味着输出一定不敏感；函数返回字段仍需经过调用者授权和数据分类评估。

## 复刻启示

- API 侧把只读查询与有副作用的 Action 分成不同资源类型，查询可缓存并提供稳定输入/输出 schema。
- Agent 工具注册默认只暴露 Query；如果开放写入 Action，需追加用户确认、细粒度权限、幂等键和完整审计。
- 画布为 API query 节点显示它读取的对象类型、链接路径、过滤器和聚合结果，便于审查工具实际可读范围。
