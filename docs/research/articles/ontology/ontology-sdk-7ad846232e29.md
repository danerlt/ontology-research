<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/questions-answers/ontology-sdk -->
<!-- 研读状态：已完成 -->

# 问答 • Ontology SDK • Palantir

- 英文来源：[现行英文问答](https://www.palantir.com/docs/foundry/questions-answers/ontology-sdk)
- 官方中文来源：[官方中文页（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/questions-answers/ontology-sdk)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：questions-answers
- 相关性：direct；SDK 授权、运行时兼容及类型映射
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T15:01:25Z
- 产品状态：问答包含 2024 与 2026 更新；部分中文答案与现行英文页存在差异

## 英文原文短摘录（不超过 25 词）

> “The Python OSDK requires a Python version >=3.10 and <3.15.”

## 摘录译文

Python OSDK 要求 Python 版本不低于 3.10 且低于 3.15。

## 中文要点

- 当前英文答复称 Developer Console 应用默认受限，应用 token 只访问已配置的项目和操作；组管理需要将应用配置为 unrestricted。组织在 Control Panel 的 “Unrestricted Project access” 只影响代表用户走授权码流程的应用，不能替代应用级权限限制。
- 对 stream-data-proxy 等底层服务端点，restricted 应用可能没有相应 operation scope；当前答复建议使用 unrestricted 应用并对所需命名空间申请 `api:*`。
- 2026-07-02 更新的 Python 支持范围为 `>=3.10, <3.15`；中文页面仍保留 2024-03-08 的 `3.9–3.11` 旧答复，不能据中文译文配置运行时。
- 当前英文答复说 TypeScript `contains` 搜索仅支持完整词和前缀，不支持任意子串匹配；目前没有官方 C# SDK，可导出 OpenAPI 生成客户端。
- `/loadObjects` 的共享/接口属性名依读取的是具体对象还是 Interface 视图而异；Python 自定义请求头的 FAQ 示例直接访问 client 内部 session 对象，属于需谨慎对待的实现细节。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| restricted application | 受限应用 | token 受应用资源/操作限制约束 |
| unrestricted application | 不受限应用 | 允许申请更宽 API operation scope 的应用模式 |
| authorization code grant | 授权码授权流程 | 代表登录用户访问资源的 OAuth 模式 |
| interface property mapping | 接口属性映射 | 将具体对象属性映射到共享/接口视图字段 |

## 疑问与待验证项

- 中英文 Python 版本范围冲突明显；本卡采用当前英文页标注的 2026 答复，仍应以 SDK 发布与安装失败信息核对目标环境。
- `api:*` 不是绕过用户/服务用户授权的通行证；实际访问还需应用配置和身份本身权限共同允许。
- FAQ 未给出 contains 搜索的全部标点、大小写和分析器规则；以具体 Search API 规范为准。

## 复刻启示

- 运行时支持矩阵需标注来源更新时间，中文旧 FAQ 不应覆盖更新后的英文约束。
- 权限 UI 分离应用最大范围、OAuth scope 和调用身份权限，并用交集方式解释最终授权。
- 共享属性和接口投影依上下文解析字段名；SDK 生成和响应需保留对象类型/接口视图上下文。