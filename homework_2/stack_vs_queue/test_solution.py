import pytest
from solution import Stack, Queue


# Граничный - пустые структуры: ошибки и флаги
def test_stack_empty_raises():
    s = Stack()
    assert s.is_empty() is True
    assert len(s) == 0
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()

def test_queue_empty_raises():
    q = Queue()
    assert q.is_empty() is True
    assert len(q) == 0
    with pytest.raises(IndexError):
        q.dequeue()
    with pytest.raises(IndexError):
        q.peek()

# Базовые: LIFO у стека, FIFO у очереди
def test_stack_lifo_order():
    s = Stack()
    for v in [1, 2, 3]:
        s.push(v)
    assert [s.pop() for _ in range(3)] == [3, 2, 1]

def test_queue_fifo_order():
    q = Queue()
    for v in [1, 2, 3]:
        q.enqueue(v)
    assert [q.dequeue() for _ in range(3)] == [1, 2, 3]

# peek не снимает элемент, размер не меняется
def test_stack_peek_does_not_pop():
    s = Stack()
    s.push(42)
    assert s.peek() == 42
    assert s.peek() == 42
    assert len(s) == 1

def test_queue_peek_does_not_dequeue():
    q = Queue()
    q.enqueue(42)
    assert q.peek() == 42
    assert q.peek() == 42
    assert len(q) == 1

# размер корректно обновляется при push/pop и enqueue/dequeue
@pytest.mark.parametrize("values", [[1], [1, 2, 3], [5, 5, 5, 5]])
def test_stack_size_updates(values):
    s = Stack()
    for v in values:
        s.push(v)
    assert len(s) == len(values)
    s.pop()
    assert len(s) == len(values) - 1


@pytest.mark.parametrize("values", [[1], [1, 2, 3], [5, 5, 5, 5]])
def test_queue_size_updates(values):
    q = Queue()
    for v in values:
        q.enqueue(v)
    assert len(q) == len(values)
    q.dequeue()
    assert len(q) == len(values) - 1


# операции вперемешку
def test_stack_interleaved():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 1
    assert s.is_empty()


def test_queue_interleaved():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()
