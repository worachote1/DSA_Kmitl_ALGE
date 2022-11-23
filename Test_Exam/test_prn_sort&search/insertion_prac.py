x = [2,1,3,-4,22,7,15]

def insertionSort(array):
    # Write your code here.
    for i in range(1,len(array)):
        j = i-1
        cur = array[j+1]
        while(j>=0 and cur<array[j]):
            array[j+1]=array[j]
            j-=1

        array[j+1]=cur
    
    return array

print(x)
print(insertionSort(x))