
def underscorifySubstring(string, substring):
    sub_length = len(substring)
    res_Pos = []
    underscore_POS_data = []
    Lp = -44
    Rp = -44
    for i in range(len(string)):
        sub_length = len(substring)
        target = string[i:i+sub_length]        
        if(target==substring):
            Lp = i
            Rp = i+sub_length
            if(underscore_POS_data == []):
                underscore_POS_data.append(Lp)
                underscore_POS_data.append(Rp)
            else:
                underscore_POS_data[1]=Rp
        if(string[i]==" " or i==len(string)-1):
            if(underscore_POS_data != []):
                res_Pos.append(underscore_POS_data[0])
                res_Pos.append(underscore_POS_data[1])
            underscore_POS_data = []
    
    print("res -> ",str(res_Pos))
    ss = ""
    if(res_Pos != []):
        for i in range(len(string)):
            if(i in res_Pos):
                ss+="_"
            ss+=string[i]
        if(res_Pos[-1]>len(string)-1):
            ss+="_"

    return ss if res_Pos != [] else string

string = "abababababababababababababaababaaabbababaa";
substring = "a"

print(underscorifySubstring(string,substring))