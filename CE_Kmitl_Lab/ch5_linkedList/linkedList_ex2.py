
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        
    def __str__(self):
        if(self.isEmpty()):
            return "linked list : "
        cur = self.head;
        ss = "linked list : ";
        while(cur.next != None):
            ss+=str(cur.data)+"->";
            cur = cur.next;
        #last element
        ss += str(cur.data);
        return ss; 
    def str_reverse(self):
        if(self.isEmpty()):
            return "reverse : "
        cur = self.tail;
        ss = "reverse : ";
        while(cur.prev != None):
            ss += str(cur.data)+"->";
            cur = cur.prev;
        
        #first element
        ss += str(cur.data);
        return ss;
        
    def isEmpty(self):
        return self.head==None;
    def append(self, data):
        if(self.isEmpty()):
            newNode = Node(data);
            self.head = newNode;
            self.tail = newNode;
            return;
        newNode = Node(data);
        self.tail.next = newNode;
        newNode.prev = self.tail;
        self.tail = newNode;
    def insert(self, index, data):
        index = int(index);
        if(index<0):
            print("Data cannot be added");
            return;
        if(index>self.size()-1):
            print("Data cannot be added");
            return;
        #if insert at first index
        if(index == 0):
            print("index = {0} and data = {1}".format(index,data));
            newNode = Node(data);
            self.head.prev = newNode;
            newNode.next = self.head;
            self.head = newNode;
            return;
        #if insert at last index
        if(index == self.size()-1):
            print("index = {0} and data = {1}".format(index,data));
            newNode = Node(data);
            self.tail.prev.next = newNode;
            newNode.prev = self.tail.prev;
            newNode.next = self.tail;
            self.tail.prev = newNode;
            return;
        #if insert between first and last index
        pointer_Idx = 0;
        newNode = Node(data);
        cur = self.head;
        while(pointer_Idx<index-1):
            cur = cur.next;
        
        newNode.next = cur.next;
        cur.next.prev = newNode;
        newNode.prev = cur;
        cur.next = newNode;
        
    def append_before(self,data):
            newNode = Node(data);
            self.head.prev = newNode;
            newNode.next = self.head;
            self.head = newNode;
    
    def remove(self, data):
        if(self.isEmpty()):
            print("Not Found!");
            return;
        #if that data is the first index
        if(self.head.data == data):
            print("removed : {0} from index : 0".format(data));
            self.head = self.head.next;
            self.head.prev = None;
            return;
        #loop through to last index before that data(which want to be removed)
        cur = self.head;
        Idx = 0;
        while(cur != None):
            if(cur.data == data):
                #if that node of that data is last index
                if(cur == self.tail):
                    self.tail = cur.prev;
                    self.tail.next = None;
                    print("removed : {0} from index : {1}".format(data,Idx))
                    return;
                cur.prev.next = cur.next;
                cur.next.prev = cur.prev;
                print("removed : {0} from index : {1}".format(data,Idx))
            cur = cur.next;
            Idx+=1

        print("Not Found!");
    #prn
    def size(self):
        cur = self.head;
        size = 0;
        while(cur != None):
            size+=1;
            cur = cur.next;
        return size;

DLL = DoublyLinkedList();
inp = input("Enter Input : ").split(",");
for item in inp:
    order = item.split(" ");
    if(order[0]=="A"):
        DLL.append(order[1]);
    elif(order[0]=="Ab"):
        DLL.append_before(order[1]);
    elif(order[0]=="I"):
        data = order[1].split(":");
        DLL.insert(data[0],data[1]);
    elif(order[0]=="R"):
        DLL.remove(order[1]);

    #Display at each loop
    print(DLL);
    print(DLL.str_reverse());
    #print("prn -> "+order[0]);
