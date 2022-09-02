class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;

class DoublyLinkedlist:
    def __init__(self):
        self.head = Node("|");
    
    def __str__(self):
        if(self.isEmptty()):
            return "Empty";
        cur = self.head;
        ss="";
        while(cur!=None):
            ss+=cur.data+" ";
            cur=cur.next;
        
        return ss;

    def isEmptty(self):
        return self.head==None;
    
    def size(self):
        size = 0;
        cur = self.head;
        #count size for each element but not the one that data == "|"
        while(cur != None):
            size+=1;
            cur = cur.next;

        return size;
    
    def insertVim(self,data):
        # print("sa");
        if(self.size()==1):
            newNode = Node(data);
            newNode.next = Node("|");
            self.head = newNode;
            return;

        cur=self.head;
        tempPrev = None;
        newNode = Node(data);
        while(cur.data != "|"):
            tempPrev = cur;
            cur = cur.next;

        tempPrev.next = newNode;
        newNode.next = cur;

    def left_move(self):
        if(self.head.data == "|"):
            return;
        cur = self.head;
        tempPrev = None;
        while(cur.next.data != "|"):
            tempPrev = cur;
            cur = cur.next;
        
        if(tempPrev==None):
            if(cur.next.next == None):
                cur.next = None; #None
                self.head = Node("|");
                self.head.next = cur;
            elif(cur.next.next != None):
                cur.next = cur.next.next;
                self.head = Node("|");
                self.head.next = cur;                
            return;
        
        #print("Asd");
        newNode = Node("|");    
        tempPrev.next = newNode;
        newNode.next = cur;
        # delete duplicate |
        cur.next = cur.next.next;

    def right_move(self):
        cur = self.head;
        tempPrev = None;
        while(cur.data != "|"):
            tempPrev=cur;
            cur = cur.next;
        
        #if it's already most right
        if(cur.next == None):
            return;
        #if "|" is at left most
        if(tempPrev==None):
            self.head = cur.next;
        elif(tempPrev != None):
            tempPrev.next = cur.next;
        
        if(cur.next.next==None):
            newNode = Node("|");
            newNode.next = None;
            cur.next.next = newNode;
        elif(cur.next.next!=None):
            newNode = Node("|");
            newNode.next = cur.next.next ;
            cur.next.next=newNode;

    def remove_left(self):
        if(self.head.data == "|"):
            return;
        cur = self.head;
        tempPrev = None;
        newNode = Node("|");
        while(cur.next.data != "|"):
            tempPrev = cur;
            cur = cur.next;
        if(tempPrev==None):
            
            self.head = newNode;
        elif(tempPrev!=None):
            
            tempPrev.next = newNode

        if(cur.next.next == None):
            newNode.next = None;
        elif(cur.next.next != None):
            newNode.next = cur.next.next;

    def remove_right(self):
        cur = self.head;
        tempPrev = None;
        newNode = Node("|");
        while(cur.data != "|"):
            tempPrev = cur;
            cur = cur.next;
        
        if(cur.next == None):
            return;
        
        if(tempPrev==None):
            self.head=newNode;
        elif(tempPrev!=None):
            tempPrev.next = newNode;
        if(cur.next.next==None):
            newNode.next = None;
        elif(cur.next.next!=None):
            newNode.next = cur.next.next;

#
Vim = DoublyLinkedlist();
inp = input("Enter Input : ").split(",");
for item in inp:
    #print("Ddas");
    data = item.split(" ");
    if(data[0]=="I"):
        #print("data[1] -> ",data[1]);
        Vim.insertVim(data[1]);
    elif(data[0]=="L"):
        Vim.left_move();
    elif(data[0]=="R"):
        Vim.right_move();
    elif(data[0]=="B"):
        Vim.remove_left();
    elif(data[0]=="D"):
        Vim.remove_right();
    
    #print(item);

#display result after using Vim-text-Editer command
print(Vim);
#print("size -> ",Vim.size());
