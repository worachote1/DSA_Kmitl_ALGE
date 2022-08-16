#   Created by Elshad Karimov on 27/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in Linked List
    # def insertSLL(self, value, location):
    #     newNode = Node(value)
    #     if self.head is None:
    #         self.head = newNode
    #         self.tail = newNode
    #     else:
    #         if location == 0:
    #             newNode.next = self.head
    #             self.head = newNode
    #         elif location == -1:
    #             newNode.next = None
    #             self.tail.next = newNode
    #             self.tail = newNode
    #         else:
    #             tempNode = self.head
    #             index = 0
    #             while index < location - 1:
    #                 if tempNode.next == None:
    #                     break 
    #                 tempNode = tempNode.next
    #                 index += 1
    #             nextNode = tempNode.next
    #             tempNode.next = newNode
    #             newNode.next = nextNode
    #             if tempNode == self.tail:
    #                 self.tail=newNode
    def insertSLL(self, value, location):
            newNode = Node(value)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                if location == 0:
                    newNode.next = self.head
                    self.head = newNode
                elif location == -1:
                    newNode.next = None
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                    if tempNode == self.tail:
                        self.tail=newNode
    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    #  Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    print("location 0 and head = none prn");
                else:
                    self.head = self.head.next
                    print("location 0 and head NOT none prn");
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    print("location -1 and head = none prn");
                else:
                    print("location -1 and head NOT none prn");
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None

    #my delete prn
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
                while(temp == None):
                    if(temp.next==self.tail):
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

            nextNode = temp.next;
            temp.next = nextNode.next;

    def testDisplay(self):
        temp = self.head;
        if(temp == None):
            print("LinkedList not exist")
            exit();
        while temp != None:
            print(temp.value);
            temp = temp.next;

singlyLinkedList = SLinkedList()
# singlyLinkedList.insertSLL(1, 1)
# singlyLinkedList.insertSLL(2, 3)
# singlyLinkedList.insertSLL(3, 1)
# singlyLinkedList.insertSLL(4, 1)
# singlyLinkedList.insertSLL(0, 0)
# singlyLinkedList.insertSLL(7, -1)
# singlyLinkedList.insertSLL(5, 6)


# singlyLinkedList.insertSLL(1,1)
# singlyLinkedList.insertSLL(2,5)
# singlyLinkedList.insertSLL(3,1)
# singlyLinkedList.insertSLL(4,9)
# singlyLinkedList.insertSLL(5,-1)
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(5,-1)
#singlyLinkedList.deleteNode(1);
singlyLinkedList.delete(0);
singlyLinkedList.testDisplay();
#default : [1, 4, 3, 2, 5]
print([node.value for node in singlyLinkedList]) 
# singlyLinkedList.deleteEntireSLL()
# print([node.value for node in singlyLinkedList]) 






