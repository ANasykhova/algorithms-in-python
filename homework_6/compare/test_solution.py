import random

import pytest
from compare.solution import make_cases, mergesort, quicksort, timer


SORTS = [mergesort, quicksort]


# Граничные: пустой, один и два элемента
@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("arr, answer", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
])
def test_edge(sort, arr, answer):
    assert sort(arr) == answer


# Базовые: отсортированный, обратный, повторы, отрицательные, вещественные
@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("arr, answer", [
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
    ([5, 3, 8, 1, 3], [1, 3, 3, 5, 8]),
    ([2, 2, 2], [2, 2, 2]),
    ([-3, -1, -2], [-3, -2, -1]),
    ([0.5, -1, 2.5, 0], [-1, 0, 0.5, 2.5]),
])
def test_basic(sort, arr, answer):
    assert sort(arr) == answer


# Входной массив не изменяется
@pytest.mark.parametrize("sort", SORTS)
def test_input_not_modified(sort):
    arr = [3, 1, 2]
    sort(arr)
    assert arr == [3, 1, 2]


# Нетривиальные: случайные массивы против sorted
@pytest.mark.parametrize("seed", range(20))
def test_random(seed):
    rnd = random.Random(seed)
    arr = [rnd.randint(-20, 20) for _ in range(rnd.randint(0, 300))]
    assert mergesort(arr) == sorted(arr)
    assert quicksort(arr) == sorted(arr)


# Устойчивость mergesort: равные по ключу элементы сохраняют порядок
class Item:
    def __init__(self, key, tag):
        self.key, self.tag = key, tag

    def __le__(self, other):
        return self.key <= other.key


def test_mergesort_stable():
    items = [Item(3, "a"), Item(1, "b"), Item(3, "c"), Item(1, "d")]
    answer = [(1, "b"), (1, "d"), (3, "a"), (3, "c")]
    assert [(x.key, x.tag) for x in mergesort(items)] == answer


# Большой массив из одинаковых элементов не деградирует
def test_quicksort_all_equal_large():
    arr = [7] * 50000
    assert quicksort(arr) == arr


# Декоратор: возвращает результат, сохраняет время и имя функции
def test_timer(capsys):
    def square(number):
        """docstring"""
        return number * number

    timed = timer(square)
    assert timed(5) == 25
    assert timed.last_time >= 0
    assert timed.__name__ == "square"
    assert timed.__doc__ == "docstring"
    assert timed.__wrapped__ is square
    assert capsys.readouterr().out.startswith("square: ")


# Разница во времени: на отсортированном и обратном quicksort O(n**2)
@pytest.mark.parametrize("case", ["отсортированный", "обратный"])
def test_time_ordered_mergesort_faster(case):
    arr = make_cases(1000)[case]
    timed_merge, timed_quick = timer(mergesort), timer(quicksort)
    timed_merge(arr)
    timed_quick(arr)
    assert timed_quick.last_time > timed_merge.last_time * 5


# Разница во времени: на повторах quicksort быстрее (копии pivot отсекаются сразу)
def test_time_duplicates_quicksort_faster():
    arr = make_cases(20000)["много повторов"]
    timed_merge, timed_quick = timer(mergesort), timer(quicksort)
    best_merge = best_quick = float("inf")
    for _ in range(3):
        timed_merge(arr)
        timed_quick(arr)
        best_merge = min(best_merge, timed_merge.last_time)
        best_quick = min(best_quick, timed_quick.last_time)
    assert best_quick * 2 < best_merge


# Входы для сравнения: нужной длины и нужного вида
def test_make_cases():
    cases = make_cases(100)
    assert all(len(arr) == 100 for arr in cases.values())
    assert cases["отсортированный"] == sorted(cases["отсортированный"])
    assert cases["обратный"] == sorted(cases["обратный"], reverse=True)
    assert set(cases["много повторов"]) <= set(range(10))
