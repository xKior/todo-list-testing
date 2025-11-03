import pytest
from src.task_manager import InMemoryTaskRepository, TaskManager
from src.task import Task, Status, Priority


@pytest.fixture
def repo():
    return InMemoryTaskRepository()


@pytest.fixture
def manager(repo):
    return TaskManager(repo)


def test_add_and_get_task(manager):
    t = Task(id=10, title="Prueba")
    manager.add_task(t)
    got = manager.get(10)
    assert got == t


def test_add_duplicate_raises(repo, manager):
    t = Task(id=1, title="A")
    repo.add(t)
    with pytest.raises(ValueError):
        manager.add_task(t)


def test_update_task_title_and_status(manager):
    t = Task(id=2, title="old")
    manager.add_task(t)
    updated = manager.update_task(2, title="new", status=Status.IN_PROGRESS)
    assert updated.title == "new"
    assert updated.status == Status.IN_PROGRESS
    assert manager.get(2).title == "new"


def test_update_nonexistent_raises(manager):
    with pytest.raises(KeyError):
        manager.update_task(999, title="x")


def test_get_by_status_filters(manager):
    a = Task(id=3, title="a", status=Status.TODO)
    b = Task(id=4, title="b", status=Status.DONE)
    manager.add_task(a)
    manager.add_task(b)
    todos = manager.get_by_status(Status.TODO)
    assert len(todos) == 1
    assert todos[0].id == 3