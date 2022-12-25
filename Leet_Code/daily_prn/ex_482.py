class Solution:
    def licenseKeyFormatting(self, s: str, k: int) :
        cnt,res,ss = 0,[],""
        for item in s:
            if(item=="-"):
                continue
            cnt+=1
        m = cnt % k
        cnt = 0
        for item in s:
            if(item=="-"):
                continue
            cnt += 1
            ss = ss + item
            if(len(res)==0 and cnt == m and m!=0):
                res.append(ss)
                ss,cnt = "",0
            elif(cnt==k):
                res.append(ss)
                ss,cnt = "",0
        return "-".join(res).upper()

test = Solution()
print(test.licenseKeyFormatting("5F3Z-2e-9-w",4))
print(test.licenseKeyFormatting("2-5g-3-J",2))