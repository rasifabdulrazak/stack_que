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
    
    
def bracket_pairs(pair:str):
    stack = []
    inbiult = {"[":"]","{":"}","(":")"}
    for i in pair:
        if i in inbiult:
            stack.append(i)
        elif i in inbiult.values():
            if not stack or inbiult[stack.pop()] != i:
                return False
    return not stack

print(bracket_pairs("(([]))"))


class MinStack:
    
    def __init__(self):
        self.stack = []
        
    def push(self,val:int):
        if not self.stack:
            self.stack.append([val,val])
        else:
            self.stack.append([val,min(val,self.stack[-1][1])])
            
    def pop(self):
        pop = self.stack.pop()
        
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]
    

# Remove Outermost Parentheses
def remove_outermost_paranthesis(s:str):
    stack = []
    ans = ""
    
    for i in s:
        if i == "(":
            stack.append(i)
            if len(stack) > 1:
                ans += i
        else:
            if len(stack) > 1:
                ans += i
            stack.pop()
            
    return ans

print(remove_outermost_paranthesis("(()())(())"))

def remove_outermost_without_stack(s:str):
    ans = ""
    level = 0
    
    for i in s:
        if i == "(":
            level += 1
            if level > 1:
                ans += i
            
        else:
            if level > 1:
                ans += i
            level -= 1
    return ans
  
print(remove_outermost_without_stack("(()())(())"))
            
    
    
    