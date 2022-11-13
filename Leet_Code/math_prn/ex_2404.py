class Solution:
    def mostFrequentEven(self, nums: list[int]) :
        data = {}
        for item in nums:
            if(item % 2 !=0):
                continue
            if(item not in data):
                data[item] = 1
            else:
                data[item]+=1
        if(len(data)==0):
            return -1
        maxVal = data[list(data)[0]]
        res = list(data)[0]
        for item in data:
            if(data[item]>maxVal):
                maxVal = data[item]
                res = item
            elif(data[item]==maxVal):
                if(item<res):
                    res = item
        return res

test = Solution()
print(test.mostFrequentEven([0,1,2,2,4,4,1]))
print(test.mostFrequentEven([4,4,4,9,2,4]))