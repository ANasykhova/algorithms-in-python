import pytest
from .solution import makeheap_n_log_n, makeheap, _is_minheap


# Вспомогательная: обе функции дают валидный minheap

@pytest.mark.parametrize("func", [makeheap_n_log_n, makeheap])
@pytest.mark.parametrize("arr", [
    # Граничные
    [],
    [1],
    [2, 1],
    # Уже отсортирован
    [1, 2, 3, 4, 5],
    # Обратный порядок
    [5, 4, 3, 2, 1],
    # Произвольный
    [9, 4, 7, 1, 8, 3, 2],
    # Дубликаты
    [3, 3, 3],
    [5, 1, 5, 1],
])
def test_is_minheap(func, arr):
    result = func(arr)
    assert _is_minheap(result)
    assert sorted(result) == sorted(arr)


# Корректность: минимум всегда в корне

@pytest.mark.parametrize("func", [makeheap_n_log_n, makeheap])
@pytest.mark.parametrize("arr", [
    [3, 1, 2],
    [9, 4, 7, 1, 8, 3, 2],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [42],
    [1, 2],
])
def test_min_at_root(func, arr):
    result = func(arr)
    assert result[0] == min(arr)


# Набор элементов не меняется

@pytest.mark.parametrize("func", [makeheap_n_log_n, makeheap])
@pytest.mark.parametrize("arr", [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [5, 4, 3, 2, 1],
    [1, 1, 1, 2, 2],
])
def test_same_elements(func, arr):
    result = func(arr)
    assert sorted(result) == sorted(arr)


# Входной массив не изменяется

@pytest.mark.parametrize("func", [makeheap_n_log_n, makeheap])
def test_input_unchanged(func):
    arr = [3, 1, 4, 1, 5]
    original = arr[:]
    func(arr)
    assert arr == original


# Точный ответ для малых случаев (детерминированных)

@pytest.mark.parametrize("func", [makeheap_n_log_n, makeheap])
@pytest.mark.parametrize("arr, answer", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 3, 3], [3, 3, 3]),
])
def test_exact_result(func, arr, answer):
    assert func(arr) == answer
