from collections import deque
import sys

dq = deque([1, 2, 3])
# dq.append(4) # добавить справа
# dq.appendleft(0) # добавить слева
# print(dq)
# dq.pop() # удалить справа
# dq.popleft() # удалить слева
# print(dq)
print(sys.getsizeof(dq))

# вставка в начало → O(1)
# вставка в конец → O(1)
# удаление с начала → O(1)
# удаление с конца → O(1)

# очереди
queue = deque()
queue.append("A")
queue.append("B")
print(queue.popleft()) # A
print(queue)

# стеки
