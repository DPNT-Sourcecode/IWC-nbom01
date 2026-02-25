"""Typed helpers shared across queue implementations."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class TaskSubmission:
    """Typed payload accepted by ``Queue.enqueue``."""

    provider: str
    user_id: int
    timestamp: datetime | str
    metadata: dict[str, object] = field(default_factory=dict)

    def core_task_values(self) -> tuple[str, int]:
        return (self.provider, self.user_id)
    
    def __str__(self):
        return f"{self.provider}_{self.user_id}_{self.timestamp}"

@dataclass
class TaskDispatch:
    """Typed payload returned by ``Queue.dequeue``."""

    provider: str
    user_id: int


__all__ = ["TaskSubmission", "TaskDispatch"]

