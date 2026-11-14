"""仅编目 Palantir Foundry Ontology 与 Agent 文档的元数据。"""

from __future__ import annotations

from collections import deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import gzip
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from threading import Lock
import time
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET


OFFICIAL_HOSTS = {"palantir.com", "www.palantir.com"}
FOUNDRY_DOC_PATHS = ("/docs/foundry", "/docs/zh/foundry")
ROBOTS_URL = "https://www.palantir.com/robots.txt"
SITEMAP_URL = "https://www.palantir.com/docs/sitemap.xml"
USER_AGENT = "OntologyAgentDocCatalog/1.0"
REQUEST_DELAY_SECONDS = 0.5
MAX_FETCH_ATTEMPTS = 3
DEFAULT_MAX_CONCURRENCY = 8

DEFAULT_SEED_URLS = [
    "https://www.palantir.com/docs/foundry/ontology/overview",
    "https://www.palantir.com/docs/foundry/action-types/overview",
    "https://www.palantir.com/docs/foundry/functions/overview",
    "https://www.palantir.com/docs/foundry/object-permissioning/overview",
    "https://www.palantir.com/docs/foundry/aip/agent-stack",
    "https://www.palantir.com/docs/foundry/agent-builder/overview",
    "https://www.palantir.com/docs/foundry/agent-sdk/getting-started",
    "https://www.palantir.com/docs/foundry/agents/overview",
    "https://www.palantir.com/docs/foundry/ontology-mcp",
    "https://www.palantir.com/docs/foundry/palantir-mcp/overview",
]

DISCOVERY_PATH_MARKERS = (
    "ontolog",
    "/object-types",
    "/action-types",
    "/object-permissioning",
    "/functions/",
    "/agent",
    "/aip/logic",
    "/palantir-mcp",
    "/mcp/",
    "/osdk/",
    "/developer-console/",
    "/workshop/agent",
    "/automate/agent",
)


def normalize_doc_url(url: str) -> str | None:
    """规范化 Palantir Foundry 文档链接；拒绝非官方或非 Foundry 页面。"""
    try:
        parsed = urlsplit(url.strip())
        hostname = (parsed.hostname or "").lower()
        port = parsed.port
    except ValueError:
        return None

    if parsed.scheme.lower() not in {"http", "https"}:
        return None
    if hostname not in OFFICIAL_HOSTS:
        return None
    if port is not None and port not in {80, 443}:
        return None

    path = parsed.path.rstrip("/") or "/"
    is_foundry_doc = any(
        path == prefix or path.startswith(prefix + "/")
        for prefix in FOUNDRY_DOC_PATHS
    )
    if not is_foundry_doc:
        return None

    return urlunsplit(("https", "www.palantir.com", path, "", ""))


def is_allowed_by_robots(
    robots_text: str, page_url: str, user_agent: str
) -> bool:
    """使用站点 robots.txt 规则判断是否允许抓取页面。"""
    parser = RobotFileParser()
    parser.parse(robots_text.splitlines())
    return parser.can_fetch(user_agent, page_url)


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def merge_candidates(
    candidates: list[dict[str, object]],
) -> list[dict[str, object]]:
    """按规范 URL 合并候选页，保留最新日期和全部发现来源。"""
    merged_by_url: dict[str, dict[str, object]] = {}

    for candidate in candidates:
        raw_url = candidate.get("url") or candidate.get("page_url")
        if not isinstance(raw_url, str):
            continue
        normalized_url = normalize_doc_url(raw_url)
        if normalized_url is None:
            continue

        existing = merged_by_url.setdefault(normalized_url, {"url": normalized_url})
        sources = set(existing.get("discovered_from", []))
        candidate_sources = candidate.get("discovered_from", [])
        if isinstance(candidate_sources, str):
            sources.add(candidate_sources)
        elif isinstance(candidate_sources, (list, tuple, set)):
            sources.update(
                source for source in candidate_sources if isinstance(source, str)
            )

        for key, value in candidate.items():
            if key in {"url", "page_url", "discovered_from"} or value in (None, "", []):
                continue
            if key == "lastmod" and existing.get(key):
                existing[key] = max(str(existing[key]), str(value))
            elif not existing.get(key):
                existing[key] = value

        if sources:
            existing["discovered_from"] = sorted(sources)

    return [merged_by_url[url] for url in sorted(merged_by_url)]


