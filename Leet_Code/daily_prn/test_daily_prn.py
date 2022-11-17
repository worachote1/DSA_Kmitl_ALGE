from collections import defaultdict

# Function to find number of subarrays
# with sum exactly equal to k.


def findSubarraySum(arr,k):

        ans= 0
        preSum = 0
        dic = {}
        dic[0] = 1
        for i in arr:
            preSum += i
            if preSum-k in dic:
                ans+=dic[preSum-k]
            if(preSum not in dic):
                dic[preSum]=1
            else:
                dic[preSum] +=1 
        
        print(dic)
        return ans


arr = [10, 2, -2, -20, 10]
Sum = -10
n = len(arr)
# print(findSubarraySum(arr, Sum))
# print(findSubarraySum([1,2,3],3))
