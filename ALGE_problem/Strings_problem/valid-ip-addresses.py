def validIPAddresses(string):
    res = [];
    for i in range(1,min(4,len(string))):
        current_IPaddress_Parts = ["","","",""]
        current_IPaddress_Parts[0]=string[:i]
        if(not checkIsvalid(current_IPaddress_Parts[0])):
            continue
        
        for j in range(i+1,min(i+4,(len(string)))):
            current_IPaddress_Parts[1] = string[i:j]
            if(not checkIsvalid(current_IPaddress_Parts[1])):
                continue
        
            for k in range(j+1,min(j+4,len(string))):
                current_IPaddress_Parts[2]=string[j:k]
                if(not checkIsvalid(current_IPaddress_Parts[2])):
                    continue
                
                current_IPaddress_Parts[3] = string[k:len(string)]
                if(not checkIsvalid(current_IPaddress_Parts[3])):
                    continue
                res.append(".".join(current_IPaddress_Parts))

    return res

def  checkIsvalid(string):
    ssNum = int(string)
    if(not (ssNum <= 255 and ssNum >= 0)):
        return False
    
    #check if this part have leading 0 
    return len(string)==len(str(ssNum))


string1 = "1921680";
print(validIPAddresses(string1));
