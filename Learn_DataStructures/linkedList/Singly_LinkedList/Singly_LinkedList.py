class Node:
    def __init__(self,value=None):
        self.value = value;
        self.next = None;

class SLinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;

    def insert(self,value,location):
        newNode = Node(value);
        if (self.head is None):
            self.head = newNode;
            self.tail = newNode;
        else:
            #insert first
            if (location == 0):
                newNode.next = self.head;
                self.head = newNode;
            #insert last
            elif (location == -1):
                newNode.next = None;
                self.tail.next = newNode; #link between last node and newNode
                self.tail = newNode;
            #insert normal
            else:
                tempNode = self.head;
                index = 0;
                #will insert after location (location is 1,2,3,...)
                while(index<location-1):
                    tempNode = tempNode.next;
                    index+=1;

                nextNode = tempNode.next;
                tempNode.next = newNode;
                newNode.next = nextNode;
                # ? prn 
                if (tempNode == self.tail):
                    self.tail=newNode;

    def testDisplay(self):
        temp = self.head;
        while temp != None:
            print(temp.value);
            temp = temp.next;


sl = SLinkedList();


sl.insert(44,0);
sl.insert(213,1);
sl.insert(89,2);
sl.insert(37,3);
sl.insert(19,4);
sl.insert(26,2);


sl.testDisplay();

