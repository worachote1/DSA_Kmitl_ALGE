def fourNumberSum(array, targetSum):
    # 26 DEC 2022
    data = {}
    res = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            sumNum = array[i]+array[j]
            diff = targetSum - sumNum
            if(diff in data):
                for item in data[diff]:
                    res.append([item[0],item[1],array[i],array[j]])

        for j in range(0,i):
            sumNum = array[j]+array[i]
            if(sumNum not in data):
                data[sumNum] = []
            data[sumNum].append([array[j],array[i]])
    
    return res

print(fourNumberSum([2,2,2,2],8))