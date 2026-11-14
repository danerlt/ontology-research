"""检查直接相关页面的研读卡片覆盖与摘录长度。"""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from scripts.build_research_cards import check_research_coverage
except ModuleNotFoundError:
    from build_research_cards import check_research_coverage


def main() -> int:
    parser = argparse.ArgumentParser(description="检查研读卡片覆盖情况")
    parser.add_argument("--catalog", type=Path, default=Path("data/palantir_docs_catalog.jsonl"))
    parser.add_argument("--cards", type=Path, default=Path("docs/research/articles"))
    arguments = parser.parse_args()

    result = check_research_coverage(arguments.catalog, arguments.cards)
    print(
        "直接相关 {direct_count} 页，已有卡片 {card_count} 张，缺卡 {missing_count}，"
        "未完成 {incomplete_count}，超出摘录限制 {over_limit_count}。".format(**result)
    )
    return int(
        bool(
            result["missing_count"]
            or result["incomplete_count"]
            or result["over_limit_count"]
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
