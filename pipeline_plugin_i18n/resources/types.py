from __future__ import annotations

from pipeline import HandlerMode
from pipeline.handlers.condition.resources.types import ConditionErrorTemplate

Translation = dict[str, ConditionErrorTemplate]
Translations = dict[HandlerMode, Translation]
