import pytest
from src.repositories.in_memory.in_memory_task_repository import InMemoryTaskRepository
from src.utils.errors.resource_not_found import ResourceNotFoundError
from src.services.tasks.use_cases.find_task import FindTaskUseCase
from tests.fixtures.tasks import task_repository


def test_it_shoud_be_able_to_fetch_a_task(task_repository):
    task_id = "id-2"
    task = FindTaskUseCase(task_repository).execute(task_id)

    assert task.title == "My Task 02"


def test_it_shoud_not_be_able_to_fetch_a_task_that_not_exists(task_repository):
    task_id = "id-5"

    with pytest.raises(ResourceNotFoundError) as err:
        FindTaskUseCase(task_repository).execute(task_id)
    assert str(err.value) == "Resource Not Found"


if __name__ == "__main__":
    pytest.main()
