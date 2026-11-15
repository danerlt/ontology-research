<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments/attachment-basics -->
<!-- 研读状态：已完成 -->

# Attachment basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments/attachment-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 附件生命周期基础概念
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:56:27Z
- 产品状态：基础概念页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Attachments are uploaded as temporary files and attached to objects via actions.”

## 摘录译文

附件先作为临时文件上传，再通过动作关联到对象。

## 中文要点

- 本体附件是“像对象参数一样工作的文件”；其生命周期有两个关键动作：先上传为临时文件，再通过 Action 把附件关联到对象。
- 附件配置在 Ontology Manager 中。页面链接到用户文档的附件上传流程，表示概念页本身没有展开具体上传接口、暂存清理时限或动作参数格式。
- 这与 Attachment Property 的定义互补：属性表达对象与文件的引用，附件资源则承载文件本体；不能把上传成功等同于已经写入某对象。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment | 附件 | 可被对象引用的文件资源 |
| Temporary file | 临时文件 | 上传后尚待关联对象的阶段性文件 |
| Action | 动作 | 将附件挂接到本体对象的业务写操作 |
| Ontology Manager | 本体管理器 | 配置对象附件属性的管理界面 |

## 疑问与待验证项

- 临时文件的保留期限、失败重试、孤儿回收以及跨用户/项目隔离规则不在此页说明。
- 上传、关联、替换和移除的授权分别需要何种权限，应结合 Upload Attachment 与 Apply Action 的端点文档核实。
- 一次 Action 是否能同时写普通属性与关联多个附件、以及关联失败后的暂存清理方式未明确。

## 复刻启示

- 设计两阶段状态机：文件上传进入 `temporary`，经授权 Action 绑定后进入 `attached`；失败、取消或过期进入可清理状态。状态与超期策略属于复刻系统需明确定义的规则。
- 将对象属性绑定、附件元数据和二进制对象分层存储；Action 负责业务关系写入，上传服务负责内容校验与暂存。
- 审计记录要串联上传者、暂存 RID、最终对象/属性、关联 Action 和内容校验结果，使问题追溯覆盖文件与本体对象两个边界。
