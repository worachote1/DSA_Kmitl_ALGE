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
        ss = ""
        num = 0
        stack = Stack()
        for item in s:
            if(item.isdigit()):
                num = 10*num + int(item)
                continue
            if(item=="["):
                stack.push(num)
                stack.push(ss)
                num = 0
                ss = ""
                continue
            if(item=="]"):
                prev_ss = stack.pop()
                prev_num = stack.pop()
                ss = prev_ss + prev_num*ss
                continue
            else:
                ss += item
        return ss

prn = Solution()
print(prn.decodeString("3[a]2[bc]"))
print(prn.decodeString("3[a2[c]]"))
print(prn.decodeString("2[abc]3[cd]ef"))