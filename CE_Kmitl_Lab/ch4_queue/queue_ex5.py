


#Fuck U Kritsada
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

class Stack:
    # __ 
    def __init__(self):
        self._data = [];
        self._size = 0;


    def push(self,data):
        self._data.append(data);
        self._size+=1;

    def pop(self):
        if(self._size==0):
            return"Can not pop";
        self._size-=1;
        return self._data.pop();

    def peek(self):
        return self._data[len(self._data)-1];

    def getData(self):
        return self._data;

    def size(self):
        return self._size;

    def isEmpty(self):
        if(self._size==0):
            return True;
        return False;

    def items(self):
        return self._data;

inp = input("Enter Input (Normal, Mirror) : ");
normal_data = inp.split(" ")[0];
mirror_data = inp.split(" ")[1];
# print("nor -> ",nor_data);
# print("mirror -> ",mirror_data);
#reverse mirror_data
temp_mirror = [];
for i in range(len(mirror_data)-1,-1,-1):
    temp_mirror.append(mirror_data[i]);

mirror_data = temp_mirror;

# check bomb and push to stack_mirror 
# and pop item from stack_mirror to Enqueue queue_mirror
stack_mirror = Stack();
queue_mirror = Queue();
count_mirrorBomb = 0;
for item in mirror_data:
    if(stack_mirror.size()<2):
        stack_mirror.push(item);
        continue;
    
    stack_mirror.push(item);
    peek_1st = stack_mirror.pop();
    peek_2nd = stack_mirror.pop();
    peek_3rd = stack_mirror.pop();
    #check if there are same 3 consecutive -> bomb ->keep in queue_mirror
    if(peek_1st==peek_2nd and peek_2nd==peek_3rd):
        #bomb
        queue_mirror.Enqueue(peek_1st);
        count_mirrorBomb+=1;
        continue;
    #not the same 3 consecutive -> not bomb -> push all 3 back to stack_mirror
    stack_mirror.push(peek_3rd);
    stack_mirror.push(peek_2nd);
    stack_mirror.push(peek_1st);

# print("queue_mirror -> ",queue_mirror.q);
# print("the rest of stack_miror -> ",stack_mirror._data);

#check bomb from normal data and use item from mirror_queue
#AAABBBCDEE FGHHHIOPPP
stack_normal = Stack();
countNormal_bomb = 0;
countMirrorItem_failed = 0;
check_AlmostBomb = False;
for item in normal_data:
    if(stack_normal.isEmpty()):
        stack_normal.push(item);
        continue;
    if(stack_normal.size()==1):
        if(stack_normal.peek()==item):
            check_AlmostBomb=True;
            stack_normal.push(item);
            continue;
        check_AlmostBomb=False;
        stack_normal.push(item);
        continue;
    #item to save the bomb from queue_mirror still exist
    if((check_AlmostBomb) and (not queue_mirror.isEmpty())):
        stack_normal.push(queue_mirror.Dequeue());
        peek_1st = stack_normal.pop();
        peek_2nd = stack_normal.pop();
        peek_3rd = stack_normal.pop();
        #use item from queue_mirror but failed or not ?
        #if it failed (bomb anyway)
        if(peek_1st==peek_2nd and peek_2nd==peek_3rd):
            countMirrorItem_failed+=1
            stack_normal.push(item);
            check_AlmostBomb = False;
            continue;
        #not failed (proteccted not to bomb)
        stack_normal.push(peek_3rd);
        stack_normal.push(peek_2nd);
        stack_normal.push(peek_1st);
        stack_normal.push(item);
        check_AlmostBomb = False;
        continue;
    
    if(item==stack_normal.peek()):
        check_AlmostBomb=True;
    else:
        check_AlmostBomb=False;
    stack_normal.push(item);
    peek_1st = stack_normal.pop();
    peek_2nd = stack_normal.pop();
    peek_3rd = stack_normal.pop();
    if(peek_1st==peek_2nd and peek_2nd==peek_3rd):
        countNormal_bomb+=1;
        continue;
    stack_normal.push(peek_3rd);
    stack_normal.push(peek_2nd);
    stack_normal.push(peek_1st);

#Display normal
print("NORMAL :");
print(stack_normal.size());
if(stack_normal.isEmpty()):
    print("Empty");
for i in range(len(stack_normal._data)-1,-1,-1):
    print(stack_normal._data[i],end="");
    if(i==0):
       print();
       # print();    
print(str(countNormal_bomb)+" Explosive(s) ! ! ! (NORMAL)");
if(countMirrorItem_failed!=0):
    print("Failed Interrupted "+str(countMirrorItem_failed)+" Bomb(s)");

#Display mirror
print("------------MIRROR------------");
print(": RORRIM");
print(stack_mirror.size());
if(stack_mirror.isEmpty()):
    print("ytpmE");
for i in range(len(stack_mirror._data)-1,-1,-1):
    print(stack_mirror._data[i],end="");
    if(i==0):
        print();
print("(RORRIM) ! ! ! (s)evisolpxE "+str(count_mirrorBomb));


        
    
