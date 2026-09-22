"""
№ 1. Stack vs Queue
Реализация стека (LIFO) и очереди (FIFO) на основе связных списков

Решение:
1) Node - узел с полями value и next
2) Stack (LIFO):
   push: новый узел становится головой
   pop: снимаем голову, голова сдвигается на head.next
3) Queue (FIFO):
   enqueue: новый узел прицепляется к хвосту
   dequeue: снимаем голову, если список пустеет - обнуляем хвост
   храним ссылки на голову и хвост => enqueue и dequeue за O(1)

Сложность Stack:
    push - O(1) по времени - меняем только head, O(1) доп. память
    pop - O(1) по времени - снимаем только head, O(1) доп. память
    peek - O(1) по времени - читаем только head, O(1) доп. память
    O(n) по памяти - под n элементов

Сложность Queue:
    enqueue - O(1) по времени - пишем только в tail, O(1) доп. память
    dequeue - O(1) по времени - снимаем только head, O(1) доп. память
    peek - O(1) по времени - читаем только head, O(1) доп. память
    O(n) по памяти - под n элементов

Визуализация:
Stack: push(1), push(2), push(3), pop()
push(1): head -> 1 -> None
push(2): head -> 2 -> 1 -> None
push(3): head -> 3 -> 2 -> 1 -> None
pop(): 3, head -> 2 -> 1 -> None

Queue: enqueue(1), enqueue(2), enqueue(3), dequeue()
enqueue(1): head -> 1 <- tail
enqueue(2): head -> 1 -> 2 <- tail
enqueue(3): head -> 1 -> 2 -> 3 <- tail
dequeue(): 1, head -> 2 -> 3 <- tail
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self.head.value

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self.head.value

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size


if __name__ == "__main__":
    s = Stack()
    for v in map(int, input("Stack push: ").split()):
        s.push(v)
    print("Stack pop:", [s.pop() for _ in range(len(s))])

    q = Queue()
    for v in map(int, input("Queue enqueue: ").split()):
        q.enqueue(v)
    print("Queue dequeue:", [q.dequeue() for _ in range(len(q))])
