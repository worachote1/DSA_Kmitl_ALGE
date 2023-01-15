class Solution:
    def wordPattern(self, pattern: str, s: str) :
        ss = s.split(" ")
        data = {}
        check_duplicate = []
        if(len(ss)!=len(pattern)):
            return False
        for i in range(len(pattern)):
            if(pattern[i] not in data):
                data[pattern[i]] = [i]
                check_duplicate.append(ss[i])
            else:
                Idx_toCheck = data[pattern[i]][-1]
                if(ss[Idx_toCheck] != ss[i]):
                    return False
                data[pattern[i]].append(i)
        #check duplicate word 
        for i in range(len(check_duplicate)):
            if(check_duplicate[i] in check_duplicate[:i]+check_duplicate[i+1:]):
                return False
        return True

test = Solution()
print(test.wordPattern("abba","dog cat cat dog"))
print(test.wordPattern("abba","dog cat cat fish"))
print(test.wordPattern("aaaa","dog cat cat dog"))

#error
print(test.wordPattern("abba","dog dog dog dog"))