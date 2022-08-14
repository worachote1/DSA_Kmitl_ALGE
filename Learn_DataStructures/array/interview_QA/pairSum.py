def pairSum(nums,target):
    res = [];
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                if(i not in res):
                    res.append(i);
                if(j not in res):
                    res.append(j);
    return res;

# print(pairSum([2,7,11,15],9));
# print(pairSum([3,2,4],6));
# print(pairSum([3,3],6));