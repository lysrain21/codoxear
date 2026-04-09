import unittest
from pathlib import Path


APP_JS = Path(__file__).resolve().parents[1] / "codoxear" / "static" / "app.js"


class TestPiDuplicateSource(unittest.TestCase):
    def test_pi_provider_choice_to_settings_does_not_fallback_to_chatgpt(self) -> None:
        source = APP_JS.read_text(encoding="utf-8")
        self.assertIn('if (backend === "pi") return { model_provider: rawValue || null, preferred_auth_method: null };', source)

    def test_pi_session_provider_choice_prefers_model_provider(self) -> None:
        source = APP_JS.read_text(encoding="utf-8")
        self.assertIn('if (backend === "pi") {', source)
        self.assertIn('return provider || explicit || fallback;', source)
        self.assertIn('defaultsForAgentBackend("pi").provider_choice', source)


if __name__ == "__main__":
    unittest.main()
