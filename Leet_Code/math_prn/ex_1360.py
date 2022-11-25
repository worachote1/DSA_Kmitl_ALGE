#1360. Number of Days Between Two Dates

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) :
        return abs(self.helper(date1) - self.helper(date2)) 

    def isLeapYear(self,year : int):
        if(year % 400 ==0 and year % 100 == 0):
            return True
        if(year % 4 ==0 and year % 100 != 0):
            return True
        return False

    def helper(self,date : str):
        data_year = int(date[0:3+1])
        data_month = int(date[5:6+1]) if date[5] != "0" else int(date[6])
        data_day = int(date[8:9+1]) if date[8] != "0" else int(date[9])
        day_of_month = [
            31,28,31,30,31,30,31,31,30,31,30,31
        ]
        res = 0
        for y in range(1971,data_year):
            res += 365 if not self.isLeapYear(y) else 366
        for m in range(data_month-1):
            res += day_of_month[m]
        res += 1 if self.isLeapYear(data_year) and data_month > 2 else 0
        res += data_day
        return res

test = Solution()
print(test.daysBetweenDates("2020-01-15","2019-12-31"))

# error test case : 
# date1 : "2023-01-13" , date2 : "2044-02-11" 
# Note from now 25/nov/2022 --> what will happen on date2 (date2 : "2044-02-11" )
print(test.daysBetweenDates("2023-01-13","2044-02-11")) # must be 7699
print("prnnnnn")
print(test.helper("2023-01-13"))
print(test.helper("2044-02-11"))