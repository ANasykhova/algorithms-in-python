"""
Задача 1. Tree Traversal
BST с операцией вставки и шестью обходами

Узел BST: val, left, right
Вставка: если val < node.val - идем влево, иначе вправо

Обходы (рекурсия):
  preorder: корень => лево => право
  inorder: лево => корень => право  (возрастающая последовательность)
  postorder: лево => право => корень
  reverse preorder: корень => право => лево
  reverse inorder: право => корень => лево  (убывающая последовательность)
  reverse postorder: право => лево => корень

Сложность вставки: O(h) по времени, O(1) по памяти (итеративно), где h - высота дерева
в среднем O(log n), в худшем (вырожденное) O(n)

Сложность каждого обхода: O(n) по времени, O(h) по памяти (стек рекурсии)

Визуализация вставки [5, 3, 7, 1, 4]:
        5
       / \
      3   7
     / \
    1   4
preorder: [5, 3, 1, 4, 7]
inorder: [1, 3, 4, 5, 7]
postorder: [1, 4, 3, 7, 5]
reverse preorder: [5, 7, 3, 4, 1]
reverse inorder: [7, 5, 4, 3, 1]
reverse postorder: [7, 4, 1, 3, 5]
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

    # обертка, чтобы снаружи передавать только значение, а корень подтягивался автоматически
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

    def preorder(self):
        result = []
        # вспомогательные, чтобы снаружи вызывать метод без передачи корня
        def _walk(node):
            if node is None:
                return
            result.append(node.val)
            _walk(node.left)
            _walk(node.right)
        _walk(self.root)
        return result

    def inorder(self):
        result = []
        def _walk(node):
            if node is None:
                return
            _walk(node.left)
            result.append(node.val)
            _walk(node.right)
        _walk(self.root)
        return result

    def postorder(self):
        result = []
        def _walk(node):
            if node is None:
                return
            _walk(node.left)
            _walk(node.right)
            result.append(node.val)
        _walk(self.root)
        return result

    def reverse_preorder(self):
        result = []
        def _walk(node):
            if node is None:
                return
            result.append(node.val)
            _walk(node.right)
            _walk(node.left)
        _walk(self.root)
        return result

    def reverse_inorder(self):
        result = []
        def _walk(node):
            if node is None:
                return
            _walk(node.right)
            result.append(node.val)
            _walk(node.left)
        _walk(self.root)
        return result

    def reverse_postorder(self):
        result = []
        def _walk(node):
            if node is None:
                return
            _walk(node.right)
            _walk(node.left)
            result.append(node.val)
        _walk(self.root)
        return result


if __name__ == "__main__":
    values = list(map(int, input().split()))
    bst = BST()
    for v in values:
        bst.insert(v)
    print("preorder: ", bst.preorder())
    print("inorder: ", bst.inorder())
    print("postorder: ", bst.postorder())
    print("reverse preorder: ", bst.reverse_preorder())
    print("reverse inorder: ", bst.reverse_inorder())
    print("reverse postorder: ", bst.reverse_postorder())
