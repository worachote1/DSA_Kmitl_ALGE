class Solution:
    def titleToNumber(self, columnTitle: str) :
        res = 0
        i = len(columnTitle)-1
        pos = 0
        while(i>=0):
            base_data = (26**pos)
            res += (ord(columnTitle[i])-64)*base_data
            pos+=1
            i-=1
            
        return res
test = Solution()
print(test.titleToNumber("A"))
print(test.titleToNumber("ZY"))
print(test.titleToNumber("FXSHRXW"))
print(test.titleToNumber("ABZ"))