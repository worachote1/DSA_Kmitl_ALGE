class Solution:
    def distributeCandies(self, candies: int, num_people: int) :
        val = 1
        Idx = 0
        res = [0 for item in range(num_people)]
        while(candies>0):
            res[Idx%num_people] += val
            candies -= val
            Idx+=1
            val+=1
            if(val>=candies):
                val = candies
        return res

test = Solution()
print(test.distributeCandies(7,4))
print(test.distributeCandies(10,3))
            
            