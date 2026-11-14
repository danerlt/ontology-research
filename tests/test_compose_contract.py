import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ComposeContractTests(unittest.TestCase):
    def test_compose_declares_all_application_and_state_services(self) -> None:
        result = subprocess.run(
            ["docker", "compose", "config", "--services"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )

        self.assertEqual(
            set(result.stdout.splitlines()),
            {"web", "ontology-api", "agent-service", "postgres", "redis"},
        )

    def test_compose_has_health_checks_and_persistent_state_volumes(self) -> None:
        result = subprocess.run(
            ["docker", "compose", "config", "--format", "json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        import json

        config = json.loads(result.stdout)
        for service_name in ("web", "ontology-api", "agent-service", "postgres", "redis"):
            self.assertIn("healthcheck", config["services"][service_name])
        self.assertIn("postgres-data", config["volumes"])
        self.assertIn("redis-data", config["volumes"])

    def test_env_example_has_local_defaults_and_actual_env_is_ignored(self) -> None:
        example = (ROOT / ".env.example").read_text(encoding="utf-8")
        self.assertIn("DATABASE_URL=", example)
        self.assertIn("REDIS_URL=", example)
        self.assertIn("JWT_SECRET=", example)
        ignored = subprocess.run(
            ["git", "check-ignore", ".env"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(ignored.returncode, 0)

    def test_compose_default_admin_email_passes_email_validation(self) -> None:
        compose = (ROOT / "docker-compose.yml").read_text(encoding="utf-8")

        self.assertIn("ADMIN_EMAIL:-admin@example.com", compose)


if __name__ == "__main__":
    unittest.main()
