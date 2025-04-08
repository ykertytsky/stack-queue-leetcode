from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

        

    def push(self, x: int) -> None:
        self.queue.append(x)

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        if not self.queue:
            raise IndexError("pop from an empty stack")
        return self.queue.popleft()

        

    def top(self) -> int:
        if len(self.queue) == 0:
            raise ValueError
        return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0