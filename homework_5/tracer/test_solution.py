import pytest
from solution import trace

# вспомогательные: самые простые рекурсии с семинара - факториал и Фибоначчи
@trace
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


@trace
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

@pytest.mark.parametrize("n, answer", [
    (0, 1),
    (1, 1),
    (2, 2),
    (5, 120),
    (10, 3628800),
])
def test_factorial_result(n, answer):
    assert factorial(n) == answer


@pytest.mark.parametrize("n, answer", [
    (0, 0),
    (1, 1),
    (2, 1),
    (6, 8),
])
def test_fib_result(n, answer):
    assert fib(n) == answer


# Количество строк вывода: каждый вызов дает строку входа и строку выхода
@pytest.mark.parametrize("n, line_count", [
    (0, 2),  # 1 вызов
    (1, 4),  # 2 вызова
    (2, 6),  # 3 вызова
    (4, 10),  # 5 вызовов
])
def test_trace_line_count(capsys, n, line_count):
    @trace
    def dec(n):
        if n == 0:
            return 0
        return dec(n - 1)

    dec(n)
    lines = capsys.readouterr().out.strip().split("\n")
    assert len(lines) == line_count


# Первая строка - вход, последняя - выход
@pytest.mark.parametrize("n", [0, 1, 3])
def test_trace_first_last_lines(capsys, n):
    @trace
    def dec(n):
        if n == 0:
            return 0
        return dec(n - 1)

    dec(n)
    lines = capsys.readouterr().out.strip().split("\n")
    assert lines[0].startswith("-> dec")
    assert lines[-1].startswith("<- dec")


# Отступ растет с глубиной стека
@pytest.mark.parametrize("line_idx, prefix", [
    (0, "->"),
    (1, "  ->"),
    (2, "    ->"),
    (3, "      ->"),
])
def test_trace_indent_depth(capsys, line_idx, prefix):
    @trace
    def countdown(n):
        if n == 0:
            return 0
        return countdown(n - 1)

    countdown(3)
    lines = capsys.readouterr().out.strip().split("\n")
    assert lines[line_idx].startswith(prefix)


# Строка выхода содержит результат
@pytest.mark.parametrize("val, expected_result", [
    (0, "= 0"),
    (3, "= 9"),
    (4, "= 16"),
])
def test_trace_shows_result(capsys, val, expected_result):
    @trace
    def square(n):
        return n * n

    square(val)
    out = capsys.readouterr().out
    assert expected_result in out


# functools.wraps сохраняет имя функции
@pytest.mark.parametrize("name", ["my_func", "compute", "helper"])
def test_trace_preserves_name(name):
    func = trace(lambda x: x)
    func.__name__ = name
    assert func.__name__ == name


# Глубина сбрасывается между независимыми вызовами
@pytest.mark.parametrize("calls", [
    [1, 2],
    [5, 10],
    [0, 0, 0],
])
def test_trace_depth_resets_between_calls(capsys, calls):
    @trace
    def identity(x):
        return x

    for c in calls:
        identity(c)
    lines = capsys.readouterr().out.strip().split("\n")
    # каждый вызов дает 2 строки, обе без отступа
    for i in range(0, len(lines), 2):
        assert lines[i].startswith("->")