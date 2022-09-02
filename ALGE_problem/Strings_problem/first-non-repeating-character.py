from itertools import count


def firstNonRepeatingCharacter(string):
    
    data = {};
    for item in string:
        if(item not in data.keys()):
            data[item] = 1;
            continue;
        data[item]+=1; 

    countChar = list(data.values());
    #print("c -> ",countChar);
    if(1 not in countChar):
        return -1;
    
    for i in  range(len(string)):
        if(data[string[i]]==1):
            return i;

string = "abcdcaf";
ss2 = "ababac";
#print(firstNonRepeatingCharacter(string));
print(firstNonRepeatingCharacter(ss2));