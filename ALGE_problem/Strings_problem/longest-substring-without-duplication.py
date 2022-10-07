def longestSubstringWithoutDuplication(string):
    data_firstIdx= {}
    startIdx = 0
    res = ""
    for i in range(len(string)):
        if string[i] not in data_firstIdx:
            data_firstIdx[string[i]]=i
        
        else:
            startIdx = max(startIdx,data_firstIdx[string[i]]+1)
            data_firstIdx[string[i]]=i

        sub = string[startIdx:i+1]
        res = sub if len(sub)>len(res) else res

    return res        

print(longestSubstringWithoutDuplication("clementisacap"))
print(longestSubstringWithoutDuplication("abcdeabcdefc"))
print(longestSubstringWithoutDuplication("abacacacaaabacaaaeaaafa"))