"""
№ 3. Merge Lists
Слияние двух отсортированных связных списков двумя способами

Решение (с фиктивным узлом):
1) создаем dummy-узел, current указывает на него
2) на каждом шаге цепляем меньший из двух текущих узлов
3) когда один список кончился - цепляем хвост другого
4) возвращаем dummy.next

Решение (без фиктивного узла):
1) выбираем голову результата: берем меньший из list1.val и list2.val
2) дальше тот же цикл сравнения
3) цепляем остаток

Сложность (с фиктивным узлом):
O(n + m) по времени - один проход по обоим спискам, на каждом шаге берём один узел
O(1) по памяти - один доп. узел (dummy), перелинковка без новых узлов

Сложность (без фиктивного узла):
O(n + m) по времени - то же самое, только голова выбирается отдельно до цикла
O(1) по памяти - даже dummy нет, только перелинковка

Визуализация:
list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4

Шаг 1: 1 <= 1 => list1 => [1],     list1 = 2 -> 4
Шаг 2: 1 <= 2 => list2 => [1, 1],  list2 = 3 -> 4
Шаг 3: 2 <= 3 => list1 => [1,1,2], list1 = 4
Шаг 4: 3 <= 4 => list2 => [1,1,2,3], list2 = 4
Шаг 5: 4 <= 4 => list1 => [1,1,2,3,4], list1 = None
list1 кончился, цепляем list2: [1, 1, 2, 3, 4, 4]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_with_dummy(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return dummy.next # убираем фиктивный узел


def merge_without_dummy(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    # выбираем голову
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return head


if __name__ == "__main__":
    def to_linked(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        cur = head
        for val in lst[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head

    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    l1 = to_linked(list(map(int, input("list1: ").split())))
    l2 = to_linked(list(map(int, input("list2: ").split())))
    print(to_list(merge_with_dummy(l1, l2)))
