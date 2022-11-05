# Ex 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0,0]
        for i in range(len(s)):
            
            #check odd palindrome
            pL_odd = i-1
            pR_odd = i+1
            while(pL_odd >= 0 and pR_odd <= len(s)-1):
                if(s[pL_odd]!=s[pR_odd]):
                    break

                if(pR_odd-pL_odd >= res[1]-res[0]):
                    res = [pL_odd,pR_odd]

                pL_odd-=1
                pR_odd+=1
            #check even palindrome
            pL_even = i-1
            pR_even = i
            while(pL_even>=0 and pR_even <= len(s)-1):
                if(s[pL_even]!=s[pR_even]):
                    break

                if(pR_even-pL_even >= res[1]-res[0]):
                    res = [pL_even,pR_even]
                
                pL_even-=1
                pR_even+=1
            
        return s[res[0]:res[1]+1]
            