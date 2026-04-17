"""
Prompt configuration for PageIndex.
Allows airia-backend to inject Czech/custom prompts from DB instead of hardcoded English defaults.

Usage:
    from pageindex.prompt_config import prompt_config
    prompt_config.set_overrides({'generate_node_summary': '...český prompt...'})
    # ... run PageIndex ...
    prompt_config.clear()

Dostupné klíče:
    'generate_node_summary', 'generate_doc_description',
    'toc_detector_single_page', 'generate_toc_init', 'generate_toc_continue'
"""


class PromptConfig:
    def __init__(self):
        self._overrides: dict[str, str] = {}

    def set_overrides(self, overrides: dict[str, str]) -> None:
        self._overrides.update(overrides)

    def get(self, key: str, default: str) -> str:
        return self._overrides.get(key, default)

    def clear(self) -> None:
        self._overrides.clear()

    def has(self, key: str) -> bool:
        return key in self._overrides


prompt_config = PromptConfig()
