import math

class Stack(object):
    def __init__(self):
        self.q = []
    
    def push(self,val):
        self.q.append(val)
    
    def pop(self):
        if(self.isEmpty()):
            return None    
        return self.q.pop()

    def top(self):
        if(self.isEmpty()):
            return None    
        return self.q[-1]

    def isEmpty(self):
        return len(self.q) == 0
        
class Solution(object):
    def evalRPN(self, tokens):
        symbolData = ["+","-","*","/"]
        stack = Stack()
        for item in tokens:
            if(item not in symbolData):
                val,sign,cntPow,Idx = 0,1,0,len(item)-1
                if(item[0] == "-"):
                    sign = sign*-1
                while(Idx >= 0 and item[Idx].isdigit()):
                    val = val + (ord(item[Idx]) - ord('0')) * 10**cntPow
                    Idx,cntPow = Idx-1,cntPow+1
                stack.push(val * sign)
            else:
                if(item == "+"):
                    x,y = stack.pop(),stack.pop()
                    stack.push(y+x)

                elif(item == "-"):
                    x,y = stack.pop(),stack.pop()
                    stack.push(y-x)

                elif(item == "*"):
                    x,y = stack.pop(),stack.pop()
                    stack.push(y*x)

                elif(item == "/"):
                    x,y = stack.pop(),stack.pop()
                    res = y/x
                    if(res < 0):
                        stack.push(int(math.ceil(res)))
                    else:
                        stack.push(int(math.floor(res)))

        return stack.pop()
    
test = Solution()
print(test.evalRPN(["2","1","+","3","*"]))
print(test.evalRPN(["4","13","5","/","+"]))
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))