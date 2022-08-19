class Queue:
    def __init__(self):
        self.q = []
    def Enqueue(self,i):
        self.q.append(i)
    def Dequeue(self):
        if(len(self.q)==0):
            return "Empty"
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0
    def size(self):
        return len(self.q)
    def show(self):
        return self.q.copy()

#EN 1,ES 2,ES 99,D,D,D,EN 3,D
q = Queue();
inp = input("Enter Input : ").split(",")
for item in inp:
    if(item[0]=="D"):
        if(q.size()==0):
            print(q.Dequeue());
            continue;
        #print("that queue -> ",q.q);
        print(q.Dequeue()[3:]);
    
    #role ES > EN so that ES must be front of EN
    if(item[0:2]=="EN"):
        q.Enqueue(item);
        continue;
    if(item[0:2]=="ES"):
        
        if(q.isEmpty()):
            q.Enqueue(item);
            continue;

        if(q.q[-1][0:2]=="ES"):
            q.Enqueue(item);
            #print("qwd -> "+item);
            continue;

        inserSpot = -44;
        for i in range(q.size()-1,0-1,-1):
                if(q.q[i][0:2]=="ES"):
                    inserSpot = i+1;
                    #print("prn insert spot -> ",inserSpot);
                    break;
        q.q.insert(inserSpot,item);
    
# EN 1,EN 2,ES 44,D