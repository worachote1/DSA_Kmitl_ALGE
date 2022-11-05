class Solution:
    def letterCombinations(self, digits: str):
        data = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if(len(digits) == 0):
            return []
        if(len(digits) == 1):
            return [item for item in data[digits]]

        res = []
        self.helper(digits, data, res, "", 0)
        return res

    def helper(self, digit_ss: str, data_map: dict, res: list, ss: str, idx: int):

        if(idx > len(digit_ss)-1):
            res.append(ss)
            return
        for item in data_map[digit_ss[idx]]:
            new_string = ss+item
            self.helper(digit_ss, data_map, res, new_string, idx+1)
