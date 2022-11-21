def binary_search(data : list,val : int,left : int , right : int):
    if(left<=right):
        mid = (left+right)//2
        if(data[mid]<val):
            return binary_search(data,val,mid+1,right)
        elif(data[mid]>val):
            return binary_search(data,val,left,mid-1)
        else:
            return True
    else:
        return False
    

data = [8,9,12,15,17,19,20,21,28]
data.sort()
print(binary_search(data,21,0,len(data)-1))