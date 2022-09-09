def insertionSort(array):
    for i in range(1,len(array)):
        curVal = array[i]
        j = i-1
        while(j>=0 and curVal<array[j]):
            array[j+1]=array[j]
            j-=1
        
        array[j+1]=curVal;
    
    return array

arr1 = [8, 5, 2, 9, 5, 6, 3];
print(insertionSort(arr1))