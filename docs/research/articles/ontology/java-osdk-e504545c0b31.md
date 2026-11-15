<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/java-osdk -->
<!-- 研读状态：已完成 -->

# Ontology SDK • Java • Java OSDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/java-osdk)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/java-osdk)（配对状态：matched；页面声明 AIP 机器翻译且准确性未验证）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:36Z
- 产品状态：本参考页未将 Java OSDK 整体标为 Beta；Object Storage v1 有 10,000 条限制，Java 读取暂不支持属性投影

## 英文原文短摘录（每个来源不超过 25 词）

> “Java OSDK uses `FetchRequest` for single-object and stream options, and `FetchPageRequest` for manual pagination options.”

## 摘录译文

Java OSDK 使用类型化请求对象区分单对象/流式读取与手动分页读取。

## 中文要点

- 本页是基于示例 `Restaurant` 的通用 Java SDK 指南；应用专属类型、API 名称和代码由 Developer Console 按目标 Ontology 生成。
- 读取方式包括按主键获取、流式读取、手动分页、排序、类型化过滤与分组聚合。分页令牌和页大小由 `FetchPageRequest` 管理；读请求可选择是否带 RID 和属性安全元数据。
- 过滤表达式由生成的对象类型属性构造，支持组合布尔条件；聚合可按精确值、数值区间或日期时间区间分组，并计算 count、sum、avg、min、max、近似去重等指标。
- Action 类型也会按 Ontology 生成；调用返回校验结果与编辑摘要，调用方应分别处理有效、无效结果。
- 数据读取上限取决于底层对象存储：文档说明 Object Storage v1（Phonograph）读取超过 10,000 个对象会报错；v2 没有该请求数限制。不能把 SDK 的流接口误认为绕过存储限制。
- 一个值得注意的 SDK 边界：虽然 `FetchRequest` 声明 `selectedProperties`，当前生成的 Java OSDK 读取方法并未将其应用到请求，因此 Java SDK 目前不支持属性级投影。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `FetchRequest` / `FetchPageRequest` | 读取请求 / 分页请求 | 分别配置单对象、流式和显式分页读取；分页令牌用于继续读取。 |
| `ObjectSet` | 对象集 | 由过滤、排序、链接或聚合操作组合出的查询集合。 |
| `Action Type` | 操作类型 | 由本体定义生成的写入操作；应用时返回验证结果和编辑。 |
| `selectedProperties` | 指定属性 | 请求模型含此字段，但当前生成 Java 读取方法不支持按属性挑选。 |

## 疑问与待验证项

- “v2 没有请求限制”是针对该页面描述的对象读取端点；仍需对照具体 API、分页上限和租户配额，不应泛化成无容量限制。
- Java 页有官方中文路由，但中文内容声明由 AIP 机器翻译且准确性未验证；涉及 API 能力的判断以英文原页为准。
- Java 当前不支持属性投影与 Python SDK 当前支持属性列表的差异，是否由 SDK 生成器版本或特定读取方法造成，需要按生成版本实测。
- 页面示例中的对象名偶有误用（如 Restaurant 与 Aircraft 混杂），复刻时应从 schema 元数据生成类型和示例，不能照抄示例中的错名。

## 复刻启示

- 在 SDK/API 设计说明中为每种语言记录能力矩阵，清楚区分平台统一语义与客户端语言差异；不要只根据一种 SDK 推断整个平台能力。
- 建模读取请求时，显式表示 RID、属性安全元数据、分页令牌、快照语义与属性投影，并让 UI 按后端真正支持的能力呈现。
- 查询构造器应是类型化本体字段的组合表达式；在服务端建立同一套可校验查询 AST，驱动预览、聚合和权限检查，而不是接受任意 SQL。
- Action 调用应分别返回参数/提交约束校验与拟执行编辑，供确认、审计和结果检查；不要把“校验通过”直接展示成“数据已提交”。
