"""
№ 3. AVL Tree
Самобалансирующееся бинарное дерево поиска

В каждом узле хранится высота поддерева. После вставки и удаления
пересчитываем высоты и при необходимости выполняем повороты

Балансовый фактор (bf) = height(left) - height(right):
  bf > 1 - левое поддерево тяжелее <- правый поворот (или лево-правый)
  bf < -1 - правое поддерево тяжелее -> левый поворот (или право-левый)

Четыре случая разбалансировки:
  LL (Left-Left):   правый поворот вокруг узла
  RR (Right-Right): левый поворот вокруг узла
  LR (Left-Right):  левый поворот вокруг левого потомка, затем правый
  RL (Right-Left):  правый поворот вокруг правого потомка, затем левый

Визуализация LL-поворота (вставка 3, 2, 1):

  Вставили 1:          Дисбаланс:       После правого поворота:
      3                   3                    2
     /                   /                   /    \
    2          →        2           →        1     3
   /                   /
  1                   1   (bf=2)

Сложность:
O(log n) по времени вставка, удаление, поиск
O(log n) по памяти - глубина стека рекурсии
"""


class Node:
    __slots__ = ("val", "left", "right", "height")

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    # вспомогательные методы
    def _height(self, node):
        return node.height if node else 0

    def _bf(self, node):
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2
        self._update_height(x)
        self._update_height(y)
        return y

    def _rebalance(self, node):
        self._update_height(node)
        bf = self._bf(node)

        if bf > 1:
            if self._bf(node.left) < 0:  # Left-Right
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if bf < -1:
            if self._bf(node.right) > 0:  # Right-Left
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # внешний доступ
    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node  # дубликат - игнорируем
        return self._rebalance(node)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # два потомка: заменяем на минимум правого поддерева
            successor = node.right
            while successor.left:
                successor = successor.left
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return self._rebalance(node)

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

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

    def display(self):
        self._display(self.root, "", True)

    def _display(self, node, prefix, is_left):
        if node is None:
            return
        connector = "└── " if is_left else "┌── "
        extension = "    " if is_left else "│   "
        if node.right:
            self._display(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + connector + str(node.val) + f" (h={node.height})")
        if node.left:
            self._display(node.left, prefix + extension, True)


if __name__ == "__main__":
    avl = AVL()
    values = list(map(int, input("Вставить значения: ").split()))
    for v in values:
        avl.insert(v)
        print(f"\nВставлено {v}:")
        avl.display()

    search_val = int(input("\nНайти значение: "))
    print("Найдено:", avl.search(search_val))

    del_val = int(input("Удалить значение: "))
    avl.delete(del_val)
    print(f"\nПосле удаления {del_val}:")
    avl.display()
