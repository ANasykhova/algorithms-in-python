"""
Задача 2. Validate BST
Проверить, является ли произвольное бинарное дерево корректным BST

Идея: для каждого узла поддерживаем допустимый диапазон (min_val, max_val)
  Корень: (-inf, +inf)
  Левый потомок: (min_val, node.val)
  Правый потомок: (node.val, max_val)
Если val узла не попадает в диапазон строго - не BST

Сложность:
O(n) по времени
O(h) по памяти - стек рекурсии

Визуализация:
Корректное BST:        Некорректное дерево:
      5                       5
     / |                     / |
    3   7                   3   7
   / |                     / |
  1   4                   1   6   <- 6 > 5, нарушение верхней границы

Для узла 6: его диапазон (-inf, 3), но 6 > 3 => False
"""


class Node:
    __slots__ = ("val", "left", "right")

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node


def build_bst(values):
    bst = BST()
    for v in values:
        bst.insert(v)
    return bst.root

def validate_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (validate_bst(root.left, min_val, root.val) and
            validate_bst(root.right, root.val, max_val))


if __name__ == "__main__":
    root = build_bst([5, 3, 7, 1, 4])
    print("validate BST:", validate_bst(root))  # True
