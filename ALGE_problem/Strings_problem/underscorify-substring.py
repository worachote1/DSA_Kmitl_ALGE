
def underscorifySubstring(string, substring):
    underscore_POS_data =  findAllPos(string,substring)
    # print(underscore_POS_data)
    underscore_POS_data = manange_collapse(underscore_POS_data)
    # print(underscore_POS_data)
    # display section
    if(underscore_POS_data==[]):
        return string
    ss = ""
    for i in range(len(string)):
        for item in underscore_POS_data:
            if(i in item):
                ss+="_"
                break
        ss += string[i]
    if(underscore_POS_data[-1][1]>len(string)-1):
        ss+="_"
    return ss

def findAllPos(string,substring):
    startIdx = 0
    res = []
    
    while(startIdx < len(string)):
        foundAt = string.find(substring,startIdx)    
        if(foundAt == -1):
            break;
        
        res.append([foundAt,foundAt+len(substring)])
        #print(res)
        startIdx = foundAt+1

    return res

def manange_collapse(data):
    if(data==[]):
        return data
    
    new_data = [data[0]]
    prev = new_data[0]

    for i in  range(1,len(data)):
        cur = data[i]
        if(prev[1]>=cur[0]):
            prev[1]=cur[1]
        else:
            new_data.append(cur)
            prev = cur
    
    return new_data


string = "abababababababababababababaababaaabbababaa";
substring = "a"
print(underscorifySubstring(string,substring))
# string2="testthis is a testtest to see if testestest it works"
# substring2="test"
# print(underscorifySubstring(string2,substring2))