class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # use: 4 min
        vowel = ['a','A','e','E','i','I','o','O','u','U']
        pL = 0
        pR = len(s)-1
        res_arr = [item for item in s]
        while(pL < pR):
            if(res_arr[pL] in vowel and res_arr[pR] in vowel):
                temp = res_arr[pR]
                res_arr[pR] = res_arr[pL]
                res_arr[pL] = temp
                pL += 1
                pR -= 1
                continue
            if(res_arr[pL] not in vowel):
                pL += 1
            if(res_arr[pR] not in vowel):
                pR -= 1
        res_ss = "".join(res_arr)
        return res_ss            