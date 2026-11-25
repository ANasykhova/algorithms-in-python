"""
№ 3. Heapsort

Сортировка кучей inplace без heapq, sorted() и list.sort().

Решение:
1) Строим maxheap (алгоритм Флойда) - корень содержит максимум
2) Переставляем корень (максимум) с последним элементом,
   уменьшаем размер кучи на 1
3) Восстанавливаем свойство maxheap через sift_down для нового корня
4) Повторяем шаги 2-3 для оставшейся кучи
В итоге массив отсортирован по возрастанию

Алгоритм inplace: дополнительный массив не нужен,
граница кучи сдвигается через параметр end


Сложность heapsort:
O(N log N) по времени - N извлечений максимума по O(log N)
O(1) по памяти - сортировка inplace, стек рекурсии не нужен


Визуализация для [4, 10, 3, 5, 1]:

Шаг 1 - строим maxheap:
  sift_down(i=1): 10 vs детей 5,1 => 10 >= 5, нет swap
  sift_down(i=0): 4 vs детей 10,3 => swap(4,10)
  => [10, 4, 3, 5, 1]
  продолжаем с i=1: 4 < 5 => swap(4,5) => [10, 5, 3, 4, 1]

Шаг 2 - извлекаем максимумы:

  end=4: swap(arr[0]=10, arr[4]=1) => [1, 5, 3, 4, | 10]
         sift_down([1,5,3,4], 0): 1 vs 5,3 => swap(1,5) => [5,1,3,4]
                                  1 vs 4 => swap(1,4) => [5,4,3,1]
         куча: [5, 4, 3, 1]

  end=3: swap(arr[0]=5, arr[3]=1) => [1, 4, 3, | 5, 10]
         sift_down([1,4,3], 0): 1 vs 4,3 => swap(1,4) => [4,1,3]
         куча: [4, 1, 3]

  end=2: swap(arr[0]=4, arr[2]=3) => [3, 1, | 4, 5, 10]
         sift_down([3,1], 0): 3 vs 1 => нет swap
         куча: [3, 1]

  end=1: swap(arr[0]=3, arr[1]=1) => [1, | 3, 4, 5, 10]
         sift_down([1], 0): нет детей

Результат: [1, 3, 4, 5, 10]
"""

import time
import random


def _sift_down_max(arr, i, end):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < end and arr[left] > arr[largest]:
            largest = left
        if right < end and arr[right] > arr[largest]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def heapsort(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        _sift_down_max(arr, i, n)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down_max(arr, 0, end)


def _mergesort(arr):
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left = _mergesort(arr[:mid])
    right = _mergesort(arr[mid:])
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


if __name__ == "__main__":
    random.seed(7)

    sizes = [1000, 5000, 10000, 50000]
    print(f"{'N':>8}  {'heapsort (s)':>14}  {'sorted (s)':>12}  {'mergesort (s)':>15}")
    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]

        a1 = arr[:]
        t0 = time.perf_counter()
        heapsort(a1)
        t_heap = time.perf_counter() - t0

        a2 = arr[:]
        t0 = time.perf_counter()
        sorted(a2)
        t_sort = time.perf_counter() - t0

        a3 = arr[:]
        t0 = time.perf_counter()
        _mergesort(a3)
        t_merge = time.perf_counter() - t0

        print(f"{n:>8}  {t_heap:>14.6f}  {t_sort:>12.6f}  {t_merge:>15.6f}")
