from __future__ import annotations

from pipeline.handlers.base_handler.resources.constants import HandlerMode
from pipeline.handlers.condition_handler.resources.types import \
    ConditionErrorTemplate

Translation = dict[str, ConditionErrorTemplate]
Translations = dict[HandlerMode, Translation]
