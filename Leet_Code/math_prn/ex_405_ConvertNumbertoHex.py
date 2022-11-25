#405. Convert a Number to Hexadecimal

# Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
# Note: You are not allowed to use any built-in library method to directly solve this problem.

class Solution:
    def toHex(self, num: int) :
        digit_code = {10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        data = []
        if(num == 0):
            return "0"
        if(num < 0):
            num = num + 2**32
        while(num>0):
            x = num % 16
            num = num // 16
            data.append(digit_code[x] if x>=10 and x<=15 else str(x))
        
        return "".join(data[::-1])

test = Solution()
print(test.toHex(-1))