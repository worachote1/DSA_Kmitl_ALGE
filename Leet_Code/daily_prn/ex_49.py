class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        data = {}
        res = []
        for item in strs:
            x = "".join(sorted([word for word in item]))
            if(x not in data):
                data[x] = [item]
            else:
                data[x].append(item)
        for item in data.values():
            res.append(item)
        return res

test = Solution()
print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))