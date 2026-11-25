import pytest
from .solution import find_kth_largest, find_kth_largest_heapq


@pytest.mark.parametrize("func", [find_kth_largest, find_kth_largest_heapq])
@pytest.mark.parametrize("nums, k, answer", [
    # Из условия
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    # Граничные: k = 1 (максимум)
    ([1, 2, 3], 1, 3),
    ([5, 1, 3], 1, 5),
    # Граничные: k = len (минимум)
    ([1, 2, 3], 3, 1),
    ([4, 2, 7], 3, 2),
    # Один элемент
    ([42], 1, 42),
    # Дубликаты
    ([3, 3, 3, 3], 2, 3),
    ([1, 2, 2, 3], 2, 2),
    ([5, 5, 1, 1], 3, 1),
    # Уже отсортирован
    ([1, 2, 3, 4, 5], 2, 4),
    ([1, 2, 3, 4, 5], 4, 2),
    # Обратный порядок
    ([5, 4, 3, 2, 1], 3, 3),
    # Нетривиальный: большой массив с очевидным ответом
    (list(range(1, 101)), 10, 91),
    (list(range(100, 0, -1)), 1, 100),
])
def test_kth_largest(func, nums, k, answer):
    assert func(nums, k) == answer


# Входной массив не изменяется

@pytest.mark.parametrize("func", [find_kth_largest, find_kth_largest_heapq])
def test_input_unchanged(func):
    nums = [3, 1, 4, 1, 5, 9]
    original = nums[:]
    func(nums, 2)
    assert nums == original


# Результат совпадает с наивной сортировкой

@pytest.mark.parametrize("func", [find_kth_largest, find_kth_largest_heapq])
@pytest.mark.parametrize("nums, k", [
    ([7, 2, 5, 1, 9, 3], 3),
    ([10, 10, 9, 8, 7], 2),
    ([1], 1),
    ([4, 3, 2, 1], 4),
])
def test_matches_sorted(func, nums, k):
    answer = sorted(nums, reverse=True)[k - 1]
    assert func(nums, k) == answer
