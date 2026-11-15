<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/input-output-types -->
<!-- 研读状态：已完成 -->

# 函数 • TypeScript basics • 输入和输出类型 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/types-reference)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:18Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：a TypeScript function must have explicit type annotations on all input parameters and specify an explicit return type.

> 中文译文：TypeScript 函数的所有输入参数必须有显式类型注释，并且必须声明显式返回类型。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 旧路由已归并到 Types reference；TypeScript 函数发布前需明确每个参数类型和返回类型，注册表只接受列出的 Foundry 类型。
- TSv1/TSv2/Python 的映射不是一一相同：例如接口对象仅 TSv2支持、媒体引用在 TSv1 为 MediaItem、TSv2/Python 为 Media；User/Group ID 等也存在版本差异。
- Python 的 `int`/`float` 会映射到默认注册类型，文档建议显式使用 Integer/Long、Float/Double 等别名避免 schema 意外变化。
- 集合、结构体、通知、附件、空间/时间聚合等复杂类型需要按接口参考确认；中文页机翻准确性未验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function registry type | 函数注册表类型 | 调用者可见的输入/输出 schema 类型。 |
| Type annotation | 类型注释 | 在函数签名中明确声明参数/返回数据类型。 |
| Optional | 可选类型 | 允许该参数为空值或未定义的类型包装。 |

## 疑问与待验证项

- 文档列出的支持表会随 TSv2/Python SDK 版本更新；schema 自动生成和旧函数版本兼容策略需确认。
- Python UDF 在 Pipeline Builder 中的返回类型语义与常规服务函数不同，应按使用场景分别处理。

## 复刻启示

- 使用版本化、语言无关的函数注册 schema，并为每种语言提供显式类型映射和兼容性错误。
- API 生成器和测试/预览表单从同一输入输出契约驱动；optional、数组、对象引用等语义不能在序列化时丢失。
