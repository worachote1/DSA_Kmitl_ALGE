class Solution(object):
    def findWords(self, words):
        res = []
        row_all = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for item in words:
            new_word = item.lower()
            for Idx in range(len(row_all)):
                if(len(list(set(row_all[Idx]+new_word)-set(row_all[Idx])))==0):
                    res.append(item)
                    break
        return res