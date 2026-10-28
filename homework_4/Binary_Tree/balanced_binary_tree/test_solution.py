import pytest
from solution import Node, BST, is_balanced, build_bst

# вспомогательные для создания примеров
def make_differs_by_one():
    # разница высот ровно 1 - все еще сбалансировано
    #      2
    #     / \
    #    1   3
    #         \
    #          4
    bst = BST()
    for v in [2, 1, 3]:
        bst.insert(v)
    bst.root.right.right = Node(4)
    return bst.root


def make_right_unbalanced():
    #     1
    #      \
    #       2
    #        \
    #         3
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    return root


def make_left_unbalanced():
    #     3
    #    /
    #   2
    #  /
    # 1
    root = Node(3)
    root.left = Node(2)
    root.left.left = Node(1)
    return root


# Граничные и базовые
@pytest.mark.parametrize("root, answer", [
    (None, True), # пустое дерево
    (Node(1), True), # один узел
    (build_bst([2, 1, 3]), True), # три узла
    (build_bst([4, 2, 6, 1, 3, 5, 7]), True), # полное дерево
    (make_differs_by_one(), True), # разница высот ровно 1
])
def test_balanced(root, answer):
    assert is_balanced(root) is answer


# несбалансированные деревья
@pytest.mark.parametrize("root, answer", [
    (build_bst([1, 2, 3]), False), # правая цепочка
    (build_bst([3, 2, 1]), False), # левая цепочка
    (make_right_unbalanced(), False), # правое поддерево глубже на 2
    (make_left_unbalanced(), False), # левое поддерево глубже на 2
])
def test_unbalanced(root, answer):
    assert is_balanced(root) is answer