<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/parameter-performance-considerations -->
<!-- 研读状态：已完成 -->

# 动作类型 • 参数配置性能注意事项 • Performance considerations for parameter configuration • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameter-performance-considerations)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:57Z
- 产品状态：参数默认值和选项间的依赖会串行加载表单；扁平依赖可并行计算，降低交互等待。

## 英文原文短摘录（每个来源不超过 25 词）

> “it is recommended to keep the dependency hierarchy as flat as possible.”

## 摘录译文

建议尽量保持依赖层级扁平。

## 中文要点

- 文档展示对象参数默认值→第二参数派生对象属性→第三参数按第二参数查询选项的三级依赖。
- 表单加载需要依次取对象、算属性默认值、查询下拉选项，链式依赖增加首屏可交互延迟。
- 如果第三参数改为直接引用第一对象参数，第二/第三参数需要的信息可并行导出。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Parameter dependency | 参数依赖 | 一个参数的默认值/选项使用另一个参数 |
| Object set options | 对象集选项 | 从限定对象集合提取多选值 |
| Dependency hierarchy | 依赖层级 | 表单参数值推导之间的先后关系 |

## 疑问与待验证项

- 文档未提供参数求值超时或缓存策略的固定指标，实际延迟需按数据量和查询运行环境测量。
- 依赖扁平化需保持业务筛选语义；不能为了并行而绕开授权过滤。

## 复刻启示

- 保存参数依赖 DAG，检测可并行分支并提示过长串行链；表单可按依赖完成度增量启用。
- 测量对象集来源、属性默认值和选项查询各自的延迟，并将授权过滤视为查询计划的一部分。
