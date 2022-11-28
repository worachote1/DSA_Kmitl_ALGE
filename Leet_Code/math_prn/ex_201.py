class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) :
        count_time_shift = 0
        while(left != right):
            left = left>>1
            right = right>>1
            count_time_shift+=1
        return left<<count_time_shift

test = Solution()
print(test.rangeBitwiseAnd(5,7))
print(test.rangeBitwiseAnd(1,2147483647))