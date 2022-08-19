class Queue:
    def __init__(self):
        self.q = []
    def queue(self,i):
        self.q.append(i)
    def dequeue(self):
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0
    def size(self):
        return len(self.q)
    def show(self):
        return self.q.copy()
q = Queue()
a = input("Enter Input : ").split(",")
for i in range(len(a)):
    if(a[i][0]=="E"):
        q.queue(a[i][2:])
        print(q.size())
    elif(a[i][0]=="D"):
        if(q.size()!=0):
            print(q.dequeue(),0)
        else:
            print(-1)
if(q.size()!=0):
    print(" ".join(q.show()))
else:
    print("Empty")