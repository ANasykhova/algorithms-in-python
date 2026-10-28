import pytest
from solution import Node, BST, validate_bst, build_bst

# вспомогательные для создания примеров
def make_wrong_subtree():
    # узел 6 правее 3, но 6 > 5 - нарушение верхней границы
    #      5
    #     / \
    #    3   7
    #     \
    #      6
    bst = BST()
    for v in [5, 3, 7]:
        bst.insert(v)
    bst.root.left.right = Node(6)
    return bst.root


def make_deep_violation():
    # левый потомок 10 имеет значение 3, но 3 < 5
    #       5
    #        \
    #        10
    #       /
    #      3
    root = Node(5)
    root.right = Node(10)
    root.right.left = Node(3)
    return root


def make_wrong_right_subtree():
    # узел 4 левее 7, но 4 < 5 - нарушение нижней границы
    #      5
    #     / \
    #    3   7
    #       /
    #      4
    bst = BST()
    for v in [5, 3, 7]:
        bst.insert(v)
    bst.root.right.left = Node(4)
    return bst.root


def make_duplicate():
    # дубликат на левой ветке
    root = Node(5)
    root.left = Node(5)
    return root


# Граничные и базовые
@pytest.mark.parametrize("root, answer", [
    (None, True), # пустое дерево
    (Node(5), True), # один узел
    (build_bst([5, 3, 7, 1, 4]), True), # классический BST
    (build_bst([5, 3, 7]), True), # три узла
    (build_bst([1, 2, 3, 4]), True), # правая цепочка - все еще BST
    (build_bst([4, 3, 2, 1]), True), # левая цепочка - все еще BST
    (build_bst([10, 5, 15, 3, 7, 12, 20]), True), # полное дерево
])
def test_valid_bst(root, answer):
    assert validate_bst(root) is answer


# невалидные деревья
@pytest.mark.parametrize("root, answer", [
    (make_wrong_subtree(), False), # нарушение верхней границы в левом поддереве
    (make_wrong_right_subtree(), False), # нарушение нижней границы в правом поддереве
    (make_deep_violation(), False), # нарушение нижней границы на глубине
    (make_duplicate(), False), # дубликат на левой ветке
])
def test_invalid_bst(root, answer):
    assert validate_bst(root) is answer