def parse_sitemap(xml_text: str) -> list[dict[str, str]]:
    """解析 sitemap 中的 Foundry 文档 URL 与更新时间。"""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise ValueError(f"无法解析官方 sitemap XML：{exc}") from exc

    candidates: list[dict[str, object]] = []
    for entry in root.iter():
        if _local_name(entry.tag) != "url":
            continue
        values = {_local_name(child.tag): (child.text or "").strip() for child in entry}
        normalized_url = normalize_doc_url(values.get("loc", ""))
        if normalized_url is None:
            continue
        candidates.append(
            {
                "url": normalized_url,
                "lastmod": values.get("lastmod", ""),
                "discovered_from": ["sitemap"],
            }
        )

    return [
        {key: str(value) for key, value in candidate.items() if key != "discovered_from"}
        for candidate in merge_candidates(candidates)
    ]


class _DocPageParser(HTMLParser):
    """只提取页面头部和侧边导航，不收集正文文本。"""

    def __init__(self, page_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.title_parts: list[str] = []
        self.description = ""
        self.canonical_url: str | None = None
        self.navigation_links: list[str] = []
        self.missing_fields: list[str] = []
        self._in_head = False
        self._in_title = False
        self._document_title_seen = False
        self._nav_stack: list[bool] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name.lower(): value or "" for name, value in attrs}
        tag = tag.lower()

        if tag == "head":
            self._in_head = True
        elif tag == "title" and self._in_head and not self._document_title_seen:
            self._in_title = True
        elif tag == "meta":
            meta_name = attributes.get("name", "").lower()
            if meta_name == "description" and not self.description:
                self.description = attributes.get("content", "").strip()
        elif tag == "link" and "canonical" in attributes.get("rel", "").lower().split():
            raw_canonical = urljoin(self.page_url, attributes.get("href", ""))
            self.canonical_url = normalize_doc_url(raw_canonical)
        elif tag == "nav":
            classes = attributes.get("class", "").lower()
            parent_is_sidebar = bool(self._nav_stack and self._nav_stack[-1])
            is_toc = "toc" in classes
            is_sidebar = not is_toc and (parent_is_sidebar or "sidebar" in classes)
            self._nav_stack.append(is_sidebar)
        elif tag == "a" and self._nav_stack and self._nav_stack[-1]:
            raw_href = urljoin(self.page_url, attributes.get("href", ""))
            normalized_href = normalize_doc_url(raw_href)
            if normalized_href and normalized_href not in self.navigation_links:
                self.navigation_links.append(normalized_href)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            if self._in_title:
                self._document_title_seen = True
            self._in_title = False
        elif tag == "head":
            self._in_head = False
        elif tag == "nav" and self._nav_stack:
            self._nav_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title_parts.append(data)


def parse_doc_page(html_text: str, page_url: str) -> dict[str, object]:
    """提取标题、规范链接、描述和侧边栏链接，不返回文章正文。"""
    parser = _DocPageParser(page_url)
    parser.feed(html_text)
    title = " ".join("".join(parser.title_parts).split())
    missing_fields = []
    if not title:
        missing_fields.append("title")
    if parser.canonical_url is None:
        missing_fields.append("canonical_url")

    return {
        "page_url": normalize_doc_url(page_url) or page_url,
        "title": title,
        "canonical_url": parser.canonical_url,
        "description": parser.description,
        "navigation_links": parser.navigation_links,
        "missing_fields": missing_fields,
    }


