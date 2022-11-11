class Solution:
    def combinationSum2(self, candidates: list[int], target: int) :
        res = []
        self.helper(candidates,target,res)
        return res
    def helper(self,candidates: list[int], target: int, res : list):
        candidates.sort()
        for i in range(len(candidates)):
            pL,pR = 0,len(candidates)-1
            if(candidates[i]==target):
                data = [candidates[i]]
                if(data not in res):
                    res.append(data)
                break
            while(pL<pR):
                # print("ds")
                # if(pL == i or pR == i):
                #     break
                if(candidates[pL]+candidates[i]==target):
                    data = [candidates[pL],candidates[i]]
                    data.sort()
                    if(data not in res):
                        res.append(data)
                if(candidates[i]+candidates[pR]==target):
                    data = [candidates[i],candidates[pR]]
                    data.sort()
                    if(data not in res):
                        res.append(data)
                sumNum = candidates[pL]+candidates[i]+candidates[pR]
                if(sumNum<target):
                    pL += 1
                elif(sumNum>target):
                    pR -= 1
                else:
                    data = [candidates[pL],candidates[i],candidates[pR]]
                    data.sort()
                    if(data not in res):
                        res.append(data)
                    pL+=1
                    pR-=1

test = Solution()
print(test.combinationSum2([10,1,2,7,6,1,5],8))
print(test.combinationSum2([2,5,2,1,2],5))

#prn error test case
print(test.combinationSum2([1,2],2))
print(test.combinationSum2([1,1],2))