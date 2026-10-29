import math
import pytest
from solution import permute

# корректность результата
@pytest.mark.parametrize("nums, answer", [
    ([], [[]]),
    ([1], [[1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
])
def test_permute_result(nums, answer):
    assert permute(nums) == answer


# Количество перестановок = n!
@pytest.mark.parametrize("nums", [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
])
def test_permute_count(nums):
    assert len(permute(nums)) == math.factorial(len(nums))


# Каждая перестановка - сортированный исходный массив
@pytest.mark.parametrize("nums", [
    [1, 2, 3],
    [3, 1, 2],
    [0, 1, 2, 3],
])
def test_permute_each_is_rearrangement(nums):
    for perm in permute(nums):
        assert sorted(perm) == sorted(nums)


# Все перестановки уникальны
@pytest.mark.parametrize("nums", [
    [1, 2, 3],
    [1, 2, 3, 4],
])
def test_permute_no_duplicates(nums):
    result = permute(nums)
    assert len(result) == len(set(map(tuple, result)))


# Декоратор trace выводит стек вызовов
def test_permute_trace_output(capsys):
    permute([1, 2])
    out = capsys.readouterr().out
    assert "-> backtrack" in out
    assert "<- backtrack" in out