from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING

from hetman_kit_localize import Localize
from pipeline.handlers.condition_handler.resources.types import \
    ConditionErrorTemplate

from pipeline_plugin_i18n.resources.exceptions import \
    PipelinePluginI18nException
from pipeline_plugin_i18n.resources.types import Translation, Translations

if TYPE_CHECKING:
    from pipeline.handlers.condition_handler.condition_handler import \
        ConditionHandler
    from pipeline.handlers.match_handler.match_handler import MatchHandler


class PipelinePluginI18n(Localize):
    """
    A plugin for the `pipeline` library that adds internationalization (i18n) support.

    This class manages the current locale context and provides a mechanism to register
    localized error messages (translations) for pipeline handlers. It uses `contextvars`
    to handle locale state safely across asynchronous contexts.
    """
    @classmethod
    def register_handler(
        cls, handler: type[ConditionHandler | MatchHandler],
        translations: Translations
    ):
        """
        Registers localized error templates for a specific `ConditionHandler` or `MatchHandler`.

        This method injects a logic into the handler to dynamically select the error
        template based on the current locale. If a translation for the current locale
        is not found, it falls back to the base locale.

        Args:
            handler (type[ConditionHandler | MatchHandler]): The handler class to register translations for.
            translations (Translations): A dictionary mapping `HandlerMode`s to a dictionary
                of locales and their corresponding error templates.

        Raises:
            PipelinePluginI18nException: If a translation for the base locale is missing
                for any of the provided modes.
        """
        def process_translation(
            self: ConditionHandler | MatchHandler, translation: Translation
        ):
            error_template: ConditionErrorTemplate = cls.resolve_translation(
                data=translation
            )

            return error_template(self)

        base_locale: str = cls.get_base_locale()

        for mode, translation in translations.items():
            if base_locale not in translation:
                raise PipelinePluginI18nException(
                    f'Handler "{handler.__name__}" is missing the "{base_locale}" base locale translation for "{mode.value}" mode.'
                )

            handler.ERROR_TEMPLATES[mode] = partial(
                process_translation, translation=translation
            )
