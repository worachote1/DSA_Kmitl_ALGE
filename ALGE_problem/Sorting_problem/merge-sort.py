def merge(array,l,m,r):
    n1 = m-l+1
    n2 = r-m

    arrLeft = [0]*n1
    arrRight = [0]*n2

    for i in range(n1):
        arrLeft[i] = array[l+i]
    for j in range(n2):
        arrRight[j] = array[m+1+j]
    
    i,j,k=0,0,l
    while(i<n1 and j<n2):
        if(arrLeft[i]<arrRight[j]):
            array[k]=arrLeft[i]
            k+=1
            i+=1
        elif(arrRight[j]<=arrLeft[i]):
            array[k]=arrRight[j]
            k+=1
            j+=1
    while(i<n1):
        array[k]=arrLeft[i]
        k+=1
        i+=1
    while(j<n2):
        array[k]=arrRight[j]
        k+=1
        j+=1


def mergeSort(array,left,right):
    if(left<right):
        mid = (left+(right-1))//2
        mergeSort(array,left,mid)
        mergeSort(array,mid+1,right)

        merge(array,left,mid,right)
    


x = [2,1,3,-4,22,7,15]
print(x)
mergeSort(x,0,len(x)-1)
print(x)