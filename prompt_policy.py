from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class PromptDecision:
    allowed: bool
    message: str
    reason: str | None = None


_EXPLOSIVE_TERMS = (
    "grenade",
    "grenades",
    "bomb",
    "bombs",
    "explosive",
    "explosives",
    "landmine",
    "landmines",
    "dynamite",
    "molotov",
    "molotov cocktail",
)

_EXPLOSIVE_PATTERN = re.compile(
    r"\b(?:%s)\b" % "|".join(re.escape(term) for term in _EXPLOSIVE_TERMS),
    re.IGNORECASE,
)


def evaluate_image_prompt(prompt: str) -> PromptDecision:
    normalized_prompt = " ".join(prompt.split())
    if _EXPLOSIVE_PATTERN.search(normalized_prompt):
        return PromptDecision(
            allowed=False,
            reason="explosive_weapon",
            message=(
                "I can’t help create or edit a realistic image that includes an "
                "explosive weapon such as a hand grenade. If you want, I can help "
                "with a tennis image that keeps the ball or replaces it with a safe "
                "sports-themed object."
            ),
        )

    return PromptDecision(
        allowed=True,
        reason=None,
        message=normalized_prompt,
    )
