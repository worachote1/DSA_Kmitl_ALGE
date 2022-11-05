#Ex 394 Decode String
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
    def decodeString(self, s: str) :
        


prn = Solution()
print(prn.decodeString("3[a]2[bc]"))
print(prn.decodeString("3[a2[c]]"))
print(prn.decodeString("2[abc]3[cd]ef"))