# Stack
# =========
# FIFO
# enque
# deque

# Queue
# =======
# LIFO
# push
# pop


# Implement stack operations using que
class MyStack:
    
    def __init__(self):
        self.q = []
        
    def push(self,x:int):
        self.q.append(x)
        
    def pop(self):
        for _ in range(len(self.q)-1):
            self.q.append(self.q.pop(0))
        return self.q.pop(0)
    
    def top(self):
        for _ in range(len(self.q)-1):
            self.q.append(self.q.pop(0))
        top = self.q.pop(0)
        self.q.append(top)
        return top
    
    def isEmpty(self):
        return len(self.q) == 0
    
# Implement que using stack
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[len(self.stack2)-1]
    
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2)==0 