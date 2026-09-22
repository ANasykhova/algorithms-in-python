"""
№ 2. Validate
Проверка, могут ли последовательности pushed и popped
получиться в результате операций push/pop на пустом стеке

Решение: ~2 указателя
1) идем по pushed, кладем элементы в стек по одному
2) после каждого push проверяем: верхушка стека == popped[j]?
   Если да - снимаем со стека, j += 1, повторяем проверку
3) если в конце стек пуст - последовательность валидна,
   иначе False

Сложность:
O(n) по времени - один полный проход по pushed (внешний for делает n шагов),
    внутренний while суммарно тоже не более n (j только растёт,
    каждый элемент popped обрабатывается ровно раз, то есть не n раз по n, а 2n шагов)
    n шагов append + не более n шагов pop = 2n = O(n)
O(n) по памяти - в худшем случае весь pushed попадает в стек

Визуализация:
pushed = [1, 2, 3], popped = [3, 1, 2]

push(1): стек = [1], popped[0] = 3, 1 != 3
push(2): стек = [1, 2], popped[0] = 3, 2 != 3
push(3): стек = [1, 2, 3], popped[0] = 3, 3 == 3 => pop, j = 1
         стек = [1, 2],  popped[1] = 1, 2 != 1
конец pushed, стек не пуст => False
"""


def validate_stack_sequences(pushed: list, popped: list) -> bool:
    stack = []
    j = 0

    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    return not stack


if __name__ == "__main__":
    pushed = list(map(int, input("pushed: ").split()))
    popped = list(map(int, input("popped: ").split()))
    print(validate_stack_sequences(pushed, popped))
