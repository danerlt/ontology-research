# Palantir Ontology 与 Agent 研究资料实施计划

> **执行要求：** 按阶段完成；阶段内先写测试，再实现最小功能。阶段状态随进展更新。全部阶段完成后删除本文件。

**目标：** 编目 Palantir 官方 Ontology/Agent 文档，为全部直接相关页面制作中文研读卡片，并沉淀供后续仿制系统设计使用的需求基线。

**架构：** 使用 Python 标准库抓取官方 sitemap 与主题入口页导航，仅提取文档元数据；目录为 JSONL，研读卡片与需求基线为 Markdown。所有直接相关页面由目录驱动生成卡片模板，并按主题人工核对原文、官方中文版本和功能状态。

**技术栈：** Python 3、标准库 `urllib`/`html.parser`/`xml.etree`/`json`/`unittest`、Markdown。此阶段不增加第三方依赖。

**设计文档：** `docs/superpowers/specs/2026-11-14-palantir-ontology-agent-docs-design.md`

## 全局约束

- 只访问 Palantir 官方公开文档域名；请求前读取并遵守 `robots.txt`。
- 站点 sitemap 最多返回 5,000 条；必须结合 Ontology、权限、Action Types、Functions、Agent、MCP 等官方主题入口页的导航链接补充发现。
- 抓取器只把标题、规范 URL、语言、栏目、更新时间、导航来源、配对链接、分类和状态写入目录；不得把文章全文落盘。
- 每份研读卡片通过官方链接指向全文；同一来源的英文直接摘录总量不超过 25 个词，并配中文译文及原创中文解读。
- `直接相关` 页面必须全部有已完成卡片；`补充参考` 页面只编目并说明关联理由。
- 标注抓取时间、人工核对时间，以及 Beta、coming soon、deprecated、更名等可能变化的状态。
- 所有面向读者的目录、卡片、计划和说明使用中文；代码标识符保持英文。
- 本计划只覆盖文档研究与需求基线。复刻系统的产品设计和实现另建设计文档与计划。

## 审查重点

- sitemap XML 格式错误或缺字段：`tests/test_palantir_docs_catalog.py::test_parse_sitemap_rejects_malformed_xml` 确认错误可见且不产生伪造条目。
- HTML 缺少标题/规范链接或导航结构变化：`tests/test_palantir_docs_catalog.py::test_parse_doc_page_reports_missing_title_and_canonical_url` 确认缺失字段与页面 URL 可诊断。
- sitemap 与导航重复发现同一页面：`tests/test_palantir_docs_catalog.py::test_merge_candidates_deduplicates_and_tracks_sources` 确认按规范 URL 去重并合并发现来源。
- 页面链接指向非 Palantir 域名、非 Foundry 文档或带追踪参数：`tests/test_palantir_docs_catalog.py::test_normalize_doc_url_rejects_external_and_non_foundry_urls` 确认只保留允许页面并规范化 URL。
- 英中页面 slug 不完全对应或功能状态不同：`tests/test_palantir_docs_catalog.py::test_find_zh_counterpart_flags_ambiguous_slug` 确认不确定配对标记为待人工核对。

---

## 阶段 1：官方文档目录抓取器

### Task 1: 官方文档目录抓取器

**目标：** 建立可重复运行的脚本，从官方 sitemap 与主题页面导航发现候选文档，只提取元数据。
**成功标准：** 可从 sitemap 和种子页收集 URL、解析页面标题/规范 URL/栏目/更新时间，按规范 URL 去重并生成 JSONL；遇到错误会记录页面与原因；不保存正文。
**测试：** `python -m unittest discover -s tests -v`；覆盖 sitemap XML、HTML 元数据、URL 安全、重复 URL 和异常页面。
**状态：** 未开始

**入口页面：**
- `https://www.palantir.com/docs/foundry/ontology/overview`
- `https://www.palantir.com/docs/foundry/action-types/overview`
- `https://www.palantir.com/docs/foundry/functions/overview`
- `https://www.palantir.com/docs/foundry/object-permissioning/overview`
- `https://www.palantir.com/docs/foundry/aip/agent-stack`
- `https://www.palantir.com/docs/foundry/agent-builder/overview`
- `https://www.palantir.com/docs/foundry/agent-sdk/getting-started`
- `https://www.palantir.com/docs/foundry/agents/overview`
- `https://www.palantir.com/docs/foundry/ontology-mcp`
- `https://www.palantir.com/docs/foundry/palantir-mcp/overview`

**文件：**
- 创建：`scripts/crawl_palantir_docs.py`
- 创建：`tests/test_palantir_docs_catalog.py`
- 生成：`data/palantir_docs_catalog.jsonl`

