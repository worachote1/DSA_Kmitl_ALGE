class Solution:
    def reverseVowels(self, s: str) :
        ss_list = []
        for item in s:
            ss_list.append(item)

        data_vowel = "aeiouAEIOU"
        pL,pR = 0,len(ss_list)-1
        while(pL<pR):
            if(ss_list[pL] in data_vowel and ss_list[pR] in data_vowel):
                temp = ss_list[pR]
                ss_list[pR]=ss_list[pL]
                ss_list[pL]=temp    
                pL+=1
                pR-=1
                continue    
            if(ss_list[pL] not in data_vowel):
                pL+=1
            if(ss_list[pR] not in data_vowel):
                pR-=1     
        return "".join(ss_list)

test = Solution()
print(test.reverseVowels("hello"))
print(test.reverseVowels("leetcode"))