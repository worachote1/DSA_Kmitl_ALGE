def threeNumberSum(array, targetSum):
    res = [];
    array.sort();
    for i in range(len(array)):
        left = i+1;
        right = len(array)-1;
        while(left<right):
            sum = array[i]+array[left]+array[right]
            if(sum==targetSum):
                #found a triplet
                res.append([array[i],array[left],array[right]]);
                left+=1;
                right-=1;
            elif(sum<targetSum):
                left+=1;
            elif(sum>targetSum):
                right-=1;
           
           # print("prn 44");
    
    return res;

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],0));    
