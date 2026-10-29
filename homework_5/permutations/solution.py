"""
№ 2. Permutations
Все перестановки массива через бэктрекинг с визуализацией стека вызовов

Алгоритм:
1) backtrack(current, remaining) — к текущей перестановке добавляем
по одному элементу из оставшихся, рекурсивно перебирая все варианты
2) база рекурсии: remaining пуст -> готовая перестановка добавляется в результат
3) декоратор @trace показывает стек вызовов с отступами

Сложность:
O(n * n!) по времени - n! перестановок, каждую собираем за O(n)
O(n) по памяти - глубина стека рекурсии не превышает n

Визуализация для [1, 2]:

-> backtrack([], [1, 2])
  -> backtrack([1], [2])
    -> backtrack([1, 2], [])
    <- backtrack([1, 2], []) = None
  <- backtrack([1], [2]) = None
  -> backtrack([2], [1])
    -> backtrack([2, 1], [])
    <- backtrack([2, 1], []) = None
  <- backtrack([2], [1]) = None
<- backtrack([], [1, 2]) = None

Результат: [[1, 2], [2, 1]]
"""

import functools
from tracer.solution import trace

# def trace(func):
#     depth = [0]
#
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         indent = "  " * depth[0]
#         args_repr = ", ".join(repr(a) for a in args)
#         print(f"{indent}→ {func.__name__}({args_repr})")
#         depth[0] += 1
#         result = func(*args, **kwargs)
#         depth[0] -= 1
#         print(f"{indent}← {func.__name__}({args_repr}) = {result}")
#         return result
#
#     return wrapper


def permute(nums):
    result = []

    @trace
    def backtrack(current, remaining):
        if not remaining:
            result.append(list(current))
            return
        for i in range(len(remaining)):
            backtrack(current + [remaining[i]], remaining[:i] + remaining[i+1:])

    backtrack([], list(nums))
    return result


if __name__ == "__main__":
    nums = list(map(int, input("Массив: ").split()))
    perms = permute(nums)
    print(f"\nВсего перестановок: {len(perms)}")
    for p in perms:
        print(p)
