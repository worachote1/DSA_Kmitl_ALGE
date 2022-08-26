# def twoNumberSum(array, targetSum):
#     res = [];
#     for i in range(len(array)-1,1-1,-1):
#         for j in range(i-1,0-1,-1):
#             res_each_pair = [];
#             if(array[i]!=array[j]):
#                 sum = array[i]+array[j];
#                 if(sum==targetSum):
#                     res_each_pair.append(array[j]);
#                     res_each_pair.append(array[i]);
#             if(res_each_pair != []):
#                 if(res_each_pair not in res):
#                     res.append(res_each_pair);
#     if(res == []):
#         return [];

#     return res[0];    

#solution 2
def twoNumberSum(array, targetSum):
    
    array.sort();
    left = 0;
    right = len(array)-1;
    while(left<right):
        res = array[left]+array[right];
        if(res<targetSum):
            left+=1;
            continue;
        if(res>targetSum):
            right-=1;
            continue;
        return [array[left],array[right]];

    return [];
#test
print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10));
print(twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9],17));
print(twoNumberSum([15],15));





