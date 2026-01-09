from __future__ import annotations

from contextvars import ContextVar
from functools import partial
from typing import TYPE_CHECKING

from pipeline.handlers.condition_handler.resources.types import \
    ConditionErrorTemplate

from pipeline_plugin_i18n.resources.exceptions import \
    PipelinePluginI18nException
from pipeline_plugin_i18n.resources.types import Translation, Translations

if TYPE_CHECKING:
    from pipeline.handlers.condition_handler.condition_handler import \
        ConditionHandler

    from pipeline.handlers.match_handler.match_handler import \
        MatchHandler

    from pipeline_plugin_i18n.resources.types import Locale


class PipelinePluginI18n:
    """
    A plugin for the `pipeline` library that adds internationalization (i18n) support.

    This class manages the current locale context and provides a mechanism to register
    localized error messages (translations) for pipeline handlers. It uses `contextvars`
    to handle locale state safely across asynchronous contexts.

    Attributes:
        BASE_LOCALE (Locale): The default locale used as a fallback when a specific
            translation is missing or no locale is set. Defaults to "en".
        CURRENT_LOCALE (ContextVar[Locale]): A context variable holding the current
            active locale. Defaults to `BASE_LOCALE` if not set.
    """
    BASE_LOCALE: Locale = "en"

    CURRENT_LOCALE: ContextVar[Locale] = ContextVar(
        "pipeline_plugin_i18n.locale"
    )

    @classmethod
    def register_handler(
        cls, handler: type[ConditionHandler | MatchHandler],
        translations: Translations
    ):
        """
        Registers localized error templates for a specific `ConditionHandler` or `MatchHandler`.

        This method injects a logic into the handler to dynamically select the error
        template based on the current locale. If a translation for the current locale
        is not found, it falls back to the `BASE_LOCALE`.

        Args:
            handler (type[ConditionHandler | MatchHandler]): The handler class to register translations for.
            translations (Translations): A dictionary mapping `HandlerMode`s to a dictionary
                of locales and their corresponding error templates.

        Raises:
            PipelinePluginI18nException: If a translation for `BASE_LOCALE` is missing
                for any of the provided modes.
        """
        def process_translation(
            self: ConditionHandler | MatchHandler, translation: Translation
        ):
            locale: Locale = cls.get_locale()

            # NOTE: If there is no translation for the base locale, it should be detected before this function is executed.
            error_template: ConditionErrorTemplate | None = translation.get(
                locale, translation[cls.BASE_LOCALE]
            )

            return error_template(self)

        for mode, translation in translations.items():
            if cls.BASE_LOCALE not in translation:
                raise PipelinePluginI18nException(
                    f'Handler "{handler.__name__}" is missing the "{cls.BASE_LOCALE}" base locale translation for "{mode.value}" mode.'
                )

            handler.ERROR_TEMPLATES[mode] = partial(
                process_translation, translation=translation
            )

    @classmethod
    def get_locale(cls) -> Locale:
        """
        Retrieves the current active locale.

        Returns:
            Locale: The current locale code (e.g., "en", "pl"). Returns `BASE_LOCALE`
            if no locale has been explicitly set in the current context.
        """
        return cls.CURRENT_LOCALE.get(cls.BASE_LOCALE)

    @classmethod
    def set_locale(cls, locale: Locale) -> None:
        """
        Sets the active locale for the current context.

        Args:
            locale (Locale): The locale code to set (e.g., "en", "pl").
        """
        cls.CURRENT_LOCALE.set(locale)
