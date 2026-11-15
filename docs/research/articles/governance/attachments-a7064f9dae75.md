<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/attachments -->
<!-- 研读状态：已完成 -->

# Functions • Functions on objects • Attachments • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/attachments)
- 官方中文来源：尚未确认（目录配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；Functions 对本体附件的读取、上传与持久关联
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:17Z
- 产品状态：TS v2 Functions 当前不支持创建附件；未关联对象的附件会过期清理

## 英文原文短摘录（不超过 25 词）

> “Attachments are uploaded as temporary files and attached to objects using actions.”

## 摘录译文

附件先以临时文件上传，再通过 Action 关联到对象。

## 中文要点

- Attachment 是一种表现为对象属性的文件；先上传为临时文件，经 Action 附加到对象后才持久化，并可像其它属性一样访问。
- TypeScript/Python Functions 可把 Attachment 作为输入读取，也能从对象属性读取；读出的数据按语言变成 Blob、Response 或 BytesIO，复杂文件格式仍需额外解析库。
- 可把附件作为 Excel 输入，解析多行后由 Ontology Edit 批量新建/修改对象；多文件参数使用 TypeScript `Attachment[]` 或 Python `list[Attachment]`。
- 函数可以创建并返回附件，但要通过 Ontology edit 把它链接到对象才能持久化；未附加对象的文件仅上传者可见，并在一段时间后自动删除。
- TypeScript v2 Functions 不支持创建附件；TSv1 还需要注意运行环境不提供 filesystem，使用依赖 `fs` 的解析库可能编译或执行失败。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment | 附件 | 可作为本体属性存储引用的文件资源 |
| temporary file | 临时文件 | 上传后尚未与对象持久关联的附件内容 |
| `OntologyEdit` | 本体编辑 | 函数返回的对象属性/关联变更计划 |
| `readAsync()` / `fetchContents()` | 读取附件数据 | TS SDK v1/v2 读取原始文件内容的方法 |

## 疑问与待验证项

- 文档用 “a certain period” 表述孤儿附件清理，没有在此页给出精确时间；应查附件生命周期 API/上传说明。
- TypeScript v2 Functions 不支持创建附件，但附件仍可作为输入/对象属性读取；需区分 OSDK 客户端和 Functions 运行时的能力差异。
- 文件格式解析取决于运行环境依赖；附件读权限、文件大小和病毒扫描策略另见安全/上传文档。

## 复刻启示

- 附件生命周期建模为上传暂存→权限检查→Action/OntologyEdit 关联→持久化；孤儿临时文件需自动清理。
- 函数输入支持附件元数据与字节流，但下载内容遵循对象属性权限；审计记录附件 RID、对象和关联 Action。
- 按语言/运行时显示附件能力矩阵，不能把 TypeScript v1、v2、Python 的读写能力合并成一种假设。