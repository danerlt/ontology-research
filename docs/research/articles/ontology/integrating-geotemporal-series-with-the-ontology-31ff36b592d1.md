<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/geotemporal-series/integrating-geotemporal-series-with-the-ontology -->
<!-- 研读状态：已完成 -->

# 地理时间序列 • 将地理时间序列与Ontology集成 • Palantir

- 英文来源：目录登记的旧英文路由目前返回 404，尚未确认当前对应页
- 官方中文来源：[中文原文](https://www.palantir.com/docs/zh/foundry/geotemporal-series/integrating-geotemporal-series-with-the-ontology)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：geotemporal-series
- 相关性：direct；Ontology 地理时间序列文档
- 官方更新时间：2026-11-12T17:46:46.929Z
- 目录核对时间：2026-11-14T14:59:53Z
- 产品状态：旧英文路由当前返回 404；中文页面仅为集成入口摘要

<!-- 研读状态：已完成 -->
## 原文短摘录与翻译

> “该类型引用地理时间序列同步中的单个序列”

## 摘录说明

保留官方中文路由中的短句。正文提示该页面由 AIP 从英文机器翻译，准确性未验证；目录登记的旧英文路由目前返回 404，暂未确认新英文页。

## 中文要点

- 接入 Ontology 需要创建地理时间序列对象类型；它引用同步中的一个序列，并带有 Geotemporal Series Reference 属性。
- Pipeline Builder 配置地理时间序列同步，使用 Geotemporal Series 输出，也可同时配置普通 Object 输出。
- 通过对象引用，Foundry 应用能围绕业务实体分析和可视化时空序列；数据本身仍是序列资源，不是普通静态标量。
- 本页是简短入口，字段契约依赖对象类型、同步和引用属性专题文档。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Geotemporal series object type | 地理时间序列对象类型 | 将同步后的时空序列暴露到 Ontology 的对象类型 |
| Geotemporal Series Reference | 地理时间序列引用 | 对象上指向地理时间序列数据的属性 |
| Geotemporal Series output | 地理时间序列输出 | Pipeline Builder 配置的时空数据输出类型 |

## 疑问与待验证项

- 旧英文 URL 当前返回 404；新页面地址、序列标识、采样和时间范围语义仍需核验。
- Reference 的官方类型定义需查英文类型参考，不应依赖未验证的机器翻译。

## 复刻启示

- 在属性类型中区分标量、时间序列引用和地理时间序列引用，分别配置查询与可视化适配器。
- 画布显示业务对象到序列资源的引用边，并保留同步来源、序列标识及时间空间上下文。