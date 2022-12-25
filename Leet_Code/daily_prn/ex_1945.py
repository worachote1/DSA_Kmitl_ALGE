class Solution:
    def getLucky(self, s: str, k: int):
        ss = ""
        for item in s:
            ss += str(ord(item)-96)
        
        sumNum = 0
        for i in range(k):
            for item in ss:
                sumNum += int(item)
            ss = str(sumNum)
            sumNum = 0

        return int(ss)

test = Solution()

print(test.getLucky("leetcode",2))
print(test.getLucky("zbax",2))