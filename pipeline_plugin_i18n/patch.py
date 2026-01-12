from pipeline.handlers import Condition, Match
from pipeline.handlers.base_handler.resources.constants import HandlerMode

from pipeline_plugin_i18n.plugin import PipelinePluginI18n


def initialize_pipeline_plugin_i18n():
    """
    Initializes the `pipeline_plugin_i18n` by registering default translations.

    This function currently registers English and Polish translations for
    standard `Condition` and `Match` handlers.
    """
    # --- Condition Handlers ---

    PipelinePluginI18n.register_handler(
        handler=Condition.ValueType,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.ValueType.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Nieprawidłowy typ. Oczekiwano {self.argument.__name__}.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.MinLength,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.MinLength.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Za krótkie. Minimalna długość to {self.argument} znaków."
                        if isinstance(self.value, str) else
                        f"Za mało elementów. Minimalna liczba to {self.argument}.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.MaxLength,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.MaxLength.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Za długie. Maksymalna długość to {self.argument} znaków."
                        if isinstance(self.value, str) else
                        f"Za dużo elementów. Maksymalna liczba to {self.argument}.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.ExactLength,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.ExactLength.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Nieprawidłowa długość. Wymagana długość to dokładnie {self.argument} znaków."
                        if isinstance(self.value, str) else
                        f"Nieprawidłowa liczba elementów. Wymagana liczba to dokładnie {self.argument}."
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.MinNumber,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.MinNumber.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Wartość musi wynosić co najmniej {self.argument}.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.MaxNumber,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.MaxNumber.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Wartość musi wynosić co najwyżej {self.argument}.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.IncludedIn,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.IncludedIn.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Wybrana opcja jest nieprawidłowa. Wybierz spośród: {list(self.argument)}.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.NotIncludedIn,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.NotIncludedIn.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _: "Ta wartość jest niedozwolona.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.Equal,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Condition.Equal.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Wartość nie zgadza się z oczekiwaną wartością.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.NotEqual,
        translations={
            HandlerMode.ROOT:
                {
                    "en": Condition.NotEqual.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl": lambda _: "Wartość musi być inna.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.MatchesField,
        translations={
            HandlerMode.CONTEXT:
                {
                    "en":
                        Condition.MatchesField.ERROR_TEMPLATES[
                            HandlerMode.CONTEXT],
                    "pl":
                        lambda self:
                        f'Musi pasować do pola "{self.input_argument}".',
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Condition.DoesNotMatchField,
        translations={
            HandlerMode.CONTEXT:
                {
                    "en":
                        Condition.DoesNotMatchField.ERROR_TEMPLATES[
                            HandlerMode.CONTEXT],
                    "pl":
                        lambda self:
                        f'Musi różnić się od pola "{self.input_argument}".',
                }
        },
    )

    # --- Match Handlers: Text ---

    PipelinePluginI18n.register_handler(
        handler=Match.Text.Lowercase,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.Lowercase.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko małe litery (a-z) (np. jan).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.LowercaseWithSpaces,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.LowercaseWithSpaces.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko małe litery i spacje (np. jan kowalski).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.Uppercase,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.Uppercase.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko wielkie litery (A-Z) (np. JAN).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.UppercaseWithSpaces,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.UppercaseWithSpaces.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko wielkie litery i spacje (np. JAN KOWALSKI).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.Letters,
        translations={
            HandlerMode.ROOT:
                {
                    "en": Match.Text.Letters.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl": lambda _: "Musi zawierać tylko litery (np. Jablko).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.LettersWithSpaces,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.LettersWithSpaces.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko litery i spacje (np. Jan Kowalski).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.Digits,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.Digits.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko cyfry (0-9) (np. 123456).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.DigitsWithSpaces,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.DigitsWithSpaces.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko cyfry i spacje (np. 82 23 12).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.Alphanumeric,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.Alphanumeric.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko litery i cyfry (np. Jan123).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.AlphanumericWithSpaces,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.AlphanumericWithSpaces.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko litery, cyfry i spacje (np. Jan Kowalski 123).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.Printable,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.Printable.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Zawiera nieprawidłowe znaki. Dozwolone są tylko drukowalne znaki ASCII.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.NoWhitespace,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.NoWhitespace.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Nie może zawierać spacji, tabulatorów ani znaków nowej linii (np. jankowalski).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Text.Slug,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Text.Slug.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi zawierać tylko małe litery, cyfry i łączniki (np. moj-slug-1).",
                }
        },
    )

    # --- Match Handlers: Network ---

    PipelinePluginI18n.register_handler(
        handler=Match.Network.IPv4,
        translations={
            HandlerMode.ROOT:
                {
                    "en": Match.Network.IPv4.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl": lambda _: "Nieprawidłowy adres IPv4.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Network.IPv6,
        translations={
            HandlerMode.ROOT:
                {
                    "en": Match.Network.IPv6.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl": lambda _: "Nieprawidłowy adres IPv6.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Network.MACAddress,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Network.MACAddress.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _: "Nieprawidłowy format adresu MAC.",
                }
        },
    )

    # --- Match Handlers: Regex ---

    PipelinePluginI18n.register_handler(
        handler=Match.Regex.Search,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Regex.Search.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Nieprawidłowa wartość. Wymagany wzorzec to {self.argument}.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Regex.FullMatch,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Regex.FullMatch.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self:
                        f"Nieprawidłowa wartość. Wymagany wzorzec to {self.argument}.",
                }
        },
    )

    # --- Match Handlers: Encoding ---

    PipelinePluginI18n.register_handler(
        handler=Match.Encoding.Base64,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Encoding.Base64.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _: "Nieprawidłowe kodowanie Base64.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Encoding.JSON,
        translations={
            HandlerMode.ROOT:
                {
                    "en": Match.Encoding.JSON.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl": lambda _: "Ciąg znaków nie jest prawidłowym JSON-em.",
                }
        },
    )

    # --- Match Handlers: Format ---

    PipelinePluginI18n.register_handler(
        handler=Match.Format.Email,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Format.Email.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Nieprawidłowy format adresu e-mail (np. user@example.com).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Format.UUID,
        translations={
            HandlerMode.ROOT:
                {
                    "en": Match.Format.UUID.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl": lambda _: "Nieprawidłowy format UUID.",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Format.HexColor,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Format.HexColor.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi być prawidłowym kodem koloru hex (np. #ff0000).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Format.E164Phone,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Format.E164Phone.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Nieprawidłowy format numeru telefonu. Wymagany format międzynarodowy (np. +48123456789).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Format.Password,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Format.Password.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda self: {
                            Match.Format.Password.RELAXED:
                                "Hasło jest za słabe. Wymagane: 6-64 znaki, co najmniej 1 wielka i 1 mała litera.",
                            Match.Format.Password.NORMAL:
                                "Hasło jest za słabe. Wymagane: 6-64 znaki, co najmniej 1 wielka litera, 1 mała litera i 1 cyfra.",
                            Match.Format.Password.STRICT:
                                "Hasło jest za słabe. Wymagane: 6-64 znaki, co najmniej 1 wielka litera, 1 mała litera, 1 cyfra i 1 znak specjalny.",
                        }[self.argument],
                }
        },
    )

    # --- Match Handlers: Localization ---

    PipelinePluginI18n.register_handler(
        handler=Match.Localization.Country,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Localization.Country.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi być prawidłowym 2-literowym kodem kraju ISO (np. PL).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Localization.Currency,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Localization.Currency.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi być prawidłowym 3-literowym kodem waluty (np. PLN).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Localization.Language,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Localization.Language.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Musi być prawidłowym 2-literowym kodem języka (np. pl).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Localization.Timezone,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Localization.Timezone.ERROR_TEMPLATES[
                            HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Nieprawidłowa strefa czasowa IANA (np. Europe/Warsaw).",
                }
        },
    )

    # --- Match Handlers: Time ---

    PipelinePluginI18n.register_handler(
        handler=Match.Time.Date,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Time.Date.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Data musi być w formacie RRRR-MM-DD (np. 2023-01-01).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Time.Time,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Time.Time.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Nieprawidłowy format czasu (HH:MM[:SS]) (np. 12:00:00).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Time.DateTime,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Time.DateTime.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Nieprawidłowy format daty i czasu ISO 8601 (np. 2023-01-01T12:00:00Z).",
                }
        },
    )

    # --- Match Handlers: Web ---

    PipelinePluginI18n.register_handler(
        handler=Match.Web.Domain,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Web.Domain.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Nieprawidłowy format domeny (np. example.com).",
                }
        },
    )

    PipelinePluginI18n.register_handler(
        handler=Match.Web.URL,
        translations={
            HandlerMode.ROOT:
                {
                    "en":
                        Match.Web.URL.ERROR_TEMPLATES[HandlerMode.ROOT],
                    "pl":
                        lambda _:
                        "Nieprawidłowy format URL. Musi to być prawidłowy adres HTTP/HTTPS (np. https://example.com).",
                }
        },
    )
