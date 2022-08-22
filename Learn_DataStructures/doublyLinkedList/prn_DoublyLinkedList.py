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

dLL = DoublyLinkedList();
print(dLL.createDLL(44));
dLL.insert(12,0);
dLL.insert(85,1);
dLL.testDisplay();
print(dLL.search(48))
        