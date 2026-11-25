r"""
№ 1. Makeheap

Преобразовать произвольный массив в minheap двумя способами:
1) за O(N log N) - вставка по одному с sift_up
2) за O(N) - алгоритм Флойда (sift_down с конца)


Решение:
1) makeheap_n_log_n: считаем, что arr[0] уже образует кучу из 1 элемента,
   затем вставляем arr[1], ..., arr[n-1] по очереди с sift_up
2) makeheap: все листья (индексы n//2 ... n-1) уже являются корректными
   кучами размером 1, поэтому вызываем sift_down только для внутренних узлов
   с индекса (n-2)//2 до 0 включительно

Доказательство O(N) для makeheap:
Высота узла - число ребер самого длинного пути от него до листа
Просеивание из узла высоты h делает не более h обменов

Пронумеруем узлы от 1 до N только для подсчета
У узла i самый левый потомок на j уровней ниже имеет номер i * 2**j
Такой потомок есть, если i * 2**j <= N
Значит, высоту хотя бы j имеют ровно N // 2**j узлов

Считаем сумму высот по уровням: каждый узел высоты h учитываем
по одному разу для j от 1 до h
S = N // 2 + N // 4 + N // 8 + ...
S <= N * (1/2 + 1/4 + 1/8 + ...) = N

Каждый обмен и завершающая проверка занимают O(1)
Проверок после последнего обмена не больше числа вызовов sift_down
Копирование массива и обход внутренних узлов занимают O(N)
Итого O(N) по времени


Сложность makeheap_n_log_n:
O(N log N) по времени - N вставок с sift_up по O(log N)
O(N) по памяти - копия входного массива


Сложность makeheap:
O(N) по времени - сумма высот всех узлов равна O(N)
O(N) по памяти - копия входного массива


Визуализация makeheap для [9, 4, 7, 1, 8, 3, 2]:

Исходное дерево (индексы 0..6):
         9(0)
        /    \
      4(1)   7(2)
      / \    / \
    1(3) 8(4) 3(5) 2(6)

Листья: 1,8,3,2 (индексы 3..6) - уже готовы
Начинаем с i = (7-2)//2 = 2

sift_down(i=2): узел 7, дети 3(i=5) и 2(i=6)
  min-ребенок = 2 (i=6) < 7 => swap(7, 2)
         9
        / \
       4   2
      / \ / \
     1  8 3  7

sift_down(i=1): узел 4, дети 1(i=3) и 8(i=4)
  min-ребенок = 1 (i=3) < 4 => swap(4, 1)
         9
        / \
       1   2
      / \ / \
     4  8 3  7

sift_down(i=0): узел 9, дети 1(i=1) и 2(i=2)
  min-ребенок = 1 (i=1) < 9 => swap(9, 1)
         1
        / \
       9   2
      / \ / \
     4  8 3  7
  продолжаем: узел 9 (теперь i=1), дети 4(i=3) и 8(i=4)
  min-ребенок = 4 < 9 => swap(9, 4)
         1
        / \
       4   2
      / \ / \
     9  8 3  7

Результат: [1, 4, 2, 9, 8, 3, 7]
Проверка: каждый родитель <= детей - валидный minheap
"""

import time


def _sift_up(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[parent] > arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
        else:
            break


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


def makeheap_n_log_n(arr):
    arr = list(arr)
    for i in range(1, len(arr)):
        _sift_up(arr, i)
    return arr


def makeheap(arr):
    arr = list(arr)
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        _sift_down(arr, i, n)
    return arr


def _is_minheap(arr):
    n = len(arr)
    for i in range(n):
        if 2 * i + 1 < n and arr[2 * i + 1] < arr[i]:
            return False
        if 2 * i + 2 < n and arr[2 * i + 2] < arr[i]:
            return False
    return True


if __name__ == "__main__":
    import random
    random.seed(7)
    sizes = [1000, 10000, 100000, 1000000]
    print(f"{'N':>10}  {'n_log_n (s)':>13}  {'floyd (s)':>11}  {'speedup':>8}")
    for n in sizes:
        arr = [random.randint(1, 1000000) for _ in range(n)]

        t0 = time.perf_counter()
        makeheap_n_log_n(arr)
        t1 = time.perf_counter() - t0

        t0 = time.perf_counter()
        makeheap(arr)
        t2 = time.perf_counter() - t0

        print(f"{n:>10}  {t1:>13.6f}  {t2:>11.6f}  {t1/t2:>7.2f}x")
