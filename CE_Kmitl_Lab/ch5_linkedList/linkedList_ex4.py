from calendar import c
from unittest.mock import NonCallableMagicMock


class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;
        self.prev = None;

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
        return self.head.data == "|";
    
    def size(self):
        size = 0;
        cur = self.head;
        #count size for each element but not the one that data == "|"
        while(cur != None):
            if(cur.data == "|"):
                cur = cur.next;
                continue;
            size+=1;
            cur = cur.next;

        return size;
    
    def insertVim(self,data):
        cur=self.head;
        #move to "|" element
        while(cur.data != "|"):
            cur = cur.next;
        
        #After insert element shift "|" to be next after newNode
        newNode = Node(data);
        if(cur.next == None):
            if(cur.prev==None):
                newNode.prev = None;
                newNode.next = cur;
                cur.prev = newNode;
                #
                self.head = newNode;
            elif(cur.prev != None):   
                cur.prev.next = newNode;
                newNode.prev = cur.prev;
                newNode.next = cur;
                cur.prev = newNode;
                #cur.next = None;

        elif(cur.next !=None):
            if(cur.prev==None):
                newNode.prev = None;
                newNode.next = cur;
                cur.prev = newNode;
                #
                self.head = newNode;
            elif(cur.prev!=None):
                cur.prev.next = newNode;
                newNode.prev = cur.prev;
                newNode.next = cur;
                cur.prev = newNode;
        
       # print("play insert");
        

    def left_move(self):
        cur=self.head;
        #move to "|" element
        while(cur.data != "|"):
            cur = cur.next;
        
        #if element before "|" is None then remain the same
        if(cur.prev==None):
            return;
        
        # shift to left but check condition
        if(cur.next==None):
            pass;




#
Vim = DoublyLinkedlist();
inp = input("Enter Input : ").split(",");
for item in inp:
    #print("Ddas");
    data = item.split(" ");
    if(data[0]=="I"):
        print("data[1] -> ",data[1]);
        Vim.insertVim(data[1]);
    elif(data[0]=="L"):
        Vim.left_move();
    elif(data[0]=="R"):
        Vim.right_move();
    elif(data[0]=="B"):
        Vim.remove_left();
    elif(data[0]=="D"):
        Vim.remove_right();

#display result after using Vim-text-Editer command
print(Vim);
print("size -> ",Vim.size());
