import pytest
from solution import AVL


def is_avl_balanced(node):
    """Проверяет, что для каждого узла |bf| <= 1."""
    if node is None:
        return True
    lh = node.left.height if node.left else 0
    rh = node.right.height if node.right else 0
    if abs(lh - rh) > 1:
        return False
    return is_avl_balanced(node.left) and is_avl_balanced(node.right)


def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    """Проверяет корректность BST-свойства."""
    if node is None:
        return True
    if not (min_val < node.val < max_val):
        return False
    return (is_bst(node.left, min_val, node.val) and
            is_bst(node.right, node.val, max_val))


# Вставка: inorder дает отсортированный результат
@pytest.mark.parametrize("values, answer", [
    ([1], [1]),                                              # один узел
    ([3, 1, 2], [1, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),                    # правая цепочка — триггер RR
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),                    # левая цепочка — триггер LL
    ([1, 3, 2], [1, 2, 3]),                                  # триггер RL
    ([3, 1, 2], [1, 2, 3]),                                  # триггер LR
    ([3, 1, 4, 1, 5, 9, 2, 6], [1, 2, 3, 4, 5, 6, 9]),    # дубликат 1 игнорируется
    ([5, 5, 5], [5]),                                        # все элементы одинаковые
])
def test_insert_inorder(values, answer):
    avl = AVL()
    for v in values:
        avl.insert(v)
    assert avl.inorder() == answer


# Вставка: дерево остается сбалансированным
@pytest.mark.parametrize("values", [
    [1, 2, 3],
    [3, 2, 1],
    [1, 3, 2],
    [3, 1, 2],
    [5, 3, 7, 1, 4, 6, 8],
    [1, 2, 3, 4, 5, 6, 7],
    [7, 6, 5, 4, 3, 2, 1],
])
def test_insert_stays_balanced(values):
    avl = AVL()
    for v in values:
        avl.insert(v)
    assert is_avl_balanced(avl.root)
    assert is_bst(avl.root)


# Удаление: корректный inorder после удаления
@pytest.mark.parametrize("values, delete_val, answer", [
    ([], 1, []),                                             # удаление из пустого дерева
    ([1], 1, []),                                            # удаление единственного узла
    ([1, 2], 1, [2]),                                        # удаление корня, остается правый
    ([2, 1], 2, [1]),                                        # удаление корня, остается левый
    ([5, 3, 7], 3, [5, 7]),                                  # удаление листа
    ([5, 3, 7, 1], 3, [1, 5, 7]),                           # удаление узла с одним потомком
    ([1, 2, 3], 2, [1, 3]),                                  # удаление узла с двумя потомками
    ([3, 1, 2], 3, [1, 2]),                                  # удаление корня
    ([5, 3, 7, 1, 4, 6, 8], 5, [1, 3, 4, 6, 7, 8]),        # удаление корня с двумя потомками
    ([1, 2], 99, [1, 2]),                                    # удаление несуществующего
])
def test_delete_inorder(values, delete_val, answer):
    avl = AVL()
    for v in values:
        avl.insert(v)
    avl.delete(delete_val)
    assert avl.inorder() == answer


# Удаление: дерево остается сбалансированным
@pytest.mark.parametrize("values, delete_val", [
    ([1, 2, 3], 2),
    ([5, 3, 7, 1, 4, 6, 8], 5),
    ([1, 2, 3, 4, 5], 3),
    ([7, 6, 5, 4, 3, 2, 1], 4),
])
def test_delete_stays_balanced(values, delete_val):
    avl = AVL()
    for v in values:
        avl.insert(v)
    avl.delete(delete_val)
    assert is_avl_balanced(avl.root)
    assert is_bst(avl.root)


# Поиск
@pytest.mark.parametrize("values, search_val, answer", [
    ([], 1, False),
    ([1], 1, True),
    ([1], 2, False),
    ([5, 3, 7, 1, 4, 6, 8], 4, True),
    ([5, 3, 7, 1, 4, 6, 8], 9, False),
    ([1, 2, 3, 4, 5], 5, True),
    ([1, 2, 3, 4, 5], 0, False),
    ([5, 3, 7, 1, 4, 6, 8], 1, True),  # крайний левый
    ([5, 3, 7, 1, 4, 6, 8], 8, True),  # крайний правый
])
def test_search(values, search_val, answer):
    avl = AVL()
    for v in values:
        avl.insert(v)
    assert avl.search(search_val) is answer