class Solution:
    def dayOfYear(self, date: str) :

        data_year = int(date[0:3+1])
        data_month = int(date[5:6+1]) if date[5] != "0" else int(date[6])
        data_day = int(date[8:9+1]) if date[8] != "0" else int(date[9])

        day_of_month = [
            31,28,31,30,31,30,31,31,30,31,30,31
        ]
        if(self.isLeapYear(data_year)):
            day_of_month[1]+=1
        
        res = 0
        for i in range(data_month-1):
            res+=day_of_month[i]
        res += data_day
        return res
        
    def isLeapYear(self,year : int):
        if(year % 400 ==0 and year % 100 == 0):
            return True
        if(year % 4 ==0 and year % 100 != 0):
            return True
        return False

test = Solution()
print(test.dayOfYear("2019-01-9"))
print(test.dayOfYear("2019-02-10"))