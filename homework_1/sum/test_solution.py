import pytest
from solution import max_even_sum


# Граничный - единственный элемент чётный, он и есть ответ
@pytest.mark.parametrize("nums, expected", [
    ([2],  2),
    ([8],  8),
    ([14], 14),
])
def test_single_even_element(nums, expected):
    assert max_even_sum(nums) == expected

# Граничный - единственный нечётный элемент, делящейся суммы нет
@pytest.mark.parametrize("nums", [
    [3], [7], [1],
])
def test_single_odd_element_returns_zero(nums):
    assert max_even_sum(nums) == 0

# Граничный - все элементы чётные, берём всё
@pytest.mark.parametrize("nums, expected", [
    ([2, 4, 6],    12),
    ([10, 20, 30], 60),
])
def test_all_even_take_all(nums, expected):
    assert max_even_sum(nums) == expected

# Базовые: убираем минимальный нечётный, чтобы потеря была наименьшей
@pytest.mark.parametrize("nums, expected", [
    ([5, 7, 13, 2, 14],  36),   # пример из условия: убираем 5, берём остальное
    ([1, 3, 5],           8),   # все нечётные: убираем 1
    ([7, 9, 11],         20),   # убираем 7, не 11
    ([1, 2, 4, 6],       12),   # один нечётный портит сумму, убираем его
    ([2, 99],             2),   # убираем большой нечётный, остаётся маленький чётный
])
def test_remove_min_odd_to_get_max_even(nums, expected):
    assert max_even_sum(nums) == expected

# Граничный - большие числа
@pytest.mark.parametrize("nums, expected", [
    ([1_000_000_000, 1],             1_000_000_000),
    ([1_000_000_000, 1_000_000_002], 2_000_000_002),
])
def test_large_values(nums, expected):
    assert max_even_sum(nums) == expected