**接口：**
- `normalize_doc_url(url: str) -> str | None`：仅返回官方 Foundry 文档 URL，去掉追踪参数和片段。
- `is_allowed_by_robots(robots_text: str, page_url: str, user_agent: str) -> bool`：依据官方 robots 规则判断是否可请求页面。`parse_sitemap(xml_text: str) -> list[dict[str, str]]`：返回规范 URL 与可用的 `lastmod`。
- `parse_doc_page(html_text: str, page_url: str) -> dict[str, object]`：返回标题、canonical URL、描述、栏目/导航链接元数据；不返回正文。`merge_candidates(candidates: list[dict[str, object]]) -> list[dict[str, object]]`：按规范 URL 去重并合并来源。
- `crawl_catalog(seed_urls: list[str], output_path: Path, max_pages: int | None = None) -> dict[str, int]`：合并 sitemap/导航候选、低频获取页面、记录错误并写出 JSONL。

- [ ] **步骤 1：编写失败测试**：新增 `test_robots_policy_denies_disallowed_path`（断言 robots 禁止的路径不可请求）；新增 `test_parse_sitemap_extracts_lastmod_and_deduplicates_urls`（断言规范 URL/lastmod 与去重）；新增 `test_parse_sitemap_rejects_malformed_xml`（断言错误可定位）；新增 `test_parse_doc_page_extracts_metadata_without_body`（断言返回标题、描述、导航链接且不含正文）；新增 `test_parse_doc_page_reports_missing_title_and_canonical_url`（断言缺失字段可诊断）；新增 `test_normalize_doc_url_rejects_external_and_non_foundry_urls`（断言拒绝外域及非 Foundry 页）。
- [ ] **步骤 2：运行测试确认失败**：运行 `python -m unittest discover -s tests -v`；预期缺少被测函数导致失败。
- [ ] **步骤 3：实现纯解析函数**：在 `scripts/crawl_palantir_docs.py` 中实现上述 URL、sitemap 和 HTML 解析接口。
- [ ] **步骤 4：运行测试确认通过**：重复运行同一 unittest 命令，预期新增测试通过。
- [ ] **步骤 5：实现低频网络抓取与 JSONL 输出**：添加官方主题入口种子、robots 检查、请求间隔、有限重试和可读错误记录。
- [ ] **步骤 6：执行一次有页数上限的真实编目**：输出候选目录并查看失败记录，确认目录记录没有正文内容。

## 阶段 2：完整编目、分类与英中配对

### Task 2: 完整编目与英中配对

**目标：** 完成 Ontology/Agent 相关页面发现，逐页判为直接相关或补充参考，查找官方中文对应页面。
**成功标准：** 每个目录项包含语言、栏目、发现来源、关联理由、相关性、英文/中文链接、研读状态；所有直接相关页面进入待研读清单；可疑配对显式标记人工核对。
**测试：** 单元测试覆盖路由分类、中文 URL 配对、重复别名和不确定配对；运行完整 unittest 命令。
**状态：** 未开始

**文件：**
- 修改：`scripts/crawl_palantir_docs.py`
- 修改：`tests/test_palantir_docs_catalog.py`
- 创建：`docs/research/README.md`
- 更新：`data/palantir_docs_catalog.jsonl`

- [ ] **步骤 1：写分类与配对失败测试**：新增 `test_classify_page_marks_direct_ontology_agent_pages`（断言本体/动作/权限/Agent/MCP 页为直接相关）；新增 `test_classify_page_marks_unrelated_analytics_supplement`（断言通用分析页为补充参考）；新增 `test_find_zh_counterpart_matches_discovered_translation`（断言正确配对）；新增 `test_find_zh_counterpart_flags_ambiguous_slug`（断言不确定配对需人工复核）。
- [ ] **步骤 2：运行测试确认失败**：运行 `python -m unittest discover -s tests -v`。
- [ ] **步骤 3：实现分类与配对**：添加 `classify_page(url, title, description)` 和 `find_zh_counterpart(en_url, discovered_urls)`；分类结果包含值、理由与置信状态。
- [ ] **步骤 4：运行测试确认通过**：运行完整 unittest 命令。
- [ ] **步骤 5：人工复核候选清单**：检查主要主题导航覆盖、Sitemap 上限造成的缺口、中文译页错配和页面状态，按设计文档的相关性规则修正目录。
- [ ] **步骤 6：生成中文索引**：在 `docs/research/README.md` 汇总主题、页面数、直接相关页数、中文覆盖情况、待复核和抓取失败记录。

## 阶段 3：研读卡片模板与本体治理批次

### Task 3: 研读卡片与本体治理

**目标：** 为每个直接相关页面生成卡片模板，并完成本体基础/管理、动作/函数/权限批次的所有直接相关页面。
**成功标准：** 每篇卡片包含英中来源、核对日期、短摘录与译文、原创中文要点、术语、疑问、复刻启示；本体和治理主题下所有直接相关目录项均标记完成。
**测试：** 测试卡片文件名稳定、模板链接/字段完整、仅直接相关页面生成必读卡片；运行完整 unittest 命令，并用覆盖检查确认直接相关页面全部有卡片。
**状态：** 未开始

**文件：**
- 创建：`scripts/build_research_cards.py`
- 创建：`scripts/check_research_coverage.py`
- 创建：`tests/test_research_cards.py`
- 创建：`docs/research/articles/_TEMPLATE.md`
- 创建：`docs/research/articles/ontology/` 下对应研读卡片
- 创建：`docs/research/articles/governance/` 下对应研读卡片
- 修改：`data/palantir_docs_catalog.jsonl`
- 修改：`docs/research/README.md`

