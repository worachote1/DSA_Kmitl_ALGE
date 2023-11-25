class Stack(object):
    def __init__(self):
        self.q = []
    def push(self,val):
        self.q.append(val)
    def pop(self):
        if(self.isEmpty()):
            return None
        return self.q.pop()
    def  top(self):
        if(self.isEmpty()):
            return None        
        return self.q[-1]
    def isEmpty(self):
        return len(self.q) == 0

class Solution(object):
    def isValid(self, s):
        openData = ["(","{","["]
        closeData = {")" : "(", "}" : "{", "]" : "["}
        stack = Stack()
        for item in s:
            if(item in openData):
                stack.push(item)
            else:
                if(closeData[item] == stack.top()):
                    stack.pop()
                else:
                    return False
        return stack.isEmpty()

test = Solution()
print(test.isValid("()"))
print(test.isValid("()[]{}"))
print(test.isValid("(]"))