import pytest
from solution import max_even_sum


# Граничный - единственный элемент четный, он и есть ответ
@pytest.mark.parametrize("nums, expected", [
    ([2],  2),
    ([8],  8),
    ([14], 14),
])
def test_single_even_element(nums, expected):
    assert max_even_sum(nums) == expected

# Граничный - единственный нечетный элемент, делящейся суммы нет
@pytest.mark.parametrize("nums", [
    [3], [7], [1],
])
def test_single_odd_element_returns_zero(nums):
    assert max_even_sum(nums) == 0

# Граничный - все элементы четные, берем все
@pytest.mark.parametrize("nums, expected", [
    ([2, 4, 6],    12),
    ([10, 20, 30], 60),
])
def test_all_even_take_all(nums, expected):
    assert max_even_sum(nums) == expected

# Базовые: убираем минимальный нечетный, чтобы потеря была наименьшей
@pytest.mark.parametrize("nums, expected", [
    ([5, 7, 13, 2, 14],  36),   # пример из условия: убираем 5, берем остальное
    ([1, 3, 5],           8),   # все нечетные: убираем 1
    ([7, 9, 11],         20),   # убираем 7, не 11
    ([1, 2, 4, 6],       12),   # один нечетный портит сумму, убираем его
    ([2, 99],             2),   # убираем большой нечетный, остается маленький четный
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
