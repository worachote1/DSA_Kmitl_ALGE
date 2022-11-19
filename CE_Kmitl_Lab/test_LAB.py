x = "1357"
data = [int(item) for item in x]
def check_Metadrome(data : list):
    prev_val = []
    for i in range(len(data)-1):
        if(not (data[i]<data[i+1])):
            return False
        if(data[i] in prev_val):
            return False
        prev_val.append(data[i])
    return True if data[len(data)-1] not in prev_val else False
x1 = "12344"
data1 = [int(item) for item in x1]
def check_Plaindrome(data : list):
    prev_val = []
    isDup = False
    for i in range(len(data)-1):
        if(not (data[i]<=data[i+1])):
            return False
        if(data[i] in prev_val):
            isDup = True
        prev_val.append(data[i])
    
    isLast_Dup = data[len(data)-1] in prev_val
    return True if isDup or isLast_Dup else False

x2 = "7531"
data2 = [int(item) for item in x2]
def check_Katadrome(data: list):
    prev_val = []
    for i in range(len(data)-1):
        if(not (data[i]>data[i+1])):
            return False
        if(data[i] in prev_val):
            return False
        prev_val.append(data[i])
    return True if data[len(data)-1] not in prev_val else False

x3 = "9874441"
data3 = [int(item) for item in x3]
def check_Nialpdrome(data : list):
    prev_val = []
    isDup = False
    for i in range(len(data)-1):
        if(not (data[i]>=data[i+1])):
            return False
        if(data[i] in prev_val):
            isDup = True
        prev_val.append(data[i])
    
    isLast_Dup = data[len(data)-1] in prev_val
    return True if isDup or isLast_Dup else False

print(check_Metadrome(data))
print(check_Plaindrome(data1))
print(check_Katadrome(data2))
print(check_Nialpdrome(data3))