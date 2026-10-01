import pytest
from solution import two_sum


# Граничный - массив из двух элементов
@pytest.mark.parametrize("arr, k, answer", [
    ([5, 5], 10, (0, 1)),
    ([1, 9], 10, (0, 1)),
])
def test_two_element_array(arr, k, answer):
    assert two_sum(arr, k) == answer

# Граничный - отрицательные числа и нули
@pytest.mark.parametrize("arr, k, answer", [
    ([-1, -2, -3, -4, -5], -8, (2, 4)),
    ([0, 4, 3, 0], 0, (0, 3)),
    ([-3, 4, 3, 90], 0, (0, 2)),
])
def test_negatives_and_zero(arr, k, answer):
    assert two_sum(arr, k) == answer

# Базовые: пара не первые два элемента, пара в конце
@pytest.mark.parametrize("arr, k, answer", [
    ([2, 7, 11, 15], 9, (0, 1)),
    ([3, 2, 4], 6, (1, 2)),
    ([1, 2, 3, 4, 5], 9, (3, 4)),
    ([1, 3, 4, 10], 7, (1, 2)),
    ([5, 5, 1, 4], 10, (0, 1)),
])
def test_various_positions(arr, k, answer):
    assert two_sum(arr, k) == answer
