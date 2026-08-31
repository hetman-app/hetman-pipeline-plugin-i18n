<img src="https://krywok.com/svg/logo/full-mix-white-alpha.svg" alt="Krywok Logo" width="190" height="55" />

---

**Krywok Pipeline Plugin I18n** is a plugin for [Krywok Pipeline](https://pipeline.krywok.com) that provides internationalization (i18n) support.

## Features

- Comprehensive translations for all standard `Condition` and `Match` handlers.
- Simple initialization to register all translations globally.

## Installation

```bash
pip install "krywok-pipeline[i18n]"
```

## Quick Start

Initialize the plugin at the start of your application to register the translations.

You must call `set_base_locale` before running the first handler to ensure the system correctly maps the initial translation state.

```python
from pipeline_plugin_i18n import initialize_pipeline_plugin_i18n

# Register translations for standard handlers
initialize_pipeline_plugin_i18n()

# Set the base locale
PipelinePluginI18n.set_base_locale("en")
```

## Context Management

The plugin uses `contextvars` to manage the locale state, making it thread-safe and safe for asynchronous applications (e.g., **FastAPI**, **Falcon**, **Flask**).

### Setting the Locale

You can set the locale for the current context (e.g., per request).

```python
from pipeline_plugin_i18n import PipelinePluginI18n

# Set to Polish
PipelinePluginI18n.set_locale("pl")
```

### Getting the Locale

```python
from pipeline_plugin_i18n import PipelinePluginI18n

current_locale = PipelinePluginI18n.get_locale()
print(current_locale)  # Output: "pl"
```

## Custom Translations

You can register your own translations for any `Condition` or `Match` handler.

```python
from pipeline import HandlerMode, Match, Pipeline

from pipeline_plugin_i18n import PipelinePluginI18n

PipelinePluginI18n.register_handler(
    handler=Match.Text.Letters,
    translations={
        HandlerMode.ROOT:
            {
                "en": Match.Text.Letters.ERROR_TEMPLATES[HandlerMode.ROOT],
                "pl": lambda self: "Musi zawierać tylko litery (np. Aaaaa)."
            }
    },
)
```

## Supported Languages

- English (`en`)
- Polish (`pl`)
