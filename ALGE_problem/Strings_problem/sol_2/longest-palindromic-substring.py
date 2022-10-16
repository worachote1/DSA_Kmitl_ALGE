def longestPalindromicSubstring(string):
    if(len(string) == 1):
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

            if(string[pL_even] != string[pR_even]):
                break;

            if(abs(pR_even-pL_even) > abs(res[1]-res[0])):
                res = [pL_even, pR_even]

            pL_even -= 1;
            pR_even += 1;
    return string[res[0]:res[1]+1]


string1 = "abaxyzzyxf"
print(longestPalindromicSubstring(string1))


# prn

def longestPalindromicSubstring(string):

    res = [-44, -44]
    for i in range(len(string)):

        # odd-len pal
        pR_odd = i-1
        pL_odd = i+1
        while(pR_odd < 0 or pL_odd > len(string)-1):
            if(string[pR_odd] != string[pL_odd]):
                break;
            pR_odd -= 1
            pL_odd += 1

        # even-len pal
        pR_even = i
        pL_even = i+1
        while(pR_odd < 0 or pL_odd > len(string)-1):
           if(string[pR_odd] != string[pL_odd]):
                break;
            pR_even-=1
            pL_even+=1
            
    res[0]=pR_odd if abs(pL_odd - pR_odd)>abs(pL_even-pR_even) else pR_even
    res[1]=pL_odd if abs(pL_odd - pR_odd)>abs(pL_even-pR_even) else pL_even

    return string[res[0]:res[1]+1]