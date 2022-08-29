class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if(self.isEmpty()):
            return "Empty";
        cur = self.head;
        ss = ""
        while(cur != None):
            ss += cur.data+"";
            cur= cur.next;
        
        return ss;
    
    def isEmpty(self):
        return self.head is None

    def append(self,data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return 
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        newNode.prev = cur

    def size(self):
        cur, size = self.head, 0
        while cur is not None:
            size += 1
            cur = cur.next
        return size

    def add_before(self,data):
        newNode = Node(data)
        cur = self.head
        if self.isEmpty():
            self.head = newNode
            return 
        cur.prev = newNode
        newNode.next = cur
        self.head = newNode
        return 

Kuy_Kritsada = DoublyLinkedList();
count_Bomb = 0;
inp = input("Enter Input : ").split(" ");

#Check the bomb at evrytime that add element
for item in inp:
    #print(item);
    Kuy_Kritsada.add_before(item);
    if(Kuy_Kritsada.size()<=2):
        continue;
    
    #play Color Crush
    cur = Kuy_Kritsada.head;
    while(cur.next.next != None):
        if((cur.data == cur.next.data) and(cur.next.data==cur.next.next.data)):
            count_Bomb+=1;
            #here 44
            #if these bombed item are the last 3 item
            if(cur.prev==None and cur.next.next.next == None):
                Kuy_Kritsada.head.next = None;
                Kuy_Kritsada.head = None;
            #if the last element just bombed
            elif(cur.prev!=None and cur.next.next.next == None):
                #Kuy_Kritsada.head = cur.prev;
                Kuy_Kritsada.prev.next =  None;
            #
            elif(cur.prev==None and cur.next.next.next != None):
                Kuy_Kritsada.head = cur.next.next.next;

            elif(cur.prev != None and cur.next.next.next != None):
                cur.next.next.next.prev = cur.prev;
                cur.prev.next = cur.next.next.next;
            
            break;
            #
        cur = cur.next;
    
    # print("prn44 -> ",Kuy_Kritsada);

print(Kuy_Kritsada.size());
print(Kuy_Kritsada);
if(count_Bomb>=2):
    print("Combo : {0} ! ! !".format(count_Bomb));

