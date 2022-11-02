class Queue:
    def __init__(self):
        self.q = []
    def isEmpty(self):
        return len(self.q)==0
    def Enqueue(self,data):
        self.q.append(data)
    def Dequeue(self):
        self.q.pop(0)
    def size(self):
        return len(self.q)
    def getData(self,idx):
        return self.q[idx]
    def coppy(self):
        return self.q.copy()

class Solution:
    def reverse(self, x: int) -> int:
        res = int(self.helper(x))
        return res if (res >= pow(-2,31) and res <= pow(2,31)-1) else 0

    def helper(self,x : int) -> str:
        data_queue = Queue()
        ss = str(x)
        
        for i in range(len(ss)-1,-1,-1):
            if(ss[i]!="-"):
                data_queue.Enqueue(ss[i])
        #pop if revsered order start with zero..zero..zero..
        for i in range(data_queue.size()):
            if(data_queue.getData(i)!=0):
                break
            data_queue.Dequeue()

        isSigned = "-" if(x<0) else ""
        return isSigned+"".join(data_queue.coppy())