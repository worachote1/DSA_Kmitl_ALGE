class Solution:
    def romanToInt(self, s: str) :
        data = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sumNum = 0
        n = len(s)
        if(n==1):
            return data[s]
        Lp,Rp = 0,1
        while(Lp < n and Rp < n):

            if(data[s[Lp]]<data[s[Rp]]):
                sumNum += data[s[Rp]]-data[s[Lp]]
                Lp = Rp+1
                Rp = Lp+1
               # print("sd")
            else :
                sumNum += data[s[Lp]]
                Lp = Rp
                Rp = Lp+1
               # print("ASDf")            
        if(Lp >= n):
            return sumNum
        return sumNum + data[s[Lp]]

test = Solution()
print(test.romanToInt("XCI"))
print(test.romanToInt("III"))
print(test.romanToInt("LVIII"))
print(test.romanToInt("MCMXCIV"))