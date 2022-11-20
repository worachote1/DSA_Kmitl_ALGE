x = [2,1,3,-4,22,7,15]

def bubble(data : list):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if(data[j]>data[j+1]):
                data[j],data[j+1]=data[j+1],data[j]

print(x)
bubble(x)
print(x)