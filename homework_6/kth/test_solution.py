import random

import pytest
from kth.solution import find_kth_largest


# Примеры из условия
@pytest.mark.parametrize("nums, k, answer", [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
])
def test_examples(nums, k, answer):
    assert find_kth_largest(nums, k) == answer


# Граничные: один элемент, k = 1 (максимум), k = n (минимум)
@pytest.mark.parametrize("nums, k, answer", [
    ([1], 1, 1),
    ([2, 1], 1, 2),
    ([2, 1], 2, 1),
    ([3, 2, 1, 5, 6, 4], 1, 6),
    ([3, 2, 1, 5, 6, 4], 6, 1),
])
def test_edge(nums, k, answer):
    assert find_kth_largest(nums, k) == answer


# Базовые: одинаковые, отрицательные, отсортированный и обратный
@pytest.mark.parametrize("nums, k, answer", [
    ([7, 7, 7, 7], 2, 7),
    ([-5, -1, -3, -2], 1, -1),
    ([-5, -1, -3, -2], 4, -5),
    ([1, 2, 3, 4, 5], 3, 3),
    ([5, 4, 3, 2, 1], 3, 3),
])
def test_basic(nums, k, answer):
    assert find_kth_largest(nums, k) == answer


# Некорректное k и пустой массив
@pytest.mark.parametrize("nums, k", [
    ([1, 2, 3], 0),
    ([1, 2, 3], 4),
    ([1, 2, 3], -1),
    ([], 1),
])
def test_invalid_k(nums, k):
    with pytest.raises(ValueError):
        find_kth_largest(nums, k)


# Ответ не зависит от выбора pivot
@pytest.mark.parametrize("seed", range(20))
def test_any_seed(seed):
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, seed=seed) == 4


# Входной массив не изменяется
def test_input_not_modified():
    nums = [3, 2, 1, 5, 6, 4]
    find_kth_largest(nums, 2)
    assert nums == [3, 2, 1, 5, 6, 4]


# Нетривиальные: все k для одного массива и случайные массивы против sorted
def test_all_k():
    nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 5]
    answer = sorted(nums, reverse=True)
    for k in range(1, len(nums) + 1):
        assert find_kth_largest(nums, k) == answer[k - 1]


@pytest.mark.parametrize("seed", range(20))
def test_random(seed):
    rnd = random.Random(seed)
    nums = [rnd.randint(-50, 50) for _ in range(rnd.randint(1, 300))]
    k = rnd.randint(1, len(nums))
    assert find_kth_largest(nums, k) == sorted(nums, reverse=True)[k - 1]


# Большие входы: отсортированный, обратный, одинаковые
@pytest.mark.parametrize("nums, k", [
    (list(range(100000)), 100000),
    (list(range(100000)), 1),
    (list(range(100000, 0, -1)), 50000),
    ([7] * 100000, 30000),
])
def test_large(nums, k):
    assert find_kth_largest(nums, k) == sorted(nums, reverse=True)[k - 1]
