def solution(data: list):
    if(check_Metadrome(data)):
        return "Metadrome"
    if(check_Plaindrome(data)):
        return "Plaindrome"
    if(check_Katadrome(data)):
        return "Katadrome"
    if(check_Nialpdrome(data)):
        return "Nialpdrome"
    if(check_Repdrome(data)):
        return "Repdrome"
    return "Nondrome"


def check_Metadrome(data: list):
    prev_val = []
    for i in range(len(data)-1):
        if(not (data[i] < data[i+1])):
            return False
        if(data[i] in prev_val):
            return False
        prev_val.append(data[i])
    return True if data[len(data)-1] not in prev_val else False

def check_Plaindrome(data: list):
    prev_val = []
    isDup = False
    for i in range(len(data)-1):
        if(not (data[i] <= data[i+1])):
            return False
        if(data[i] in prev_val):
            isDup = True
        prev_val.append(data[i])

    isLast_Dup = data[len(data)-1] in prev_val
    return True if isDup or isLast_Dup else False

def check_Katadrome(data: list):
    prev_val = []
    for i in range(len(data)-1):
        if(not (data[i]>data[i+1])):
            return False
        if(data[i] in prev_val):
            return False
        prev_val.append(data[i])
    return True if data[len(data)-1] not in prev_val else False


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

def check_Repdrome(data: list):
    prev = int(data[0])
    for item in data:
        if(prev != int(item)):
            return False
    return True


inp = input("Enter Input : ")
data = [int(item) for item in inp]
print(solution(data))
