import pytest
from solution import ListNode, merge_with_dummy, merge_without_dummy


# Вспомогательные, авто создание списка из обычного массива
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

# Оба способа проверяем на одних и тех же кейсах
@pytest.fixture(params=[merge_with_dummy, merge_without_dummy])
def merge_fn(request):
    return request.param


# Граничный - один или оба списка пусты
@pytest.mark.parametrize("l1, l2, answer", [
    ([], [], []),
    ([1, 2, 3], [], [1, 2, 3]),
    ([], [1, 2, 3], [1, 2, 3]),
])
def test_empty_lists(merge_fn, l1, l2, answer):
    assert to_list(merge_fn(to_linked(l1), to_linked(l2))) == answer

# Граничный - из одного элемента
@pytest.mark.parametrize("l1, l2, answer", [
    ([42], [], [42]),                    # l1 один элемент, l2 пустой
    ([], [42], [42]),                    # l2 один элемент, l1 пустой
    ([5], [5], [5, 5]),                  # оба по одному, равные
])
def test_empty_lists(merge_fn, l1, l2, answer):
    assert to_list(merge_fn(to_linked(l1), to_linked(l2))) == answer

# Базовые
@pytest.mark.parametrize("l1, l2, answer", [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]), # простое пересечение
    ([2, 4, 6], [1, 3, 5], [1, 2, 3, 4, 5, 6]),
    ([1], [2, 3, 4], [1, 2, 3, 4]), # первый полностью до второго
    ([2, 3, 4], [1], [1, 2, 3, 4]), # второй полностью до первого
    ([3], [1, 2, 4], [1, 2, 3, 4]), # один полностью внутри другого
    ([1, 2, 4], [3], [1, 2, 3, 4]),
    ([1, 2, 3, 4], [1], [1, 1, 2, 3, 4]), # одинаковые первые элементы
    ([1], [1, 2, 3, 4], [1, 1, 2, 3, 4]),
    ([1, 2, 3], [1, 1, 3, 4], [1, 1, 1, 2, 3, 3, 4]), # дубликаты в обоих списках
    ([1, 2, 4], [3, 4, 4], [1, 2, 3, 4, 4, 4]), # одинаковые последние элементы
    ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),  # все элементы равны
    ([-3, -1, 2], [-2, 0, 3], [-3, -2, -1, 0, 2, 3]),  # Отрицательные числа
    ([-5, -3], [-4, -2, 0], [-5, -4, -3, -2, 0]),
    # они по сути проверены, но еще раз закрепим
    ([1, 2, 4, 10], [3, 4, 5, 11, 12, 13], [1, 2, 3, 4, 4, 5, 10, 11, 12, 13]), # длинный хвост второго
    ([3, 4, 5, 11, 12, 13], [1, 2, 4, 10], [1, 2, 3, 4, 4, 5, 10, 11, 12, 13]), # длинный хвост первого
])
def test_various(merge_fn, l1, l2, answer):
    assert to_list(merge_fn(to_linked(l1), to_linked(l2))) == answer
