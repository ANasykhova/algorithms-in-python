"""
№ 1. Compare
Рекурсивные версии mergesort и quicksort
Декоратор, замеряющий время выполнения функции
Тесты, на которых время выполнения сортировок сильно отличается

Решение:
Mergesort
1) делим массив пополам
2) рекурсивно сортируем каждую половину
3) сливаем две отсортированные половины: каждый раз берем меньший
из двух текущих элементов (при равенстве из левой - сортировка устойчивая)
4) база рекурсии: массив длины <= 1 уже отсортирован
Корректность: по индукции половины отсортированы,
а слияние каждый раз берет наименьший из оставшихся

Quicksort
1) pivot = последний элемент
2) раскладываем элементы в три новых списка: less < pivot, equal == pivot, greater > pivot
3) рекурсивно сортируем less и greater, склеиваем less + equal + greater
4) все копии pivot сразу попадают в equal и в рекурсию не идут
Pivot "последний элемент" выбран специально, чтобы показать худший случай

Корректность quicksort: все из less меньше всех из equal, а те меньше всех из greater
less и greater строго короче массива (в equal есть хотя бы pivot)
=> рекурсия завершается, склейка отсортированных частей отсортирована

Декоратор timer
1) засекает time.perf_counter до и после вызова
2) печатает время и сохраняет его в атрибут wrapper.last_time
3) functools.wraps сохраняет имя и докстринг функции
Применяем как timer(mergesort), чтобы замерить всю сортировку,
а не каждый рекурсивный вызов

Входы, на которых время сильно отличается (make_cases)
- случайный: обе сортировки O(n log n), время почти равное
- отсортированный и обратный: pivot всегда максимум или минимум
=> quicksort деградирует до O(n**2), mergesort не меняется
- много повторов (значения 0..9): quicksort отсекает все копии pivot
=> глубина рекурсии <= 10, он быстрее mergesort

Замер при n = 4000 (мс, на другой машине числа другие, соотношения те же):
случайный: merge 5.4, quick 5.6
отсортированный: merge 3.5, quick 557 => quicksort медленнее в 160 раз
обратный: merge 4.3, quick 551 => quicksort медленнее в 130 раз
много повторов: merge 5.2, quick 0.9 => quicksort быстрее в 6 раз


Сложность:
Mergesort
O(n log n) по времени - log n уровней, слияние O(n)
O(n) по памяти - срезы на пути рекурсии: n + n/2 + ...

Quicksort
O(n log n) по времени в среднем - части уменьшаются примерно вдвое
O(n**2) по времени в худшем - части n-1 и 0
O(n) по памяти в среднем - новые списки на пути рекурсии
O(n**2) по памяти в худшем - n + (n-1) + ... списков
На отсортированном входе глубина рекурсии n => при n > 10000 RecursionError

Timer
O(1) по времени и памяти - два замера времени

Визуализация:
mergesort([5, 3, 8, 1, 3])
Шаг 1, деление (mid = len // 2):
[5, 3, 8, 1, 3] => [5, 3] и [8, 1, 3]

Шаг 2, деление:
[5, 3] => [5] и [3]
[8, 1, 3] => [8] и [1, 3]
[1, 3] => [1] и [3]

Шаг 3, слияние снизу вверх:
[5] + [3] => [3, 5]
[1] + [3] => [1, 3]
[8] + [1, 3] => [1, 3, 8]

Шаг 4, слияние [3, 5] и [1, 3, 8]:
3 vs 1 => берем 1, result = [1]
3 vs 3 => равны, берем из левой (<=), result = [1, 3]
5 vs 3 => берем 3, result = [1, 3, 3]
5 vs 8 => берем 5, result = [1, 3, 3, 5]
левая кончилась => дописываем [8], result = [1, 3, 3, 5, 8]
тройка из левой половины осталась раньше тройки из правой => устойчивость


quicksort([5, 3, 8, 1, 3])
Шаг 1:
[5, 3, 8, 1, 3], pivot = 3
less = [1], equal = [3, 3], greater = [5, 8]

Шаг 2:
quicksort([1]) => длина 1 => [1]
quicksort([5, 8]), pivot = 8
less = [5], equal = [8], greater = [] => [5] + [8] + [] = [5, 8]

Шаг 3:
[1] + [3, 3] + [5, 8] = [1, 3, 3, 5, 8]

Худший случай quicksort: [1, 2, 3, 4]
pivot = 4 => less = [1, 2, 3], greater = []
pivot = 3 => less = [1, 2], greater = []
pivot = 2 => less = [1], greater = []
Каждый уровень убирает один элемент => глубина n, сравнений n + (n-1) + ... = O(n**2)
"""

import functools
import random
import sys
import time

sys.setrecursionlimit(10000)


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        wrapper.last_time = time.perf_counter() - start
        print(f"{func.__name__}: {wrapper.last_time:.6f}s")
        return result

    wrapper.last_time = 0.0
    return wrapper


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(arr):
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    return _merge(mergesort(arr[:mid]), mergesort(arr[mid:]))


def quicksort(arr):
    if len(arr) <= 1:
        return list(arr)
    pivot = arr[-1]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)


def make_cases(number, seed=0):
    rnd = random.Random(seed)
    return {
        "случайный": [rnd.randint(0, 1000000) for _ in range(number)],
        "отсортированный": list(range(number)),
        "обратный": list(range(number, 0, -1)),
        "много повторов": [rnd.randint(0, 9) for _ in range(number)],
    }


if __name__ == "__main__":
    number = int(input("Размер массива (до 9000): "))
    timed_merge = timer(mergesort)
    timed_quick = timer(quicksort)
    for name, arr in make_cases(number).items():
        print(f"\n{name}:")
        timed_merge(arr)
        timed_quick(arr)
        if timed_merge.last_time > 0:
            print(f"quick / merge = {timed_quick.last_time / timed_merge.last_time:.2f}")
