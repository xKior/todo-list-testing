
"""Gestor de tareas. Separación de responsabilidades: manager no conoce detalles de persistencia.
Se aplica Dependency Inversion: TaskRepository abstraído para permitir pruebas e integración.
"""
from __future__ import annotations
from typing import List, Protocol, Optional
from .task import Task, Status


class TaskRepository(Protocol):
    def add(self, task: Task) -> None:
        ...

    def update(self, task: Task) -> None:
        ...

    def get(self, task_id: int) -> Optional[Task]:
        ...

    def list_all(self) -> List[Task]:
        ...


class InMemoryTaskRepository:
    def __init__(self):
        self._store: dict[int, Task] = {}

    def add(self, task: Task) -> None:
        if task.id in self._store:
            raise ValueError("Task with id already exists")
        self._store[task.id] = task

    def update(self, task: Task) -> None:
        if task.id not in self._store:
            raise KeyError("Task not found")
        self._store[task.id] = task

    def get(self, task_id: int) -> Optional[Task]:
        return self._store.get(task_id)

    def list_all(self) -> List[Task]:
        return list(self._store.values())


class TaskManager:
    def __init__(self, repository: TaskRepository):
        self._repo = repository

    def add_task(self, task: Task) -> None:
        """Reglas de negocio al añadir tareas."""
        self._repo.add(task)

    def update_task(self, task_id: int, *, title: Optional[str] = None, status: Optional[Status] = None) -> Task:
        task = self._repo.get(task_id)
        if task is None:
            raise KeyError("Task not found")
        updated = task
        if title is not None:
            updated = updated.with_title(title)
        if status is not None:
            updated = updated.with_status(status)
        self._repo.update(updated)
        return updated

    def get_by_status(self, status: Status) -> List[Task]:
        return [t for t in self._repo.list_all() if t.status == status]

    def get(self, task_id: int) -> Optional[Task]:
        return self._repo.get(task_id)