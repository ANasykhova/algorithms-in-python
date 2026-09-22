import pytest
from solution import validate_stack_sequences


# Граничный - один элемент (минимальный len по условию)
def test_single_element():
    assert validate_stack_sequences([1], [1]) is True

# Граничный - полный разворот и прямой порядок (pop только в конце)
@pytest.mark.parametrize("pushed, popped, answer", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
])
def test_all_push_then_pop(pushed, popped, answer):
    assert validate_stack_sequences(pushed, popped) is answer

# Базовые
@pytest.mark.parametrize("pushed, popped, answer", [
    ([1, 2, 3, 4, 5], [1, 3, 5, 4, 2], True),
    ([1, 2, 3], [3, 1, 2], False),
    ([1, 2, 3, 4, 5], [3, 5, 4, 2, 1], True),
    ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], [3, 1, 4, 2, 5], False),  # после pop(3) нужен 1, но наверху 2
    ([1, 2, 3, 4, 5], [5, 3, 4, 2, 1], False),  # после pop(5) нужен 3, но наверху 4
])
def test_basic_examples(pushed, popped, answer):
    assert validate_stack_sequences(pushed, popped) is answer

# Граничный - большой ввод (проверка O(n) по производительности)
def test_large_input():
    n = 100000
    pushed = list(range(n))
    popped = list(range(n - 1, -1, -1))  # разворот: всегда True
    assert validate_stack_sequences(pushed, popped) is True
