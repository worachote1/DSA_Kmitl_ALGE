class Stack(object):
    def __init__(self):
        self.q = []
    def push(self,val):
        self.q.append(val)
    def pop(self):
        val = self.q.pop()
        return val
    def top(self):
        if(not len(self.q)):
            return None
        return self.q[-1]

class Solution(object):
    def decodeString(self, s):
        res_ss = ""
        stack = Stack()
        for item in s:
            if(item != ']'):
                stack.push(item)
            else:
                ss = ""
                while(stack.top() and not stack.top().isdigit()):
                    temp = stack.pop()
                    if(temp != "["):
                        ss += temp
                ss_num,powNum = 0,0
                while(stack.top() and stack.top().isdigit()):
                    ss_num += (ord(stack.pop()) - ord('0')) * 10**powNum
                    powNum += 1
                ss = ss*ss_num
                for item in ss[::-1]:
                    stack.push(item)
        for item in stack.q:
            res_ss += item
        return res_ss
        
test = Solution()
print(test.decodeString("3[a]2[bc]"))
print(test.decodeString("3[a2[c]]"))
print(test.decodeString("2[abc]3[cd]ef"))