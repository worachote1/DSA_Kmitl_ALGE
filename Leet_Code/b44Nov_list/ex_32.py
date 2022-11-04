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
    def longestValidParentheses(self, s: str):
        count_res = 0
        stack = Stack()
    
        for i in range(len(s)):
            if(s[i] == "("):
                stack.push(i)
                
            elif(s[i]==")"):
                if(stack.isEmpty()):
                    stack.push(i)
                    
                elif(s[stack.peek()]=="("):
                    stack.pop()
                else:
                    stack.push(i)
        
        if(stack.isEmpty()):
            count_res = len(s)
            return count_res

        n = len(s)
        while(not stack.isEmpty()):
            top = stack.pop()
            count_res = max(count_res,n-top-1)
            n = top

        #test in case only left side idx in stack
        count_res = max(count_res,n)

        return count_res