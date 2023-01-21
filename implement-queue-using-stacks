class MyQueue:
    def __init__(self):
        self.stack_primary = []
        self.stack_helper = [] 

    def push(self, x: int) -> None:
        self.stack_primary.append(x) 

    def pop(self) -> int:
        while len(self.stack_primary) != 1:
            self.stack_helper.append(self.stack_primary.pop())
        front = self.stack_primary.pop()
        while self.stack_helper: 
            self.stack_primary.append(self.stack_helper.pop())
        return front 

    def peek(self) -> int:
        return self.stack_primary[0]
        
    def empty(self) -> bool:
        return len(self.stack_primary) == 0
