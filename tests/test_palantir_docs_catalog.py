import importlib
import gzip
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


try:
    crawler = importlib.import_module("scripts.crawl_palantir_docs")
except ModuleNotFoundError:
    crawler = None


class PalantirDocsCatalogTests(unittest.TestCase):
    def require_function(self, name):
        self.assertIsNotNone(crawler, "抓取器模块尚未实现")
        function = getattr(crawler, name, None)
        self.assertTrue(callable(function), f"{name} 尚未实现")
        return function

    def test_robots_policy_denies_disallowed_path(self):
        is_allowed_by_robots = self.require_function("is_allowed_by_robots")
        robots = "User-agent: *\nDisallow: /private/\nAllow: /docs/\n"

        allowed = is_allowed_by_robots(
            robots,
            "https://www.palantir.com/private/page",
            "ontology-research-bot",
        )

        self.assertFalse(allowed)

    def test_parse_sitemap_extracts_lastmod_and_deduplicates_urls(self):
        parse_sitemap = self.require_function("parse_sitemap")
        sitemap = """<?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
          <url>
            <loc>https://www.palantir.com/docs/foundry/ontology/overview?trk=nav</loc>
            <lastmod>2026-11-10</lastmod>
          </url>
          <url>
            <loc>https://palantir.com/docs/foundry/ontology/overview</loc>
            <lastmod>2026-11-12</lastmod>
          </url>
        </urlset>"""

        pages = parse_sitemap(sitemap)

        self.assertEqual(len(pages), 1)
        self.assertEqual(
            pages[0]["url"],
            "https://www.palantir.com/docs/foundry/ontology/overview",
        )
        self.assertEqual(pages[0]["lastmod"], "2026-11-12")

    def test_parse_sitemap_rejects_malformed_xml(self):
        parse_sitemap = self.require_function("parse_sitemap")

        with self.assertRaises(ValueError):
            parse_sitemap("<urlset><url><loc>")

    def test_parse_doc_page_extracts_metadata_without_body(self):
        parse_doc_page = self.require_function("parse_doc_page")
        html = """<!doctype html>
        <html><head>
          <title>Ontology overview • Palantir</title>
          <link rel="canonical" href="https://www.palantir.com/docs/foundry/ontology/overview">
          <meta name="description" content="Official overview of Ontology resources.">
        </head><body>
          <nav class="ptcom-design__sideBar__test"><a href="/docs/foundry/ontology/object-types">Object types</a>
            <a href="https://outside.example/page">外部链接</a></nav>
          <main><p>这段文章正文不得进入目录元数据。</p></main>
        </body></html>"""

        metadata = parse_doc_page(
            html,
            "https://www.palantir.com/docs/foundry/ontology/overview",
        )

        self.assertEqual(metadata["title"], "Ontology overview • Palantir")
        self.assertEqual(
            metadata["canonical_url"],
            "https://www.palantir.com/docs/foundry/ontology/overview",
        )
        self.assertEqual(
            metadata["description"],
            "Official overview of Ontology resources.",
        )
        self.assertEqual(
            metadata["navigation_links"],
            ["https://www.palantir.com/docs/foundry/ontology/object-types"],
        )
        self.assertNotIn("这段文章正文不得进入目录元数据", str(metadata))

    def test_parse_doc_page_ignores_svg_accessibility_titles(self):
        parse_doc_page = self.require_function("parse_doc_page")
        html = """<html><head><title>核心文档标题</title></head>
        <body><svg><title>Search</title></svg>
          <svg><title>Hide sidebar</title></svg></body></html>"""

        metadata = parse_doc_page(
            html,
            "https://www.palantir.com/docs/foundry/ontology/overview",
        )

        self.assertEqual(metadata["title"], "核心文档标题")

    def test_parse_doc_page_reports_missing_title_and_canonical_url(self):
        parse_doc_page = self.require_function("parse_doc_page")

        metadata = parse_doc_page(
            "<html><head><meta name='description' content='无标题页'></head></html>",
            "https://www.palantir.com/docs/foundry/ontology/missing",
        )

        self.assertEqual(
            metadata["missing_fields"],
            ["title", "canonical_url"],
        )
        self.assertEqual(
            metadata["page_url"],
            "https://www.palantir.com/docs/foundry/ontology/missing",
        )

    def test_normalize_doc_url_removes_tracking_and_fragment(self):
        normalize_doc_url = self.require_function("normalize_doc_url")

        normalized = normalize_doc_url(
            "http://palantir.com/docs/foundry/ontology/overview/?trk=nav#contents"
        )

        self.assertEqual(
            normalized,
            "https://www.palantir.com/docs/foundry/ontology/overview",
        )

    def test_normalize_doc_url_rejects_external_and_non_foundry_urls(self):
        normalize_doc_url = self.require_function("normalize_doc_url")

        self.assertIsNone(normalize_doc_url("https://outside.example/docs/foundry/ontology"))
        self.assertIsNone(normalize_doc_url("https://www.palantir.com/docs/gotham/overview"))
        self.assertEqual(
            normalize_doc_url("https://palantir.com/docs/zh/foundry/ontology/overview"),
            "https://www.palantir.com/docs/zh/foundry/ontology/overview",
        )

    def test_merge_candidates_deduplicates_and_tracks_sources(self):
        merge_candidates = self.require_function("merge_candidates")
        candidates = [
            {
                "url": "https://www.palantir.com/docs/foundry/ontology/overview?trk=nav",
                "lastmod": "2026-11-10",
                "discovered_from": ["sitemap"],
            },
            {
                "url": "https://palantir.com/docs/foundry/ontology/overview",
                "title": "Ontology overview",
                "lastmod": "2026-11-12",
                "discovered_from": ["navigation"],
            },
        ]

        merged = merge_candidates(candidates)

        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["title"], "Ontology overview")
        self.assertEqual(merged[0]["lastmod"], "2026-11-12")
        self.assertEqual(merged[0]["discovered_from"], ["navigation", "sitemap"])

    def test_crawl_catalog_writes_metadata_only_jsonl(self):
        crawl_catalog = self.require_function("crawl_catalog")
        seed_url = "https://www.palantir.com/docs/foundry/ontology/overview"
        robots = "User-agent: *\nAllow: /\n"
        sitemap = f"""<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
          <url><loc>{seed_url}</loc><lastmod>2026-11-12</lastmod></url>
        </urlset>"""
        body_marker = "全文正文不得写入编目文件"
        page_html = f"""<html><head>
          <title>Ontology overview</title>
          <link rel="canonical" href="{seed_url}">
          <meta name="description" content="Ontology overview page.">
        </head><body><nav class="sideBar"><a href="{seed_url}/objects">对象类型</a></nav>
        <main>{body_marker}</main></body></html>"""

        def fake_fetch(url):
            if url == "https://www.palantir.com/robots.txt":
                return robots
            if url == "https://www.palantir.com/docs/sitemap.xml":
                return sitemap
            if url == seed_url:
                return page_html
            raise AssertionError(f"请求了未预期的 URL：{url}")

        with TemporaryDirectory() as temporary_directory:
            output_path = Path(temporary_directory) / "catalog.jsonl"
            with patch.object(crawler, "fetch_text", side_effect=fake_fetch, create=True):
                with patch.object(crawler.time, "sleep"):
                    stats = crawl_catalog([seed_url], output_path, max_pages=1)

            catalog_text = output_path.read_text(encoding="utf-8")
            records = [json.loads(line) for line in catalog_text.splitlines()]

        self.assertEqual(stats["fetched"], 1)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["title"], "Ontology overview")
        self.assertEqual(records[0]["fetch_status"], "ok")
        self.assertNotIn(body_marker, catalog_text)

    def test_crawl_catalog_records_page_fetch_errors(self):
        crawl_catalog = self.require_function("crawl_catalog")
        seed_url = "https://www.palantir.com/docs/foundry/ontology/overview"
        robots = "User-agent: *\nAllow: /\n"
        sitemap = f"""<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
          <url><loc>{seed_url}</loc></url>
        </urlset>"""

        def fake_fetch(url):
            if url == "https://www.palantir.com/robots.txt":
                return robots
            if url == "https://www.palantir.com/docs/sitemap.xml":
                return sitemap
            raise OSError("模拟网络中断")

        with TemporaryDirectory() as temporary_directory:
            output_path = Path(temporary_directory) / "catalog.jsonl"
            with patch.object(crawler, "fetch_text", side_effect=fake_fetch, create=True):
                with patch.object(crawler.time, "sleep"):
                    stats = crawl_catalog([seed_url], output_path, max_pages=1)

            records = [json.loads(line) for line in output_path.read_text(encoding="utf-8").splitlines()]

        self.assertEqual(stats["failed"], 1)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["url"], seed_url)
        self.assertEqual(records[0]["fetch_status"], "error")
        self.assertIn("模拟网络中断", records[0]["error"])

    def test_fetch_text_decompresses_gzip_response(self):
        fetch_text = self.require_function("fetch_text")
        expected_text = "Palantir 文档内容"

        class FakeHeaders:
            def get_content_charset(self):
                return "utf-8"

            def get(self, name, default=None):
                if name.lower() == "content-encoding":
                    return "gzip"
                return default

        class FakeResponse:
            headers = FakeHeaders()

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return None

            def read(self):
                return gzip.compress(expected_text.encode("utf-8"))

        with patch.object(crawler, "urlopen", return_value=FakeResponse()) as mocked_urlopen:
            try:
                result = fetch_text("https://www.palantir.com/docs/foundry/ontology/overview")
            except Exception as exc:
                self.fail(f"gzip 响应应能正常解压，当前抛出 {type(exc).__name__}")

        request = mocked_urlopen.call_args.args[0]
        self.assertEqual(request.get_header("Accept-encoding"), "gzip")
        self.assertEqual(result, expected_text)


if __name__ == "__main__":
    unittest.main()
