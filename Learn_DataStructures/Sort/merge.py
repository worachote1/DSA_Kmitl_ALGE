x = [2, 1, 3, -4, 22, 7, 15]

# helper
def merge(data: list, l: int, m: int, r: int):
    n1 = m - l + 1
    n2 = r - m

    L_arr = [0] * n1
    R_arr = [0] * n2

    for i in range(0,n1):
        L_arr[i]=data[l+i]
    for i in range(0,n2):
        R_arr[i] = data[m+1+i]

    i = 0
    j = 0
    k = l
    while(i<n1 and j<n2):
        if(L_arr[i]<=R_arr[j]):
            data[k]=L_arr[i]
            k+=1
            i+=1   
        elif(R_arr[j]<L_arr[i]):
            data[k]=R_arr[j]
            k+=1
            j+=1
    
    while(i<n1):
        data[k]=L_arr[i]
        k+=1
        i+=1
    while(j<n2):
        data[k]=R_arr[j]
        k+=1
        j+=1  

def merge_sort(data: list,l: int,r: int):
    if(l<r):
        m = (l+(r-1))//2
        merge_sort(data,l,m)
        merge_sort(data,m+1,r)

        merge(data,l,m,r)    

print(x)
merge_sort(x,0,len(x)-1)
print(x)
