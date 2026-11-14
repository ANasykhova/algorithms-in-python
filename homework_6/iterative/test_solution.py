import math
import random

import pytest
from iterative.solution import mergesort_iter, quicksort_iter


SORTS = [mergesort_iter, quicksort_iter]


# Граничные: пустой, один и два элемента
@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("arr, answer", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
])
def test_edge(sort, arr, answer):
    assert sort(arr) == answer


# Базовые: отсортированный, обратный, повторы, отрицательные, вещественные, примеры из визуализации
@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("arr, answer", [
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([2, 2, 2], [2, 2, 2]),
    ([1, 1, 2, 1, 1], [1, 1, 1, 1, 2]),
    ([-3, -1, -2], [-3, -2, -1]),
    ([0.5, -1, 2.5, 0], [-1, 0, 0.5, 2.5]),
    ([6, 2, 9, 4, 2, 7, 1], [1, 2, 2, 4, 6, 7, 9]),
    ([4, 8, 2, 5, 1, 5, 9, 3], [1, 2, 3, 4, 5, 5, 8, 9]),
])
def test_basic(sort, arr, answer):
    assert sort(arr) == answer


# Длины не степени двойки - неполный последний отрезок в mergesort
@pytest.mark.parametrize("number", [3, 5, 6, 7, 9, 15, 17, 33])
def test_mergesort_not_power_of_two(number):
    arr = list(range(number, 0, -1))
    assert mergesort_iter(arr) == sorted(arr)


# Входной массив не изменяется
@pytest.mark.parametrize("sort", SORTS)
def test_input_not_modified(sort):
    arr = [3, 1, 2, 5, 4]
    sort(arr)
    assert arr == [3, 1, 2, 5, 4]


# Нетривиальные: случайные массивы против sorted
@pytest.mark.parametrize("seed", range(20))
def test_random(seed):
    rnd = random.Random(seed)
    arr = [rnd.randint(-20, 20) for _ in range(rnd.randint(0, 200))]
    assert mergesort_iter(arr) == sorted(arr)
    assert quicksort_iter(arr) == sorted(arr)


# Большие входы: отсортированный, обратный, одинаковые, два значения
@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("arr", [
    list(range(100000)),
    list(range(100000, 0, -1)),
    [7] * 100000,
    [0, 1] * 50000,
])
def test_large(sort, arr):
    assert sort(arr) == sorted(arr)


# Явный стек quicksort не больше log n
@pytest.mark.parametrize("arr", [
    list(range(10000)),
    list(range(10000, 0, -1)),
    [5] * 10000,
    random.Random(1).sample(range(10000), 10000),
])
def test_quicksort_stack_is_logarithmic(arr):
    stats = {}
    quicksort_iter(arr, stats=stats)
    assert stats["max_stack"] <= math.log2(len(arr)) + 1


# Устойчивость mergesort: равные по ключу элементы сохраняют порядок
class Item:
    def __init__(self, key, tag):
        self.key, self.tag = key, tag

    def __le__(self, other):
        return self.key <= other.key


def test_mergesort_stable():
    items = [Item(2, "a"), Item(1, "b"), Item(2, "c"), Item(1, "d"), Item(2, "e")]
    answer = [(1, "b"), (1, "d"), (2, "a"), (2, "c"), (2, "e")]
    assert [(x.key, x.tag) for x in mergesort_iter(items)] == answer
