class Solution:
    def letterCombinations(self, digits: str):
        data = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if(len(digits)==0):
            return []
        if(len(digits)==1):
            return [item for item in digits]

        res = []
        self.helper(digits,data,res)
        return res

    def helper(self,digit_ss,data_map,res):
        pass