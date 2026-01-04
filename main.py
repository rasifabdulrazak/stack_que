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