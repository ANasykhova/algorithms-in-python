import pytest
from solution import BST


# Граничные случаи: пустое дерево
@pytest.mark.parametrize("method", [
    "preorder", "inorder", "postorder",
    "reverse_preorder", "reverse_inorder", "reverse_postorder",
])
def test_empty_tree(method):
    bst = BST()
    assert getattr(bst, method)() == []

# Граничные случаи: один узел
@pytest.mark.parametrize("method", [
    "preorder", "inorder", "postorder",
    "reverse_preorder", "reverse_inorder", "reverse_postorder",
])
def test_single_node(method):
    bst = BST()
    bst.insert(42)
    assert getattr(bst, method)() == [42]


# База: все шесть обходов на эталонном дереве
@pytest.mark.parametrize("method, expected", [
    ("preorder", [5, 3, 1, 4, 7]),
    ("inorder", [1, 3, 4, 5, 7]),
    ("postorder", [1, 4, 3, 7, 5]),
    ("reverse_preorder", [5, 7, 3, 4, 1]),
    ("reverse_inorder", [7, 5, 4, 3, 1]),
    ("reverse_postorder", [7, 4, 1, 3, 5]),
])
def test_six_traversals(method, expected):
    bst = BST()
    for v in [5, 3, 7, 1, 4]:
        bst.insert(v)
    assert getattr(bst, method)() == expected


@pytest.mark.parametrize("values, answer", [
    ([10, 5, 15, 3, 7, 12, 20], [3, 5, 7, 10, 12, 15, 20]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
])
def test_inorder_gives_sorted_sequence(values, answer):
    bst = BST()
    for v in values:
        bst.insert(v)
    assert bst.inorder() == answer


@pytest.mark.parametrize("values, answer", [
    ([10, 5, 15, 3, 7, 12, 20], [20, 15, 12, 10, 7, 5, 3]),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
])
def test_reverse_inorder_gives_descending(values, answer):
    bst = BST()
    for v in values:
        bst.insert(v)
    assert bst.reverse_inorder() == answer


@pytest.mark.parametrize("values, method, answer", [
    ([1, 2, 3, 4], "inorder", [1, 2, 3, 4]),
    ([1, 2, 3, 4], "preorder", [1, 2, 3, 4]),
    ([1, 2, 3, 4], "postorder", [4, 3, 2, 1]),
    ([4, 3, 2, 1], "inorder", [1, 2, 3, 4]),
    ([4, 3, 2, 1], "preorder", [4, 3, 2, 1]),
    ([4, 3, 2, 1], "postorder", [1, 2, 3, 4]),
])
def test_degenerate_chains(values, method, answer):
    bst = BST()
    for v in values:
        bst.insert(v)
    assert getattr(bst, method)() == answer
