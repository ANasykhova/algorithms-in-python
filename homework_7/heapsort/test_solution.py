import random
import pytest
from .solution import heapsort


@pytest.mark.parametrize("arr, answer", [
    # Граничные
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    # Уже отсортирован
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    # Обратный порядок
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    # Произвольный
    ([4, 10, 3, 5, 1], [1, 3, 4, 5, 10]),
    # Дубликаты
    ([3, 1, 2, 1, 3], [1, 1, 2, 3, 3]),
    ([5, 5, 5], [5, 5, 5]),
    # Нетривиальные
    ([9, 4, 7, 1, 8, 3, 2, 6, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], [1, 2, 2, 3, 3, 4, 5, 5, 6]),
])
def test_heapsort(arr, answer):
    heapsort(arr)
    assert arr == answer


# Совпадает с sorted()

@pytest.mark.parametrize("arr", [
    [7, 2, 5, 1, 9, 3, 8, 4, 6],
    list(range(20, 0, -1)),
    [1] * 10,
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
])
def test_matches_sorted(arr):
    answer = sorted(arr)
    heapsort(arr)
    assert arr == answer


# Inplace: функция изменяет переданный массив

def test_inplace():
    arr = [3, 1, 2]
    original_id = id(arr)
    heapsort(arr)
    assert id(arr) == original_id
    assert arr == [1, 2, 3]


# Случайные массивы

@pytest.mark.parametrize("number", [10, 100, 1000])
def test_random(number):
    arr = [random.randint(-1000, 1000) for _ in range(number)]
    answer = sorted(arr)
    heapsort(arr)
    assert arr == answer
