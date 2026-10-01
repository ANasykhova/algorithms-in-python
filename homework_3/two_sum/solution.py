"""
№ 1. Two Sum
Найти индексы двух элементов массива, сумма которых равна k

Решение:
1) идем по массиву, для каждого x вычисляем resid = k - x
2) проверяем, встречался ли complement раньше (храним в словаре seen: значение => индекс)
3) если да - пара найдена, возвращаем индексы в порядке возрастания
4) иначе добавляем x в seen и идем дальше

Сложность:
O(n) по времени - один проход по массиву
O(n) по памяти - словарь seen до n записей

Визуализация:
arr = [1, 3, 4, 10], k = 7

i=0, x=1,  resid=6: seen = {}         => 6 нет, seen = {1: 0}
i=1, x=3,  resid=4: seen = {1:0}      => 4 нет, seen = {1:0, 3:1}
i=2, x=4,  resid=3: seen = {1:0,3:1}  => 3 есть (j=1) => return (1, 2)
"""


def two_sum(arr: list, k: int) -> tuple:
    seen = {}
    for i, x in enumerate(arr):
        resid = k - x
        if resid in seen:
            j = seen[resid]
            return (min(i, j), max(i, j))
        seen[x] = i


if __name__ == "__main__":
    arr = list(map(int, input("arr: ").split()))
    k = int(input("k: "))
    i, j = two_sum(arr, k)
    print(i, j)
