import string


def longestPalindromicSubstring(string):
    if(len(string)==1):
        return string;
    res = [-44,-44];
    for i in range(len(string)):
        #check odd-length palindromes
        pL_odd = i-1;
        pR_odd = i+1;
        while(pL_odd >= 0 and pR_odd<=len(string)-1):
            if(string[pL_odd]!=string[pR_odd]):
                break;
            if(abs(pL_odd-pR_odd)>=abs(res[0]-res[1])):
                res = [pL_odd,pR_odd];
            pL_odd-=1;
            pR_odd+=1;
        
        #check even-length palindromes
        pL_even = i-1;
        pR_even = i;
        while(pL_even >= 0 and pR_even<=len(string)-1):
            if(string[pL_even]!=string[pR_even]):
                break;
            if(abs(pL_even-pR_even)>=abs(res[0]-res[1])):
                res = [pL_even,pR_even];
            pL_even-=1;
            pR_even+=1;

    #print(res);
    return string[res[0]:res[1]+1]

string = "abaxyzzyxf";
print(longestPalindromicSubstring(string));
ss1 = "aa";
print(longestPalindromicSubstring(ss1));
ss2 = "a";
print(longestPalindromicSubstring(ss2));