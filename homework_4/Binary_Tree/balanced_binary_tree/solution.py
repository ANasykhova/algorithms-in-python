"""
Задача 3. Balanced Binary Tree
Дерево сбалансировано, если для каждого узла |height(left) - height(right)| <= 1

Идея: считаем высоту снизу вверх. Если на каком-то уровне разница высот > 1,
возвращаем -1 как сигнал «не сбалансировано». Это позволяет прерваться
раньше, не обходя все дерево.

Сложность:
O(n) по времени - каждый узел посещается ровно раз
O(h) по памяти - стек рекурсии

Визуализация:

Сбалансированное:    Несбалансированное:
      3                     1
     /  |                    |
    9  20                     2
      /  |                     |
     15   7                     3

height(9)=0, height(20)=1, |0-1|=1 => OK
height(1): правое поддерево высоты 2, левое 0, |0-2|=2 => False
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

def _check_height(node):
    if node is None:
        return 0
    left = _check_height(node.left)
    if left == -1:
        return -1
    right = _check_height(node.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return max(left, right) + 1

def is_balanced(root):
    return _check_height(root) != -1


if __name__ == "__main__":
    root = build_bst([4, 2, 6, 1, 3, 5, 7])
    print("is balanced:", is_balanced(root))  # True
