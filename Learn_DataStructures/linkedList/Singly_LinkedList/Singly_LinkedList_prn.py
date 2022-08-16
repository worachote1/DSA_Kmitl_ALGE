from asyncio.proactor_events import _ProactorBaseWritePipeTransport

#Class for Node
class Node:
    def __init__(self,value=None):
        self.value = value;
        self.next = None;


#Class for SLinkedList
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
                self.tail = newNode;
            #insert last
            elif (location == -1):
                newNode.next = None;
                self.tail.next = newNode; #link between last node and newNode
                self.tail = newNode;
            #insert normal
            else:
                tempNode = self.head;
                index = 0;
                #will insert before location (which is 1,2,3,...)
                while(index<location-1):
                    tempNode = tempNode.next;
                    index+=1;

                nextNode = tempNode.next;
                tempNode.next = newNode;
                newNode.next = nextNode;
                
                #check if need to set tail
                if (tempNode == self.tail):
                    self.tail=newNode;

    def testDisplay(self):
        temp = self.head;
        if(temp == None):
            print("LinkedList not exist")
            exit();
        while temp != None:
            print(temp.value);
            temp = temp.next;
    
    def search(self,value):
        temp = self.head;
        if(temp is None):
            return "LinkedList not exist"
            
        index=0;
        while(temp != None):
            if(value==temp.value):
                return "found "+str(value)+" at index = "+str(index);
            temp = temp.next;
            index+=1;
        
        return "Not found "+str(value)+" in this LinkedList";

    def delete(self,location):
        if(self.head == None):
            print("LinkedList not exist prn");
            exit();
        #if remove first element
        if(location==0):
            #if linkedList have only one element
            if(self.head is self.tail):
                self.head=None;
                self.tail=None;
                print("location 0 and head = none prn");
            else:
                self.head = self.head.next;
                print("location 0 and head NOT none prn");
        #if remove last element
        elif(location==-1):
            #if linkedList have only one element
            if(self.head == self.tail):
                self.head=None;
                self.tail=None;
                print("location -1 and head = none prn");
            else:
                print("location -1 and head NOT none prn");
                temp = self.head;
                #find element before last node
                print("ssH");
                while(temp != None):
                    print("l3ald");
                    if(temp.next==self.tail):
                        print("trav prn");
                        break;
                    temp = temp.next;
            
                temp.next = None;
                self.tail = temp;
        #if remove element between head and tail
        else:
            temp = self.head;
            index = 0;
            while(index<location-1):
                temp = temp.next;
                index+=1;

            nextNode = temp.next;
            temp.next = nextNode.next;

    #delete entire LinkedList
    def deleteAll(self):
        if(self.head is None):
            print("LinkedList not exist already");
        else:
            self.head = None;
            self.tail= None;

singlyLinkedList = SLinkedList();
singlyLinkedList.insert(1, 1)
singlyLinkedList.insert(2, 1)
singlyLinkedList.insert(3, 1)
singlyLinkedList.insert(4, 2)
singlyLinkedList.insert(5,-1)
#singlyLinkedList.deleteNode(1);
singlyLinkedList.delete(-1);
singlyLinkedList.testDisplay();
#default : [1, 4, 3, 2, 5]

