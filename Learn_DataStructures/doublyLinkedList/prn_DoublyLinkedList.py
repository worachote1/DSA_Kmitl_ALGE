from ctypes import DllCanUnloadNow


class Node:
    def __init__(self,value=None):
        self.value = value;
        self.next = None;
        self.prev = None;

class DoublyLinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
    
    def testDisplay(self):
        temp = self.head;
        if(temp == None):
            print("LinkedList not exist")
            exit();
        while temp != None:
            print(temp.value);
            temp = temp.next;

    #Create of Doubly LinkedList
    def createDLL(self,nodeValue):
        node = Node(nodeValue);
        node.prev = None;
        node.next = None;
        self.head = node;
        self.tail = node;
        return "prn create succ";
    def insert(self,nodeValue,location):
        if(self.head == None):
            print("The node cannot be inserted");
        else:
            newNode = Node(nodeValue);
            if(location==0):
                newNode.prev = None;
                newNode.next = self.head;
                self.head.prev = newNode;
                self.head = newNode;
            elif(location == -1):
                newNode.next = None;
                newNode.prev = self.tail;
                self.tail.next = newNode;
                self.tail = newNode;
            else:
                tempNode = self.head;
                index = 0;
                while index<location-1:
                    tempNode = tempNode.next;
                    index +=1;
                newNode.next = tempNode.next;
                tempNode.next.prev = newNode;
                newNode.prev = tempNode;
                tempNode.next = newNode;

    def search(self,nodeValue):
        if(self.head==None):
            return "There's no element exist"
        temp = self.head;
        index=0;
        while(temp!=None):
            if(temp.value==nodeValue):
                return "found at index "+str(index);
            temp = temp.next;
            index+=1;
        return "The node does not exist"
    
        # Delete a node from Doubly Linked List
    def deleteNode(self,location):
        if self.head is None:
            print("There is not any element in DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")

dLL = DoublyLinkedList();
print(dLL.createDLL(44));
dLL.insert(12,0);
dLL.insert(85,1);
dLL.testDisplay();
print(dLL.search(44))
        
a = 0.1;
b = 0.2;
c = (a*10+b*10)/10;
print(c);