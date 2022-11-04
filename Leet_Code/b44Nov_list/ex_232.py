# 232. Implement Queue using Stacks
class MyQueue:
    
    def __init__(self):
        self.q = []

    def push(self, x: int):
        self.q.append(x)

    def pop(self) :
        return self.q.pop(0)

    def peek(self) :
        return self.q[0]

    def empty(self) :
        return len(self.q)==0        