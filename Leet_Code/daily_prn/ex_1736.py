class Solution:
    def maximumTime(self, time: str) :
        data = list(time)
        for i in range(len(data)):
            if(data[i]=="?"):
                if(i==0):
                    if(data[i+1] not in "456789"):
                        data[i]="2"
                    else:
                        data[i]="1"
                elif(i==1):
                    if(data[i-1]=="2"):
                        data[i]="3"
                    else:
                        data[i]="9"
                elif(i==3):
                    data[i]="5"
                elif(i==4):
                    data[i]="9"
        return "".join(data)
        
test = Solution()
print(test.maximumTime("2?:?0"))
print(test.maximumTime("0?:3?"))
print(test.maximumTime("1?:22"))

        