import pytest
from solution import count_primes


# Граничный - нет простых при n < 2
@pytest.mark.parametrize("n", [0, 1, 2])
def test_no_primes_for_small_n(n):
    assert count_primes(n) == 0

# Граничный - n само является простым: оно не считается (строго < n)
@pytest.mark.parametrize("n, expected", [
    (3,  1),   # < 3: только {2}
    (7,  3),   # < 7: {2, 3, 5}
    (11, 4),   # < 11: {2, 3, 5, 7}
])
def test_n_is_prime_itself_not_counted(n, expected):
    assert count_primes(n) == expected

# Базовые: классические контрольные значения π(n)
@pytest.mark.parametrize("n, expected", [
    (10,   4),   # пример из условия: 2, 3, 5, 7
    (12,   5),   # добавляется 11
    (100, 25),
])
def test_basic_examples(n, expected):
    assert count_primes(n) == expected

# Граничный - большие n, проверяем производительность решета
@pytest.mark.parametrize("n, expected", [
    (1000,       168),
    (100000,    9592),
    (1000000, 78498),
])
def test_large_n(n, expected):
    assert count_primes(n) == expected
