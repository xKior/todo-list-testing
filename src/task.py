"""Modelos y validaciones de Task.
Aplicando principios SOLID: Single Responsibility (modelo y validación aquí), Open/Closed (enums extendibles), Liskov y otros.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Status(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()


class ValidationError(ValueError):
    pass


@dataclass(frozen=True)
class Task:
    id: int
    title: str = field(compare=False)
    priority: Priority = field(default=Priority.MEDIUM, compare=False)
    status: Status = field(default=Status.TODO, compare=False)
    description: Optional[str] = field(default=None, compare=False)

    def __post_init__(self):
        if not isinstance(self.id, int) or self.id < 0:
            raise ValidationError("id must be a non-negative integer")
        if not self.title or not isinstance(self.title, str):
            raise ValidationError("title must be a non-empty string")
        if len(self.title) > 200:
            raise ValidationError("title must be at most 200 characters")
        if self.description is not None and len(self.description) > 1000:
            raise ValidationError("description too long")
        if not isinstance(self.priority, Priority):
            raise ValidationError("invalid priority")
        if not isinstance(self.status, Status):
            raise ValidationError("invalid status")

    def with_status(self, new_status: Status) -> Task:
        """Devuelve una nueva Task con status actualizado (inmutabilidad)."""
        return Task(
            id=self.id,
            title=self.title,
            priority=self.priority,
            status=new_status,
            description=self.description,
        )

    def with_title(self, new_title: str) -> Task:
        return Task(
            id=self.id,
            title=new_title,
            priority=self.priority,
            status=self.status,
            description=self.description,
        )