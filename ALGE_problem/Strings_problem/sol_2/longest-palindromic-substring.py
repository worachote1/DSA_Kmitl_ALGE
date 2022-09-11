def longestPalindromicSubstring(string):
    if(len(string)==1):
        return string;
    res = [-44, -44]
    for i in range(len(string)):
        # check for ood palindrome
        pL_ood = i-1
        pR_ood = i+1
        while(pL_ood >= 0 and pR_ood <= len(string)-1):

            if(string[pL_ood] != string[pR_ood]):
                break;

            if(abs(pR_ood-pL_ood) > abs(res[1]-res[0])):
                res = [pL_ood, pR_ood]

            pL_ood -= 1;
            pR_ood += 1;

        # check for even palindrome
        pL_even = i-1
        pR_even = i
        while(pL_even >= 0 and pR_even <= len(string)-1):

            if(string[pL_even]!=string[pR_even]):
                break;
            
            if(abs(pR_even-pL_even)>abs(res[1]-res[0])):
                res = [pL_even,pR_even]

            pL_even-=1;
            pR_even+=1;
    return string[res[0]:res[1]+1]  
        

string1 = "abaxyzzyxf"
print(longestPalindromicSubstring(string1))