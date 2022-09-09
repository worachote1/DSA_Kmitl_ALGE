def reverseWordsInString(string):
    res=[]
    pR= len(string)-1
    pL = len(string)-1
    while(pL >= 0):
        if string[pL] != " ":
            pL -= 1
        else:
            res.append(string[pL+1:pR+1])
            pL -= 1
            pR = pL

    res.append(string[pL+1:pR+1])

    return " ".join(res)