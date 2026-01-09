from __future__ import annotations

from typing import Literal

from pipeline.handlers.base_handler.resources.constants import HandlerMode
from pipeline.handlers.condition_handler.resources.types import \
    ConditionErrorTemplate

Locale = Literal["en", "pl"]

Translation = dict[Locale, ConditionErrorTemplate]
Translations = dict[HandlerMode, Translation]
