class Solution:
    def reverseWords(self, s: str) :
        res = []
        p1 = p2 = len(s)-1
        while(p1>=0):
            if(s[p1] != " "):
                p1-=1
            else:
                res.append(s[p1+1:p2+1])
                p1-=1
                p2 = p1

        res.append(s[p1+1:p2+1])
        x = []
        for item in res:
            if(item != ""):
                x.append(item)
        return " ".join(x)
        
test = Solution()
print(test.reverseWords("the sky is blue"))
print(test.reverseWords("  hello world  "))