
def isUnique(list):
    a =[];
    for item in list:
        if item in a:
            print("not unique found "+str(item))
            return False;
        else:
            a.append(item);
    return True;


myList = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]

print(isUnique(myList));