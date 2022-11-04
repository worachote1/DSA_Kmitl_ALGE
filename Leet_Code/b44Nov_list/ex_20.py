class Stack:
    def __init__(self):
        self.q = []
    def push(self,val):
        self.q.append(val)
    def pop(self):
        return self.q.pop()
    def peek(self):
        return self.q[-1]
    def isEmpty(self):
        return len(self.q)==0

class Solution:
    def isValid(self, s: str) :
        stack = Stack()
        open_data = "([{"
        for item in s :
            if(item in open_data):
                stack.push(item)
                continue

            if(item not in open_data):
                if(stack.isEmpty()):
                    return False
                if(item == ")"):
                    if(stack.peek()=="("):
                        stack.pop()
                    else:
                        return False
                if(item == "]"):
                    if(stack.peek()=="["):
                        stack.pop()
                    else:
                        return False
                if(item == "}"):
                    if(stack.peek()=="{"):
                        stack.pop()
                    else:
                        return False
        
        return True if stack.isEmpty() else False
            