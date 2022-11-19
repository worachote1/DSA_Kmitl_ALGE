def solution(data : list):
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

def check_Metadrome(data : list):
    pass
def check_Plaindrome(data : list):
    pass
def check_Katadrome(data : list):
    pass
def check_Nialpdrome(data : list):
    pass
def check_Repdrome(data : list):
    pass

inp = input("Enter Input : ").split(" ")
data = [int(item) for item in inp]
print(solution(data))