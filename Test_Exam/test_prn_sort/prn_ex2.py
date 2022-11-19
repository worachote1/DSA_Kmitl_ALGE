def solution(data : list):
    
    data_postive = [item for item in data if item>=0]
    # data_Idx_negative = [i for i in range(len(data)) if data[i]<0]
    #sort data
    for i in range(len(data_postive)):
        for j in range(len(data_postive)-1-i):
            if(data_postive[j]>data_postive[j+1]):
                temp = data_postive[j]
                data_postive[j]=data_postive[j+1]
                data_postive[j+1]=temp

    #change data
    for i in range(len(data)):
        if(data[i]<0):
            continue
        data[i]=data_postive.pop(0)
    
    return " ".join([str(item) for item in data])

inp = input("Enter Input : ").split(" ")
data = [int(item) for item in inp]
print(solution(data))