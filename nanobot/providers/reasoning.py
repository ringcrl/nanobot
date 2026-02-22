"""Reasoning effort helpers shared by providers and config."""

from __future__ import annotations

from typing import Literal, cast

ReasoningEffort = Literal["none", "low", "medium", "high", "xhigh"]

_ALL_EFFORTS = frozenset({"none", "low", "medium", "high", "xhigh"})
_OPENAI_CHAT_EFFORTS = frozenset({"low", "medium", "high"})


def normalize_reasoning_effort(reasoning_effort: str | None) -> ReasoningEffort | None:
    """Normalize config/user input to canonical lowercase values."""
    if reasoning_effort is None:
        return None
    normalized = reasoning_effort.strip().lower()
    if not normalized:
        return None
    if normalized not in _ALL_EFFORTS:
        return None
    return cast(ReasoningEffort, normalized)


def openai_chat_reasoning_effort(reasoning_effort: str | None) -> Literal["low", "medium", "high"] | None:
    """Return a Chat Completions-compatible effort value."""
    normalized = normalize_reasoning_effort(reasoning_effort)
    if normalized in _OPENAI_CHAT_EFFORTS:
        return cast(Literal["low", "medium", "high"], normalized)
    return None