def fetch_text(url: str, timeout_seconds: int = 20) -> str:
    """获取公开页面文本；调用方负责 robots 检查和请求节奏。"""
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xml,text/xml,*/*;q=0.5",
            "Accept-Encoding": "gzip",
        },
    )
    with urlopen(request, timeout=timeout_seconds) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        payload = response.read()
        if response.headers.get("Content-Encoding", "").lower() == "gzip":
            payload = gzip.decompress(payload)
        return payload.decode(charset, errors="replace")


def _is_discovery_candidate(url: str) -> bool:
    normalized_url = normalize_doc_url(url)
    if normalized_url is None:
        return False
    path = urlsplit(normalized_url).path.lower()
    return any(marker in path for marker in DISCOVERY_PATH_MARKERS)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _failed_page_record(candidate: dict[str, object], error: Exception) -> dict[str, object]:
    url = str(candidate["url"])
    return {
        "url": url,
        "section": _get_doc_section(url),
        "canonical_url": None,
        "title": "",
        "description": "",
        "language": "zh" if "/zh/foundry/" in url else "en",
        "lastmod": str(candidate.get("lastmod", "")),
        "discovered_from": list(candidate.get("discovered_from", [])),
        "navigation_link_count": 0,
        "missing_fields": ["title", "canonical_url"],
        "fetch_status": "error",
        "error": f"{type(error).__name__}: {error}",
        "checked_at": _utc_now(),
    }


DIRECT_DOC_SECTIONS = {
    "ontology": "本体模型与治理文档",
    "ontologies": "本体管理与治理文档",
    "object-types": "对象类型与本体建模文档",
    "action-types": "本体动作文档",
    "object-permissioning": "本体对象权限文档",
    "object-link-types": "本体对象链接类型文档",
    "functions": "本体函数文档",
    "ontology-resources": "Ontology API 兼容参考",
    "ontologies-v2-resources": "Ontology REST API v2 参考",
    "aip-agents-v2-resources": "Agent REST API v2 参考",
    "sql-queries-v2-resources": "Ontology SQL API 参考",
    "ontology-sdk": "Ontology SDK 文档",
    "ontology-sdk-react-applications": "Ontology SDK 应用开发文档",
    "ontology-manager": "本体管理器文档",
    "agent-manager": "Agent Manager 文档",
    "aip-evals": "Ontology 与 Agent 评估文档",
    "aip": "AIP Agent 平台文档",
    "assist": "AIP Assist Agent 文档",
    "foundryts": "Ontology 查询 SDK 文档",
    "dynamic-scheduling": "Ontology 数据模型配置文档",
    "time-series": "Ontology 时间序列数据文档",
    "geotemporal-series": "Ontology 地理时间序列文档",
    "agent-builder": "Agent 构建文档",
    "agent-sdk": "Agent SDK 文档",
    "agents": "Agent 文档",
    "ontology-mcp": "Ontology MCP 文档",
    "palantir-mcp": "Palantir MCP 文档",
    "mcp": "MCP 集成文档",
    "osdk": "Ontology SDK 文档",
    "developer-console": "开发者控制台与本体集成文档",
    "workshop": "Workshop Agent 应用文档",
    "automate": "Automate Agent 文档",
}


def classify_page(url: str, title: str, description: str) -> dict[str, str]:
    """按文档路径和页面元数据分类；低置信结果保留人工复核标记。"""
    normalized_url = normalize_doc_url(url) or url
    path = urlsplit(normalized_url).path.lower()
    page_text = f"{title} {description}".lower()
    if "/data-connection/" in path and "agent" in page_text:
        return {
            "relevance": "supplement",
            "relevance_reason": "此处的 Agent 指数据连接代理运行时，不是 AIP 本体 Agent",
            "classification_confidence": "high",
            "classification_status": "rule_matched",
        }
    if "/geospatial/" in path and "ontology" in page_text:
        return {
            "relevance": "supplement",
            "relevance_reason": "该页介绍 Gaia 地理空间应用如何消费本体数据，属于下游集成示例",
            "classification_confidence": "high",
            "classification_status": "rule_matched",
        }
    if "/api/v1/" in path or "(v1)" in title.lower():
        return {
            "relevance": "direct",
            "relevance_reason": "Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2",
            "classification_confidence": "high",
            "classification_status": "rule_matched",
        }

    path_segments = [segment for segment in path.split("/")]
    section_reason = next(
        (
            reason
            for segment, reason in DIRECT_DOC_SECTIONS.items()
            if segment in path_segments
        ),
        None,
    )
    if section_reason:
        return {
            "relevance": "direct",
            "relevance_reason": section_reason,
            "classification_confidence": "high",
            "classification_status": "rule_matched",
        }

    related_terms = (
        "ontology",
        "object type",
        "object-type",
        "action type",
        "action-type",
        "agent",
        "permission",
        "mcp",
    )
    if any(term in page_text for term in related_terms):
        return {
            "relevance": "direct",
            "relevance_reason": "标题或简介提及本体、对象、动作、权限或 Agent 主题",
            "classification_confidence": "medium",
            "classification_status": "needs_review",
        }

    return {
        "relevance": "supplement",
        "relevance_reason": "路径、标题和简介未命中本体或 Agent 主题规则",
        "classification_confidence": "medium",
        "classification_status": "needs_review",
    }


def _get_doc_section(url: str) -> str:
    path = urlsplit(url).path
    for prefix in ("/docs/zh/foundry/", "/docs/foundry/"):
        if path.startswith(prefix):
            sections = path[len(prefix) :].strip("/").split("/")
            if not sections or not sections[0]:
                return "foundry"
            if sections[0] == "api":
                return "/".join(sections[:3])
            return sections[0]
    return "foundry"


def _slug_terms(url: str) -> set[str]:
    path = urlsplit(url).path.lower()
    path = path.replace("/docs/zh/foundry/", "", 1)
    path = path.replace("/docs/foundry/", "", 1)
    return {
        term
        for term in re.split(r"[/_-]+", path)
        if term and term not in {"overview", "getting", "started", "docs", "foundry"}
    }


def find_zh_counterpart(
    english_url: str, discovered_urls: list[str]
) -> dict[str, object]:
    """按完全相同的文档路由配对；近似 slug 仅作为人工核对候选。"""
    normalized_english_url = normalize_doc_url(english_url)
    if normalized_english_url is None or "/docs/zh/foundry/" in normalized_english_url:
        return {"status": "not_applicable", "counterpart_url": None, "candidates": []}

    english_path = urlsplit(normalized_english_url).path
    expected_zh_path = english_path.replace(
        "/docs/foundry/", "/docs/zh/foundry/", 1
    )
    zh_urls = sorted(
        {
            normalized_url
            for raw_url in discovered_urls
            if (normalized_url := normalize_doc_url(raw_url)) is not None
            and "/docs/zh/foundry/" in normalized_url
        }
    )
    exact_matches = [
        url for url in zh_urls if urlsplit(url).path == expected_zh_path
    ]
    if len(exact_matches) == 1:
        return {
            "status": "matched",
            "counterpart_url": exact_matches[0],
            "candidates": exact_matches,
        }
    if exact_matches:
        return {
            "status": "needs_review",
            "counterpart_url": None,
            "candidates": exact_matches,
        }

    english_terms = _slug_terms(normalized_english_url)
    suggestions = []
    for zh_url in zh_urls:
        zh_terms = _slug_terms(zh_url)
        if english_terms and len(english_terms & zh_terms) / len(english_terms) >= 0.5:
            suggestions.append(zh_url)
    if suggestions:
        return {
            "status": "needs_review" if len(suggestions) == 1 else "ambiguous",
            "counterpart_url": None,
            "candidates": suggestions,
        }

    return {"status": "missing", "counterpart_url": None, "candidates": []}


def crawl_catalog(
    seed_urls: list[str],
    output_path: Path,
    max_pages: int | None = None,
    max_concurrency: int = DEFAULT_MAX_CONCURRENCY,
    progress_callback: Callable[[dict[str, int]], None] | None = None,
) -> dict[str, int]:
    """读取 sitemap 和主题侧边栏，只把文档元数据写入 JSONL。"""
    if max_concurrency < 1:
        raise ValueError("max_concurrency 必须大于 0")
    try:
        robots_text = fetch_text(ROBOTS_URL)
    except (HTTPError, URLError, OSError, TimeoutError) as exc:
        raise RuntimeError(f"读取 robots.txt 失败，已停止抓取：{exc}") from exc

    if not is_allowed_by_robots(robots_text, SITEMAP_URL, USER_AGENT):
        raise RuntimeError("robots.txt 不允许读取官方文档 sitemap，已停止抓取")

    try:
        sitemap_text = fetch_text(SITEMAP_URL)
        sitemap_pages = parse_sitemap(sitemap_text)
    except (HTTPError, URLError, OSError, TimeoutError, ValueError) as exc:
        raise RuntimeError(f"读取或解析官方文档 sitemap 失败：{exc}") from exc

    candidates_by_url: dict[str, dict[str, object]] = {}
    pairing_urls = {page["url"] for page in sitemap_pages}
    queue: deque[str] = deque()
    queued_urls: set[str] = set()

    def enqueue(candidate: dict[str, object], source: str | None = None) -> None:
        raw_url = candidate.get("url") or candidate.get("page_url")
        if not isinstance(raw_url, str):
            return
        normalized_url = normalize_doc_url(raw_url)
        if normalized_url is None:
            return
        pairing_urls.add(normalized_url)
        if source != "seed" and not _is_discovery_candidate(normalized_url):
            return

        normalized_candidate = dict(candidate)
        normalized_candidate["url"] = normalized_url
        if source:
            normalized_candidate["discovered_from"] = [source]
        current = candidates_by_url.get(normalized_url)
        if current is not None:
            candidates_by_url[normalized_url] = merge_candidates(
                [current, normalized_candidate]
            )[0]
            return

        candidates_by_url[normalized_url] = normalized_candidate
        if normalized_url not in queued_urls:
            queue.append(normalized_url)
            queued_urls.add(normalized_url)

    def pairing_candidates() -> list[str]:
        return sorted(pairing_urls | candidates_by_url.keys())

    for seed_url in seed_urls:
        enqueue({"url": seed_url}, "seed")
    for sitemap_page in sitemap_pages:
        if _is_discovery_candidate(sitemap_page["url"]):
            enqueue(sitemap_page, "sitemap")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint_path = output_path.with_suffix(output_path.suffix + ".checkpoint")
    records_by_url: dict[str, dict[str, object]] = {}
    if checkpoint_path.exists():
        for line_number, line in enumerate(
            checkpoint_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"抓取检查点格式错误：{checkpoint_path} 第 {line_number} 行"
                ) from exc
            if not isinstance(record, dict) or not isinstance(record.get("url"), str):
                raise ValueError(
                    f"抓取检查点缺少页面 URL：{checkpoint_path} 第 {line_number} 行"
                )
            records_by_url[record["url"]] = record

    discovered_urls = pairing_candidates()
    for url, record in records_by_url.items():
        record["section"] = _get_doc_section(url)
        _add_research_annotations(record, discovered_urls)

    completed_urls = {
        url
        for url, record in records_by_url.items()
        if record.get("fetch_status") != "error"
    }
    attempted = len(completed_urls)
    last_request_at: float | None = None
    request_lock = Lock()

    def fetch_with_policy(url: str) -> str:
        nonlocal last_request_at
        if not is_allowed_by_robots(robots_text, url, USER_AGENT):
            raise PermissionError(f"robots.txt 不允许抓取：{url}")

        for attempt in range(MAX_FETCH_ATTEMPTS):
            with request_lock:
                if last_request_at is not None:
                    elapsed = time.monotonic() - last_request_at
                    wait_seconds = max(0.0, REQUEST_DELAY_SECONDS - elapsed)
                    if wait_seconds:
                        time.sleep(wait_seconds)
                last_request_at = time.monotonic()
            try:
                return fetch_text(url)
            except (HTTPError, URLError, OSError, TimeoutError) as exc:
                if attempt + 1 == MAX_FETCH_ATTEMPTS:
                    raise
                time.sleep(REQUEST_DELAY_SECONDS * (2**attempt))
        raise RuntimeError("抓取重试循环意外结束")

    with ThreadPoolExecutor(max_workers=max_concurrency) as executor:
        while queue and (max_pages is None or attempted < max_pages):
            batch: list[tuple[str, dict[str, object], object]] = []
            batch_records: list[dict[str, object]] = []
            while (
                queue
                and len(batch) < max_concurrency
                and (max_pages is None or attempted < max_pages)
            ):
                url = queue.popleft()
                candidate = candidates_by_url[url]
                if url in completed_urls:
                    continue
                attempted += 1

                if not is_allowed_by_robots(robots_text, url, USER_AGENT):
                    record = _failed_page_record(
                        candidate, PermissionError("robots.txt 不允许抓取")
                    )
                    _add_research_annotations(record, pairing_candidates())
                    records_by_url[url] = record
                    batch_records.append(record)
                    continue

                future = executor.submit(fetch_with_policy, url)
                batch.append((url, candidate, future))

            for url, candidate, future in batch:
                try:
                    html_text = future.result()
                except PermissionError as exc:
                    record = _failed_page_record(candidate, exc)
                    _add_research_annotations(record, pairing_candidates())
                except Exception as exc:  # 每个页面单独记录失败，继续处理剩余目录。
                    record = _failed_page_record(candidate, exc)
                    _add_research_annotations(record, pairing_candidates())
                else:
                    metadata = parse_doc_page(html_text, url)
                    record = {
                        "url": url,
                        "section": _get_doc_section(url),
                        "canonical_url": metadata["canonical_url"],
                        "title": metadata["title"],
                        "description": metadata["description"],
                        "language": "zh" if "/zh/foundry/" in url else "en",
                        "lastmod": str(candidate.get("lastmod", "")),
                        "discovered_from": sorted(candidate.get("discovered_from", [])),
                        "navigation_link_count": len(metadata["navigation_links"]),
                        "missing_fields": metadata["missing_fields"],
                        "fetch_status": "metadata_incomplete" if metadata["missing_fields"] else "ok",
                        "checked_at": _utc_now(),
                    }
                    _add_research_annotations(record, pairing_candidates())
                    completed_urls.add(url)

                    for navigation_url in metadata["navigation_links"]:
                        if _is_discovery_candidate(navigation_url):
                            enqueue({"url": navigation_url}, "navigation")

                records_by_url[url] = record
                batch_records.append(record)

            if batch_records:
                with checkpoint_path.open("a", encoding="utf-8", newline="\n") as checkpoint_file:
                    for record in batch_records:
                        checkpoint_file.write(
                            json.dumps(record, ensure_ascii=False, sort_keys=True)
                        )
                        checkpoint_file.write("\n")
                    checkpoint_file.flush()

            if progress_callback is not None:
                progress_callback(
                    {
                        "discovered": len(candidates_by_url),
                        "attempted": attempted,
                        "fetched": len(completed_urls),
                        "failed": sum(
                            record.get("fetch_status") == "error"
                            and "PermissionError" not in str(record.get("error", ""))
                            for record in records_by_url.values()
                        ),
                        "blocked": sum(
                            "PermissionError" in str(record.get("error", ""))
                            for record in records_by_url.values()
                        ),
                        "pending": max(
                            0, len(candidates_by_url) - len(completed_urls)
                        ),
                    }
                )

    with output_path.open("w", encoding="utf-8", newline="\n") as catalog_file:
        for url in sorted(records_by_url):
            record = records_by_url[url]
            catalog_file.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            catalog_file.write("\n")

    fetched = len(completed_urls)
    pending = max(0, len(candidates_by_url) - fetched)
    if pending == 0 and checkpoint_path.exists():
        checkpoint_path.unlink()

    failed = sum(
        record.get("fetch_status") == "error"
        and "PermissionError" not in str(record.get("error", ""))
        for record in records_by_url.values()
    )
    blocked = sum(
        "PermissionError" in str(record.get("error", ""))
        for record in records_by_url.values()
    )
    return {
        "discovered": len(candidates_by_url),
        "attempted": attempted,
        "fetched": fetched,
        "failed": failed,
        "blocked": blocked,
        "pending": pending,
    }


def _add_research_annotations(
    record: dict[str, object], discovered_urls: list[str]
) -> None:
    url = str(record["url"])
    classification = classify_page(
        url,
        str(record.get("title", "")),
        str(record.get("description", "")),
    )
    zh_pair = find_zh_counterpart(url, discovered_urls)
    record.update(classification)
    record.update(
        {
            "zh_counterpart_url": zh_pair["counterpart_url"],
            "zh_pair_status": zh_pair["status"],
            "zh_pair_candidates": zh_pair["candidates"],
        }
    )


def main() -> int:
    """运行官方文档目录抓取器。"""
    import argparse

    parser = argparse.ArgumentParser(description="编目 Palantir Ontology 与 Agent 官方文档元数据")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/palantir_docs_catalog.jsonl"),
        help="JSONL 目录输出路径",
    )
    parser.add_argument("--max-pages", type=int, help="最多读取的文档页数")
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=DEFAULT_MAX_CONCURRENCY,
        help="并发读取文档页数（请求仍受全局低频限速保护）",
    )
    arguments = parser.parse_args()

    next_progress_report = 50

    def report_progress(progress: dict[str, int]) -> None:
        nonlocal next_progress_report
        if (
            progress["attempted"] >= next_progress_report
            or progress["pending"] == 0
        ):
            print(
                "抓取进度：已尝试 {attempted} 页，成功 {fetched} 页，失败 {failed} 页，"
                "受 robots 限制 {blocked} 页，待处理 {pending} 页。".format(**progress),
                flush=True,
            )
            while next_progress_report <= progress["attempted"]:
                next_progress_report += 50

    stats = crawl_catalog(
        DEFAULT_SEED_URLS,
        arguments.output,
        arguments.max_pages,
        max_concurrency=arguments.max_concurrency,
        progress_callback=report_progress,
    )
    print(
        "抓取完成：发现 {discovered} 页，读取 {fetched} 页，失败 {failed} 页，"
        "受 robots 限制 {blocked} 页，待处理 {pending} 页。目录：{path}".format(
            **stats, path=arguments.output
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
