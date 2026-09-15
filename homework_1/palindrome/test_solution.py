import pytest
from solution import is_palindrome


# Граничный (подразумевается, что придет число, хотя бы цифра) - самый короткий вариант
@pytest.mark.parametrize("number", [0, 7, 9])
def test_single_digit_always_palindrome(number):
    assert is_palindrome(number) is True

# Граничный - самый "маленький" вариант
@pytest.mark.parametrize("number", [-121, -7, -1000])
def test_negative_always_palindrome(number):
    assert is_palindrome(number) is True

# Числа с нулями - ни одно положительное число, оканчивающееся на 0, не является палиндромом
@pytest.mark.parametrize("number", [10, 100, 1000, 20, 350])
def test_trailing_zero_is_not_palindrome(number):
    assert is_palindrome(number) is False

# Базовые: четное и нечетное число цифр
@pytest.mark.parametrize("number, answer", [
    (121, True),
    (31, False),
    (1221, True),
    (1321, False),
    (9999, True),
    (14341, True),
    (14361, False),
    (1234321, True),
    (1000021, False),
])
def test_basic_examples(number, answer):
    assert is_palindrome(number) is answer

# Граничный (четко в условии не обговариавается, но примерно по стандарту) - самый длинный вариант
@pytest.mark.parametrize("number, answer", [
    (1000000001,   True),
    (1000000007,   False)
])
def test_large(number, answer):
    assert is_palindrome(number) is answer