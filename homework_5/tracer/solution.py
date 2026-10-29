"""
№ 1. Tracer
Декоратор, отображающий стек вызовов рекурсивной функции.

Каждый вызов выводит:
  -> func(args) - вход с отступом глубины стека
  <- func(args) = result - выход с результатом

Реализация:
1) хранить глубину как изменяемый список [0], чтобы вложенные функции могли менять счетчик
2) перед вызовом - напечатать стрелку входа и увеличить глубину
3) после вызова - уменьшить глубину и напечатать стрелку выхода с результатом

Сложность:
O(1) по времени - накладных расходов на каждый уровень рекурсии
O(h) по памяти - стек рекурсии глубиной h

Визуализация для factorial(3):

-> factorial(3)
  -> factorial(2)
    -> factorial(1)
    <- factorial(1) = 1
  <- factorial(2) = 2
<- factorial(3) = 6
"""

import functools


def trace(func):
    depth = [0]  # список, чтобы вложенная функция могла изменять значение

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        indent = "  " * depth[0]
        args_repr = ", ".join(repr(a) for a in args)
        kwargs_repr = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_repr, kwargs_repr]))
        print(f"{indent}-> {func.__name__}({all_args})")
        depth[0] += 1
        result = func(*args, **kwargs)
        depth[0] -= 1
        print(f"{indent}<- {func.__name__}({all_args}) = {result}")
        return result

    return wrapper


if __name__ == "__main__":
    @trace
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    n = int(input("n: "))
    print(f"\nfactorial({n}) =", factorial(n))
