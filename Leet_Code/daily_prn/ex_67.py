class Stack:
    def __init__(self) :
        self.q = []
    def push(self,val):
        self.q.append(val)
    def pop(self):
        return self.q.pop()
    def isEmpty(self):
        return len(self.q)==0
                
class Solution:
    def addBinary(self, a: str, b: str) :
        ss_res = ""
        a_stack = Stack()
        b_stack = Stack()
        for i in range(len(a)):
            a_stack.push(int(a[i]))
        for i in range(len(b)):
            b_stack.push(int(b[i]))
        carry = 0
        while(True):
            if(a_stack.isEmpty() and b_stack.isEmpty()):
                break
            if(not a_stack.isEmpty()):
                carry += a_stack.pop()
            
            if(not b_stack.isEmpty()):
                carry += b_stack.pop()
            
            ss_res += str(carry % 2)
            carry = carry//2
        
        return "1"+ss_res[::-1] if carry==1 else ss_res[::-1]

test = Solution()
print(test.addBinary("11","1"))
print(test.addBinary("1010","1011"))
        