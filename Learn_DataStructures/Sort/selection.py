x = [2,1,3,-4,22,7,15]

def selection(data : list):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1,len(data)):
            if(data[min_idx]>data[j]):
                min_idx = j
        data[i],data[min_idx]=data[min_idx],data[i]

print(x)
selection(x)
print(x)