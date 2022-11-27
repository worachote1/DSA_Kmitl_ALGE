class Stack :
    def __init__(self) :
        self.q = []
    def push(self,val : int):
        self.q.append(val)
    def pop(self):
        return self.q.pop()
    def peek(self):
        return self.q[-1]
    def isEmpty(self):
        return len(self.q)==0

class Solution:
    def calPoints(self, operations: list[str]):
        data = Stack()
        for item in operations:
            if(item.isdigit() or item[1:].isdigit()):
                data.push(int(item))
            elif(item == "C"):
                data.pop()
            elif(item == "D"):
                data.push(data.peek()*2)
            elif(item == "+"):
                pop_firstVal = data.pop()
                pop_secondVal = data.pop()
                x = pop_firstVal + pop_secondVal
                data.push(pop_secondVal)
                data.push(pop_firstVal)
                data.push(x)
        return sum(data.q) if not data.isEmpty() else 0

test = Solution()
print(test.calPoints(["5","2","C","D","+"]))
print(test.calPoints(["1","C"]))