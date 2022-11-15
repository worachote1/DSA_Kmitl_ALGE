class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int):
        # Tomohiko Sakamoto’s Algorithm
        return self.helper(day, month, year)

    def helper(self, day: int, month: int, year: int):
        # leading number of days of each month
        LEADING_DAYS = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
        day_of_week = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        if (month < 3):
            year -= 1
        data = (year + year // 4 - year // 100 + year // 400 + LEADING_DAYS[month - 1] + day) % 7
        return day_of_week[data]

test = Solution()
print(test.dayOfTheWeek(31,8,2019))
print(test.dayOfTheWeek(26,12,2004))
