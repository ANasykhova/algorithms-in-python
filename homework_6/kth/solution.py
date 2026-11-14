"""
№ 3. K-th
Найти k-й по величине элемент массива
(без сортировки всего массива и без куч)

Решение: quickselect
1) k-й наибольший стоит на позиции target = n - k в отсортированном массиве
2) работаем с отрезком [low, high], сначала это весь массив
3) выбираем случайный pivot из отрезка
4) трехпутевое разбиение за один проход:
[low, lt) < pivot, [lt, gt] == pivot, (gt, high] > pivot
блок [lt, gt] уже стоит на своих местах
5) если lt <= target <= gt => ответ pivot
если target < lt => ищем левее: high = lt - 1
если target > gt => ищем правее: low = gt + 1
6) отрезок сузился до одного элемента => это ответ
7) k вне 1..n => ValueError

Почему так:
- идем только в одну часть, а не в обе как quicksort => O(n) в среднем
- случайный pivot: нет худшего случая на отсортированном входе
- трехпутевое разбиение: повторы pivot отсекаются за один проход
- цикл вместо рекурсии: нет RecursionError

Корректность: левее lt только меньшие pivot, правее gt только большие
значит позиции lt..gt в отсортированном массиве заняты pivot,
а элемент с позицией target лежит в той части, куда попал target
отрезок каждый раз строго уменьшается => цикл завершается

Сложность:
O(n) по времени в среднем - n + 3n/4 + (3/4)**2 n + ...
O(n**2) по времени в худшем - pivot каждый раз крайний, маловероятно
O(n) по памяти - копия входа
O(1) дополнительной памяти - только индексы, рекурсии нет

Визуализация:
find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4, seed = 4)
n = 9, target = 9 - 4 = 5
после разбиения отрезок показан тремя зонами: (меньше) [равные] (больше)

Шаг 1:
low = 0, high = 8, pivot = arr[3] = 1
() [1] (3, 2, 2, 4, 5, 5, 6, 3), lt = gt = 0
target = 5 > 0 => low = 1

Шаг 2:
low = 1, high = 8, pivot = arr[5] = 5
(3, 2, 2, 4, 3) [5, 5] (6), lt = 6, gt = 7
target = 5 < 6 => high = 5

Шаг 3:
low = 1, high = 5, pivot = arr[1] = 3
(2, 2) [3, 3] (4), lt = 3, gt = 4
target = 5 > 4 => low = 5

Шаг 4:
low = high = 5 => отрезок из одного элемента => ответ arr[5] = 4

Массив в конце: [1, 2, 2, 3, 3, 4, 5, 5, 6] => 4-й с конца = 4
пятерки и тройки отсеяны целиком за одно разбиение
"""

import random


def _partition3(arr, low, high, pivot):
    lt, i, gt = low, low, high
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def find_kth_largest(nums, k, seed=None):
    # seed - зерно для выбора pivot, нужно для воспроизводимой визуализации
    n = len(nums)
    if not 1 <= k <= n:
        raise ValueError(f"k должно быть от 1 до {n}, получено {k}")

    arr = list(nums)
    rnd = random.Random(seed)
    target = n - k
    low, high = 0, n - 1
    while low < high:
        pivot = arr[rnd.randint(low, high)]
        lt, gt = _partition3(arr, low, high, pivot)
        if target < lt:
            high = lt - 1
        elif target > gt:
            low = gt + 1
        else:
            return pivot
    return arr[low]


if __name__ == "__main__":
    nums = list(map(int, input("Массив: ").split()))
    k = int(input("k: "))
    print(f"{k}-й наибольший:", find_kth_largest(nums, k))
