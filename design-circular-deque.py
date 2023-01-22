class MyCircularDeque:

    def __init__(self, k: int):
        self.maxsize = k 
        self.queue = deque([])

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.maxsize:
            self.queue.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.maxsize:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1 

    def getRear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

    def isFull(self) -> bool:
        return len(self.queue) == self.maxsize
