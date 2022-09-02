def isPalindrome(string):
    if(len(string)==0):
        return True;
    return isPalindromePlay(string,0,len(string)-1);

def isPalindromePlay(string,pLeft,pRight):

    if(pLeft>=pRight):
        return True;

    if(string[pLeft]!=string[pRight]):
        return False;

    return isPalindromePlay(string,pLeft+1,pRight-1);

p = "abcdcba";
print(isPalindrome(p));


