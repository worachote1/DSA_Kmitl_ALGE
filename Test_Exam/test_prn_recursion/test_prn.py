#three num sum

def threeNumberSum(array, targetSum):
    # Write your code here.
    res = []
    array.sort()
    for i in range(len(array)-1):
        leftIdx = i+1
        rightIdx = len(array)-1
        while(leftIdx<rightIdx):
            sum = array[i]+array[leftIdx]+array[rightIdx]
            if(sum==targetSum):
                print("sfa")
                found_arr = [array[i],array[leftIdx],array[rightIdx]]
                if(found_arr not in res):
                    res.append(found_arr)
                leftIdx+=1
                rightIdx-=1
            
            if(sum<targetSum):
                leftIdx+=1
            if(sum>targetSum):
                rightIdx-=1

    return res

arr = [12, 3, 1, 2, -6, 5, -8, 6]
print(threeNumberSum(arr,0))