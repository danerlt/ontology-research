"""为直接相关的 Palantir 页面生成逐篇中文研读卡片。"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


CARD_STATUS_MARKER = "<!-- 研读状态："
CARD_URL_PATTERN = re.compile(r"<!-- 页面 URL：\s*(.*?)\s*-->")
CARD_STATUS_PATTERN = re.compile(r"<!-- 研读状态：\s*(.*?)\s*-->")
ENGLISH_WORD_PATTERN = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)*|\d+")


def _read_catalog(catalog_path: Path) -> list[dict[str, object]]:
    records = []
    for line_number, line in enumerate(
        Path(catalog_path).read_text(encoding="utf-8").splitlines(), start=1
    ):
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"目录 JSONL 第 {line_number} 行格式错误") from exc
        if not isinstance(record, dict) or not isinstance(record.get("url"), str):
            raise ValueError(f"目录 JSONL 第 {line_number} 行缺少页面 URL")
        records.append(record)
    return records


def card_filename(record: dict[str, object]) -> str:
    """根据规范 URL 生成稳定且不冲突的卡片文件名。"""
    url = str(record["url"])
    path_parts = [part for part in urlsplit(url).path.split("/") if part]
    slug = path_parts[-1] if path_parts else "foundry"
    safe_slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", slug).strip("-").lower()
    if not safe_slug:
        safe_slug = "article"
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
    return f"{safe_slug}-{digest}.md"


def _theme_directory(record: dict[str, object]) -> str:
    url = str(record["url"]).lower()
    if "mcp" in url:
        return "mcp"
    if any(term in url for term in ("agent", "/aip/", "assist")):
        return "agents"
    if "/api/" in url:
        return "api"
    if any(term in url for term in ("action", "function", "permission")):
        return "governance"
    return "ontology"


def _counterpart_for_record(
    record: dict[str, object], english_urls: set[str]
) -> tuple[str | None, str]:
    if record.get("language") == "en":
        counterpart = record.get("zh_counterpart_url")
        if isinstance(counterpart, str) and counterpart:
            return counterpart, str(record.get("zh_pair_status", "matched"))
        return None, str(record.get("zh_pair_status", "missing"))

    chinese_url = str(record["url"])
    english_url = chinese_url.replace("/docs/zh/foundry/", "/docs/foundry/", 1)
    if english_url in english_urls:
        return english_url, "matched"
    return None, "needs_review"


def build_card(
    record: dict[str, object],
    english_counterpart_url: str | None = None,
) -> str:
    """为单页生成可编辑的中文研读卡片初稿。"""
    url = str(record["url"])
    title = str(record.get("title") or url)
    language = str(record.get("language", "en"))
    is_english = language == "en"
    if is_english:
        zh_url = record.get("zh_counterpart_url")
        zh_status = str(record.get("zh_pair_status", "missing"))
        english_url = None
    else:
        zh_url = None
        zh_status = "not_applicable"
        english_url = english_counterpart_url

    if isinstance(zh_url, str) and zh_url:
        zh_source = f"[官方中文页面]({zh_url})（配对状态：{zh_status}）"
    else:
        zh_source = f"尚未确认（配对状态：{zh_status}）"
    if english_url:
        english_source = f"[英文原文]({english_url})"
    elif is_english:
        english_source = f"[英文原文]({url})"
    else:
        english_source = "尚未确认英文对应页面"

    excerpt_heading = (
        "## 英文原文短摘录（每个来源不超过 25 词）"
        if is_english
        else "## 原文短摘录与翻译"
    )
    excerpt_placeholder = (
        "> 【待研读：摘录并翻译短句】" if is_english else "> 【待研读：摘录中文原文】"
    )
    status = "未开始"
    checked_at = str(record.get("checked_at", "未记录"))
    lastmod = str(record.get("lastmod") or "未提供")
    relevance = str(record.get("relevance", "待分类"))
    relevance_reason = str(record.get("relevance_reason", "待复核"))
    return f"""<!-- 页面 URL：{url} -->
<!-- 研读状态：{status} -->

# {title}

- 英文来源：{english_source}
- 官方中文来源：{zh_source}
- 页面语言：{"英文" if is_english else "中文"}
- 主题栏目：{record.get("section", "未分类")}
- 相关性：{relevance}；{relevance_reason}
- 官方更新时间：{lastmod}
- 目录核对时间：{checked_at}
- 产品状态：待核对 Beta、预览、弃用或更名信息

