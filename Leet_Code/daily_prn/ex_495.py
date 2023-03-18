# 495. Teemo Attacking
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        cnt = 0
        for i in range(len(timeSeries)-1):
            cnt += timeSeries[i+1]-timeSeries[i] if (timeSeries[i]+duration-1 >= timeSeries[i+1]) else duration
        return cnt + duration
    
    
test = Solution()
print(test.findPoisonedDuration([1,4],2))
print(test.findPoisonedDuration([1,2],2))

#
print(test.findPoisonedDuration([1,2,3,4,5,6,7,8,9],1))