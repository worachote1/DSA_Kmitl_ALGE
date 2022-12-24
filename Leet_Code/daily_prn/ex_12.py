class Solution:
    def intToRoman(self, num: int) :
       #data = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        data = {"M" : 1000,"CM" : 900 ,"D" : 500,"CD" : 400,"C" : 100,"XC" : 90,"L" :50,"XL" : 40 ,"X" : 10,"IX" : 9 ,"V" : 5,"IV" : 4,"I" : 1}
        res = ""
        for item in data:
            while(num >= data[item]):
                res = res + item
                num -= data[item]
        return res

test = Solution()
print(test.intToRoman(3))
print(test.intToRoman(58))
print(test.intToRoman(1994))