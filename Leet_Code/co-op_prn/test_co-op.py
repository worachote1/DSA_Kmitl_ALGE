import math
class Stack :
    def __init__(self) :
        self.q = []
    def push(self,val):
        self.q.append(val)
    def pop(self):
        return self.q.pop()
    def isEmpty(self):
        return len(self.q)==0
    def size(self):
        return len(self.q)

class Solution:
    def evalRPN(self, tokens: list[str]) :
        data = Stack()
        
        for item in tokens:
            if(item.isdigit()):
                data.push(int(item))
            if((len(item)>1 and item[0]=="-")):
                data.push(-1*int(item[1:]))

            if(item=="+"):
                    x = data.pop()
                    y = data.pop()
                    data.push(y+x)
              
            elif(item=="-"):
                    x = data.pop()
                    y = data.pop()
                    data.push(y-x)
            elif(item=="*"):
                    x = data.pop()
                    y = data.pop()
                    data.push(x*y)
            elif(item=="/"):
                    x = data.pop()
                    y = data.pop()
                    res = y/x
                    if(res<0):
                        res = int(math.ceil(res))
                    else :
                        res = int(math.floor(res))
                    data.push(res)                       
        return data.pop()
    
test = Solution()
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))