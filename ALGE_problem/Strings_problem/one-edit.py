def oneEdit(stringOne, stringTwo):
    # Write your code here.
    n1,n2=len(stringOne),len(stringTwo)
    if(abs(n1-n2)>1):
        return False
    for i in range(min(n1,n2)):
        if(stringOne[i]!=stringTwo[i]):
            if(n1>n2):
                return stringOne[i+1:]==stringTwo[i:]
            elif(n2>n1):
                return stringOne[i:]==stringTwo[i+1:]
            else:
                return stringOne[i+1:]==stringTwo[i+1:]
    return True

print(oneEdit("bcdefghijklmnopqrstuvwxyz","abcdefghijklmnopqrstuvwxyz"))