{excerpt_heading}

{excerpt_placeholder}

## 摘录译文

【待填写】

## 中文要点

【用自己的话概括本页解决的问题、对象和关键操作。】

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 【待填写】 | 【待填写】 | 【待填写】 |

## 疑问与待验证项

- 【记录文档未说明之处、与其他页面的差异，以及需要验证的假设。】

## 复刻启示

- 【写出对本体管理系统的数据模型、治理流程、权限或 Agent 接入的具体启示。】
"""


def build_research_cards(
    catalog_path: Path,
    output_dir: Path,
) -> list[Path]:
    """为每个直接相关页面生成卡片；已有卡片不覆盖。"""
    records = _read_catalog(catalog_path)
    english_urls = {
        str(record["url"])
        for record in records
        if record.get("language") == "en"
    }
    created: list[Path] = []
    for record in records:
        if record.get("relevance") != "direct":
            continue
        theme_dir = _theme_directory(record)
        target = Path(output_dir) / theme_dir / card_filename(record)
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        english_counterpart_url, _ = _counterpart_for_record(record, english_urls)
        target.write_text(
            build_card(record, english_counterpart_url), encoding="utf-8", newline="\n"
        )
        created.append(target)
    return created


def english_excerpt_word_count(card_content: str) -> int:
    """统计英文原文短摘录中的英文词数。"""
    section_heading = "## 英文原文短摘录"
    if section_heading not in card_content:
        return 0
    excerpt_section = card_content.split(section_heading, 1)[1]
    excerpt_section = re.split(r"\n## ", excerpt_section, maxsplit=1)[0]
    quote_lines = [
        line[1:].strip()
        for line in excerpt_section.splitlines()
        if line.lstrip().startswith(">")
    ]
    quote = " ".join(quote_lines)
    return len(ENGLISH_WORD_PATTERN.findall(quote))


def validate_card_content(card_content: str) -> None:
    word_count = english_excerpt_word_count(card_content)
    if word_count > 25:
        raise ValueError(f"英文短摘录有 {word_count} 词，超过每个来源 25 词的限制")


def check_research_coverage(
    catalog_path: Path,
    cards_dir: Path,
) -> dict[str, object]:
    """核对直接相关目录项是否有已完成卡片并遵守短摘录上限。"""
    records = _read_catalog(catalog_path)
    direct_urls = {
        str(record["url"])
        for record in records
        if record.get("relevance") == "direct"
    }
    cards_by_url: dict[str, tuple[Path, str, str]] = {}
    for path in Path(cards_dir).rglob("*.md"):
        if path.name.startswith("_"):
            continue
        content = path.read_text(encoding="utf-8")
        url_match = CARD_URL_PATTERN.search(content)
        if url_match is None:
            continue
        status_match = CARD_STATUS_PATTERN.search(content)
        status = status_match.group(1).strip() if status_match else "未标记"
        cards_by_url[url_match.group(1).strip()] = (path, status, content)

    missing_urls = sorted(direct_urls - cards_by_url.keys())
    incomplete_urls = sorted(
        url
        for url in direct_urls & cards_by_url.keys()
        if cards_by_url[url][1] != "已完成"
    )
    over_limit_urls = []
    for url in sorted(direct_urls & cards_by_url.keys()):
        try:
            validate_card_content(cards_by_url[url][2])
        except ValueError:
            over_limit_urls.append(url)

    return {
        "direct_count": len(direct_urls),
        "card_count": len(direct_urls & cards_by_url.keys()),
        "missing_count": len(missing_urls),
        "incomplete_count": len(incomplete_urls),
        "over_limit_count": len(over_limit_urls),
        "missing_urls": missing_urls,
        "incomplete_urls": incomplete_urls,
        "over_limit_urls": over_limit_urls,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="生成 Palantir Ontology 与 Agent 研读卡片")
    parser.add_argument("--catalog", type=Path, default=Path("data/palantir_docs_catalog.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("docs/research/articles"))
    arguments = parser.parse_args()
    created = build_research_cards(arguments.catalog, arguments.output)
    print(f"已生成 {len(created)} 张卡片；已有卡片未覆盖。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
