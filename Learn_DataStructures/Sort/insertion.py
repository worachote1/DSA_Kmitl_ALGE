x = [2,1,3,-4,22,7,15]

def insertion(data : list):
    for i in range(1,len(data)):
        key = data[i]
        j = i-1
        while(j>=0 and key<data[j]):
            data[j+1]=data[j]
            j-=1
        data[j+1]=key

print(x)
insertion(x)
print(x)