- [ ] **步骤 1：写模板生成/覆盖检查失败测试**：新增 `test_card_filename_is_stable_for_doc_url`（断言稳定文件名）；新增 `test_build_card_contains_source_metadata_and_required_sections`（断言标题、英中链接、日期和研读小节齐全）；新增 `test_build_research_cards_skips_supplement_reference`（断言只生成直接相关卡片）；新增 `test_coverage_checker_reports_missing_direct_card`（断言缺卡时检查失败）；新增 `test_card_validation_rejects_more_than_25_english_words`（断言超出摘录上限时报错）。
- [ ] **步骤 2：运行测试确认失败**：运行 `python -m unittest discover -s tests -v`。
- [ ] **步骤 3：实现模板与覆盖检查器**：模板预填标题、URL、官方中文链接、类别、日期、状态和待填写小节；覆盖检查器逐页核验目录与卡片状态，并检查每篇英文摘录不超过 25 词。
- [ ] **步骤 4：运行测试确认通过**：运行完整 unittest 命令。
- [ ] **步骤 5：完成本体/治理主题卡片**：按主题批次核对官方英文和中文页面，逐篇补充短摘录、译文、解读、术语、问题、复刻启示与核对日期。
- [ ] **步骤 6：更新目录和批次状态**：仅在卡片各字段完成后将该页面标记为已完成。
- [ ] **步骤 7：运行覆盖检查**：运行 `python scripts/check_research_coverage.py`；预期本阶段主题的直接相关页面未完成数为 0。

## 阶段 4：Agent、Ontology MCP 与平台 MCP 批次

### Task 4: Agent 与 MCP 研读

**目标：** 完成 Agent 构建/运行与通过 Ontology/MCP 接入本体主题下所有直接相关页面。
**成功标准：** Agent Builder、Agent SDK、Agent Stack/Manager、Pro-code agents、Ontology MCP、Palantir MCP，以及 AIP Logic/Workshop/Automate/SDK 中符合范围的页面均有完成卡片；区分本体数据操作与本体结构管理、区分 Agent 消费端与开发端权限。
**测试：** 运行完整 unittest 和覆盖检查；人工按来源链接复核产品名称、权限边界、审批/审计与 Beta/coming soon 状态。
**状态：** 未开始

**文件：**
- 创建：`docs/research/articles/agents/` 下对应研读卡片
- 创建：`docs/research/articles/mcp/` 下对应研读卡片
- 修改：`data/palantir_docs_catalog.jsonl`
- 修改：`docs/research/README.md`
- 修改：`scripts/check_research_coverage.py`（仅在覆盖检查确需调整时）

- [ ] **步骤 1：完成 Agent 构建/运行卡片**：逐篇梳理 Agent Builder、Agent SDK、Agent Stack、Agent Manager、Pro-code agents 及范围内的 AIP Logic 页面。
- [ ] **步骤 2：完成 Agent/MCP 集成卡片**：逐篇梳理 Ontology MCP 与 Palantir MCP，覆盖资源暴露、权限限制、工具、提案审查、外部数据流、安全和审计。
- [ ] **步骤 3：检查页面状态和术语一致性**：复核 Agent Studio/Chatbot Studio/Agent Builder 等名称以及文档中的 Beta、路线图和弃用说明。
- [ ] **步骤 4：运行完整 unittest 与覆盖检查**：预期所有直接相关页面未完成数为 0。
- [ ] **步骤 5：更新主题索引**：补齐页面状态、官方中文覆盖、疑问和来源日期。

## 阶段 5：复刻需求基线与系统设计交接

### Task 5: 复刻需求基线

**目标：** 汇总公开文档支持的功能与设计推论，交付下一阶段本体管理系统设计输入。
**成功标准：** `replica-requirements.md` 清晰划分本体模型、元数据管理、数据读写、动作/函数、权限、版本/审批、Agent 接入、审计和可观测性；每项标注来源与“官方明示/设计推论”；未决产品范围列为下一阶段问题。
**测试：** 运行完整 unittest 和覆盖检查；人工逐项确认需求有来源链接，事实与推论分开，未将 Palantir 私有实现当成事实。
**状态：** 未开始

**文件：**
- 创建：`docs/research/replica-requirements.md`
- 修改：`docs/research/README.md`

- [ ] **步骤 1：按系统能力整理证据**：从研读卡片提取实体/链接/动作、权限、写入审计、Agent 工具、审批和操作观测能力。
- [ ] **步骤 2：标注事实与推论**：每条需求附支持它的官方来源链接，并区分官方文档直接陈述和本项目的设计判断。
- [ ] **步骤 3：复核全部直接相关卡片覆盖**：运行 `python -m unittest discover -s tests -v` 和 `python scripts/check_research_coverage.py`；预期测试通过且未完成页数为 0。
- [ ] **步骤 4：交接下一阶段**：基于该需求基线重新进行本体管理系统产品设计和实施规划，再选择 Vue/React、FastAPI、PostgreSQL/MySQL、Redis、Docker 和服务边界；本计划完成后删除。





