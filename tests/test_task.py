
import pytest
from src.task import Task, Priority, Status, ValidationError


def test_task_valid_creation():
    t = Task(id=1, title="Comprar leche", priority=Priority.HIGH, status=Status.TODO)
    assert t.id == 1
    assert t.title == "Comprar leche"


@pytest.mark.parametrize("bad_id", [-1, 'a'])
def test_task_invalid_id(bad_id):
    with pytest.raises(ValidationError):
        Task(id=bad_id, title="x")


def test_task_title_length():
    long_title = 'x' * 201
    with pytest.raises(ValidationError):
        Task(id=1, title=long_title)


def test_task_with_status_returns_new_instance():
    t = Task(id=1, title="t")
    t2 = t.with_status(Status.DONE)
    assert t is not t2
    assert t.status == Status.TODO
    assert t2.status == Status.DONE
    