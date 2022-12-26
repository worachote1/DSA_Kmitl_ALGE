class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]):
        type_pokerHand = ["Flush","Three of a Kind","Pair","High Card"]
        isFlush,data = True,{}
        for i in range(len(suits)-1):
            if(suits[i]!=suits[i+1]):
                isFlush = False
                break
        if(isFlush):
            return type_pokerHand[0]
        for item in ranks:
            if(item not in data):
                data[item]=1
                continue
            data[item]+=1
            if(data[item]==3):
                return type_pokerHand[1]
        if(2 in list(data.values())):
            return type_pokerHand[2]
        return type_pokerHand[3]

        

test = Solution()
print(test.bestHand([4,4,2,4,4],["d","a","a","b","c"]))
