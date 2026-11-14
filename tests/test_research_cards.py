import importlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


cards = importlib.import_module("scripts.build_research_cards")


class ResearchCardTests(unittest.TestCase):
    def sample_record(self, **updates):
        record = {
            "url": "https://www.palantir.com/docs/foundry/ontology/overview",
            "title": "Overview • Ontology • Palantir",
            "language": "en",
            "section": "ontology",
            "relevance": "direct",
            "relevance_reason": "本体模型与治理文档",
            "lastmod": "2026-11-10",
            "checked_at": "2026-11-14T12:00:00Z",
            "fetch_status": "ok",
            "zh_counterpart_url": "https://www.palantir.com/docs/zh/foundry/ontology/overview",
            "zh_pair_status": "matched",
        }
        record.update(updates)
        return record

    def test_card_filename_is_stable_for_doc_url(self):
        filename = cards.card_filename
        record = self.sample_record()

        first = filename(record)
        second = filename(record)

        self.assertEqual(first, second)

    def test_build_card_contains_source_metadata_and_required_sections(self):
        build_card = cards.build_card

        content = build_card(self.sample_record())

        self.assertIn("https://www.palantir.com/docs/foundry/ontology/overview", content)
        self.assertIn("https://www.palantir.com/docs/zh/foundry/ontology/overview", content)
        self.assertIn("## 中文要点", content)
        self.assertIn("## 术语对照", content)
        self.assertIn("## 疑问与待验证项", content)
        self.assertIn("## 复刻启示", content)

    def test_build_research_cards_skips_supplement_reference(self):
        build_cards = cards.build_research_cards
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            catalog = root / "catalog.jsonl"
            output = root / "articles"
            records = [
                self.sample_record(),
                self.sample_record(
                    url="https://www.palantir.com/docs/foundry/data-connection/agent-worker-runtime",
                    title="Agent worker runtime",
                    relevance="supplement",
                ),
            ]
            catalog.write_text(
                "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in records),
                encoding="utf-8",
            )

            generated = build_cards(catalog, output)

        self.assertEqual(len(generated), 1)

    def test_coverage_checker_reports_missing_direct_card(self):
        check_coverage = cards.check_research_coverage
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            catalog = root / "catalog.jsonl"
            cards_dir = root / "articles"
            catalog.write_text(
                json.dumps(self.sample_record(), ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            result = check_coverage(catalog, cards_dir)

        self.assertEqual(result["missing_count"], 1)

    def test_coverage_cli_runs_as_a_direct_script(self):
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            catalog = root / "catalog.jsonl"
            catalog.write_text(
                json.dumps(self.sample_record(), ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            checker_path = Path(__file__).parents[1] / "scripts" / "check_research_coverage.py"

            result = subprocess.run(
                [
                    sys.executable,
                    str(checker_path),
                    "--catalog",
                    str(catalog),
                    "--cards",
                    str(root / "articles"),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("直接相关 1 页", result.stdout)

    def test_card_validation_rejects_more_than_25_english_words(self):
        validate = cards.validate_card_content
        content = (
            "## 英文原文短摘录（每篇最多 25 词）\n"
            "> " + " ".join(f"word{index}" for index in range(26)) + "\n"
        )

        with self.assertRaises(ValueError):
            validate(content)


if __name__ == "__main__":
    unittest.main()
