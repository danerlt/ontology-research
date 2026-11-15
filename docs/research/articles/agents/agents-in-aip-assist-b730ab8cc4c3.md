<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/assist/agents-in-aip-assist -->
<!-- 研读状态：已完成 -->

# 辅助 • Power AIP Assist with custom content sources • 部署自定义源支持的AIP Assist代理 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/assist/agents-in-aip-assist)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/assist/agents-in-aip-assist)（页面声明机器翻译未经验证）
- 页面语言：中文
- 主题栏目：assist
- 相关性：direct；AIP Assist Agent 文档
- 官方更新时间：2026-11-12T17:46:46.936Z
- 目录核对时间：2026-11-14T14:58:34Z
- 产品状态：官方中文页面声明机器翻译准确性未经验证；以英文现行文档核对术语和规则。

## 原文短摘录与翻译

> “确保将您的内容组织成标题和子部分。”

## 摘录译文

英文对应原文：“Make sure to organize your content into headings and subsections.”

## 中文要点

- 该页面是 `agents-in-aip-assist` 的官方中文版本；其开头明确说明译文由 AIP 从英文生成且尚未验证。
- 内容讲述将 Notepad/Markdown 内容注册给 AIP Assist，再创建、配置并发布 AIP Chatbot；内容层级有助于检索分段。
- 中文页称自定义内容源是 Agent 的“唯一搜索上下文”；英文页另提本体上下文和工具，可能是“检索来源”与“全部运行上下文”定义不同，应以英文页面和相关产品文档复核。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 自定义内容源 | custom content source | 注册给 AIP Assist 的检索文档。 |
| AIP Assist 代理 | AIP Assist Agent | 使用 AIP Assist 内容源的助手。 |
| 检索上下文 | retrieval context | Agent 用于查找材料的内容范围；与工具/本体上下文需区分。 |
| 机器翻译 | machine translation | 页面明确标注为未验证的自动译文。 |

## 疑问与待验证项

- 中文页把自定义内容源描述为“唯一搜索上下文”，和英文页关于本体上下文或 Functions 工具的表述存在范围差异；两者或许区分 RAG 来源与其他上下文。
- 该页面自身提示机器翻译准确性未验证，尤其产品名、retrieval context 和授权描述需要人工对照英文。

## 复刻启示

- 对官方中文术语页标记机器翻译来源和核验状态；遇到“唯一”等范围词时链接英文原句并记录差异。
- 系统内明确区分文档检索、Ontology 对象上下文和工具调用三种 Agent 上下文来源，并分别实施权限检查。
