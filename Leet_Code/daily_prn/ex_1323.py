class Solution:
    def maximum69Number (self, num: int) -> int:
        ss = [item for item in str(num)]
        res = []
        maxNum = 0
        for i in range(len(ss)):
            if(ss[i]==9):
                continue
            temp = ss[i]
            ss[i] = "9"
            ss_toInt = int("".join(ss))
            if(ss_toInt>maxNum):
                maxNum = ss_toInt
                res = [item for item in ss] 
            ss[i]=temp
        
        return int("".join(res))