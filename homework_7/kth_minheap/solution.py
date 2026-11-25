"""
№ 2. K-th minheap

Найти k-й наибольший элемент массива с помощью minheap.

Решение:
1) Поддерживаем minheap размером k
2) Элемент на вершине кучи - наименьший из k наибольших,
   то есть ровно k-й наибольший
3) Для каждого нового элемента: если он больше вершины -
   заменяем вершину и восстанавливаем кучу (sift_down)
4) Ответ - heap[0] после обработки всех элементов

Две реализации:
- find_kth_largest: кучу реализуем вручную
- find_kth_largest_heapq: используем модуль heapq


Построение начальной кучи занимает O(k)
При k = 1 каждое сравнение и замена занимают O(1)

Сложность find_kth_largest:
O(N log(k + 1)) по времени - проход и просеивания в куче
O(k) по памяти - храним heap размером k


Сложность find_kth_largest_heapq:
O(N log(k + 1)) по времени - проход и замены через heapreplace
O(k) по памяти - heap размером k


Визуализация для nums = [3, 2, 1, 5, 6, 4], k = 2:

Строим кучу из первых k=2 элементов:
  makeheap([3, 2]) => [2, 3]  (minheap: 2 сверху)

Обрабатываем остаток [1, 5, 6, 4]:

  nums[2] = 1: 1 <= heap[0]=2 => пропускаем
    heap = [2, 3]

  nums[3] = 5: 5 > heap[0]=2 => заменяем вершину
    heap[0] = 5 => [5, 3], sift_down => [3, 5]
    heap = [3, 5]

  nums[4] = 6: 6 > heap[0]=3 => заменяем вершину
    heap[0] = 6 => [6, 5], sift_down => [5, 6]
    heap = [5, 6]

  nums[5] = 4: 4 <= heap[0]=5 => пропускаем
    heap = [5, 6]

Ответ: heap[0] = 5
Верно: sorted([3,2,1,5,6,4]) = [1,2,3,4,5,6], 2-й наибольший = 5
"""

import heapq


def _sift_down(arr, i, n):
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def _makeheap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        _sift_down(arr, i, n)
    return arr


def find_kth_largest(nums, k):
    heap = _makeheap(nums[:k])
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heap[0] = nums[i]
            _sift_down(heap, 0, k)
    return heap[0]


def find_kth_largest_heapq(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heapreplace(heap, nums[i])
    return heap[0]


if __name__ == "__main__":
    nums = list(map(int, input("Массив: ").split()))
    k = int(input("k: "))
    print("Ручная куча:", find_kth_largest(nums, k))
    print("heapq:      ", find_kth_largest_heapq(nums, k))
