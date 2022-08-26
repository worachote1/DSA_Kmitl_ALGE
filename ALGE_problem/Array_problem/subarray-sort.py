def subarraySort(array):
    out_of_order = [];
    for i in range(len(array)-1):
        if(array[i]>array[i+1]):
            out_of_order.append(array[i]);
            out_of_order.append(array[i+1]);

    #it's sorted already
    if(len(out_of_order)==0):
        return [-1,-1];
    # print("out_of_order -> ",out_of_order);
    maxOut = max(out_of_order);
    minOut = min(out_of_order);
    # print("prn max min -> "+str(maxOut)+" "+str(minOut));
    maxIndex = -44;
    minIndex = -44;

    for i in range(len(array)):
        minIndex = i;
        if(minOut<array[i]):
            break;
    
    for i in range(len(array)-1,-1,-1):
        maxIndex= i;
        if(maxOut>array[i]):
            break;
    
    return [minIndex,maxIndex];
    
        


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]));
print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]));
#[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]