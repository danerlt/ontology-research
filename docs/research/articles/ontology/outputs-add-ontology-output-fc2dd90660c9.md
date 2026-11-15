<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/pipeline-builder/outputs-add-ontology-output -->
<!-- 研读状态：已完成 -->

# 管道构建器 • Pipeline outputs • 添加Ontology输出 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/pipeline-builder/outputs-add-ontology-output)
- 官方中文来源：[官方中文页面（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/pipeline-builder/outputs-add-ontology-output)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：pipeline-builder
- 相关性：direct；将流水线输出绑定为对象类型和链接类型
- 官方更新时间：2026-11-12T17:46:46.926Z
- 目录核对时间：2026-11-14T15:01:10Z
- 产品状态：支持 batch/stream 数据集输出；流数据对象编辑和多对多链接当前有限制

## 英文原文短摘录（不超过 25 词）

> “Pipeline Builder currently supports creating Ontology objects and links from both batch and streaming datasets.”

## 摘录译文

Pipeline Builder 当前支持从批处理和流式数据集创建本体对象与链接。

## 中文要点

- Ontology output 将 transform 输出指向结构化对象/关系，提供本体建模指导并帮助节省计算检查时间。
- 对象类型输出可以新建空白模板，也可由图中的 transform 节点连接已产生数据的输出；名称、图标和属性在输出面板配置。
- Pipeline Builder 可管理自己创建的对象类型；未由该流水线创建的现有对象类型不能直接在此修改或删除。首次部署后 Object type ID 不可改，但归流水线管理的 API name 可编辑。
- 流式数据集支撑的对象类型不能启用编辑，也不能配置多对多链接；链接类型可作为独立输出并连接相关对象类型。
- Ontology 校验错误可在流水线中处理，包括 schema 与主分支版本不一致造成的迁移；历史“放弃 Ontology 输出”功能已标为弃用，转换回数据集输出会把类型后续管理移交 Ontology Manager。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology output | 本体输出 | Pipeline 输出节点对接本体对象/链接 schema |
| transform node | 转换节点 | 产生流水线数据并连接对象类型输出的节点 |
| Object type ID | 对象类型 ID | 首次部署后不可修改的对象类型标识 |
| disown Ontology output | 放弃本体输出管理 | 将后续对象类型 schema 管理权移交 Ontology Manager 的旧流程 |

## 疑问与待验证项

- 流式对象禁用编辑和多对多链接的原因及解除条件未在本页展开；产品建模须遵守当前功能限制。
- Object type ID 与 API name 是不同标识；更新时应确认对象引用、SDK 生成包和目标环境依赖哪个字段。
- “弃用”流程的最终移除时间未给出，当前建议按 Pipeline Builder 与 Ontology Manager 的最新 schema 工作流操作。

## 复刻启示

- 画布应明确表示 transform→对象类型输出→对象数据源的依赖边，同时将对象类型 schema 作为一等资源节点展示。
- 对象资源要记录 owner（Pipeline Builder 或 Ontology Manager）、稳定 RID/ID 和可改 API name，禁止未授权修改他方资源。
- 输出验证应检查 schema 版本、数据源范围和链接基数；流式数据相关的不可用操作应在配置阶段禁用并解释。