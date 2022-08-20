class Queue:
    def __init__(self):
        self.q = []
    def Enqueue(self,i):
        self.q.append(i)
    def Dequeue(self):
        if(len(self.q)==0):
            return ""
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0
    def size(self):
        return len(self.q)
    def show(self):
        return self.q.copy()

routine = input("Enter Input : ").split(",");
Myqueue = Queue();
Yourqueue = Queue();
for item in routine:
    Myqueue.Enqueue(item[0:3]);
    Yourqueue.Enqueue(item[4:]);

#Display Queue section
print("My   Queue = ",end="");
for i in range(len(Myqueue.q)):
    print(Myqueue.q[i],end="");
    if(i!=len(Myqueue.q)-1):
        print(end=", ");
    
print();

print("Your Queue = ",end="");
for i in range(len(Yourqueue.q)):
    print(Yourqueue.q[i],end="");
    if(i!=len(Yourqueue.q)-1):
        print(end=", ");
print();

#Cal and Display Activity:Location section
score = 0;
activity = ["Eat","Game","Learn","Movie"];
location = ["Res.","ClassR.","SuperM.","Home"];
ssMy = "My   Activity:Location = ";
ssYour = "Your Activity:Location = ";
for i in range(len(Myqueue.q)):
    MyAct = activity[int(Myqueue.q[i][0])];
    MyLoc = location[int(Myqueue.q[i][2])];
    ssMy+=MyAct+":"+MyLoc;
    if(i!=len(Myqueue.q)-1):
        ssMy+=", ";
    
    YourAct = activity[int(Yourqueue.q[i][0])];
    yourLoc = location[int(Yourqueue.q[i][2])];
    ssYour+=YourAct+":"+yourLoc;
    if(i!=len(Yourqueue.q)-1):
        ssYour+=", ";
    
    #cal
    if(MyAct==YourAct and MyLoc!=yourLoc):
        score+=1;
        continue;
    if(MyAct!=YourAct and MyLoc==yourLoc):
        score+=2;
        continue;
    if(MyAct==YourAct and MyLoc==yourLoc):
        score+=4;
        continue;
    
    score-=5;

print(ssMy);
print(ssYour);
ssResult = "";
if(score>=7):
    ssResult+="Yes! You're my love! : Score is "+str(score)+".";
    print(ssResult);
    exit();
elif(score>0):
    ssResult+="Umm.. It's complicated relationship! : Score is "+str(score)+".";
    print(ssResult);
    exit();

ssResult+="No! We're just friends. : Score is "+str(score)+".";
print(ssResult);


