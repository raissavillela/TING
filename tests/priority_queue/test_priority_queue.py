from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    new_queue = PriorityQueue()

    high_priority = {"nome_do_arquivo": "file1.txt", "qtd_linhas": 3}
    high_priority2 = {"nome_do_arquivo": "file2.txt", "qtd_linhas": 2}
    regular_priority = {"nome_do_arquivo": "file3.txt", "qtd_linhas": 5}
    regular_priority2 = {"nome_do_arquivo": "file4.txt", "qtd_linhas": 7}

    new_queue.enqueue(regular_priority)
    new_queue.enqueue(high_priority)
    new_queue.enqueue(regular_priority2)
    new_queue.enqueue(high_priority2)

    assert len(new_queue) == 4

    assert new_queue.dequeue() == high_priority
    assert new_queue.dequeue() == high_priority2
    assert new_queue.dequeue() == regular_priority
    assert new_queue.dequeue() == regular_priority2

    new_queue.enqueue(high_priority)
    new_queue.enqueue(regular_priority)

    assert new_queue.search(0) == high_priority
    assert new_queue.search(1) == regular_priority

    with pytest.raises(IndexError):
        new_queue.search(-1)
    with pytest.raises(IndexError):
        new_queue.search(2)