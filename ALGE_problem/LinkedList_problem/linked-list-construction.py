# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if(self.head == None):
            self.head = node
            if(self.tail==None):
                self.tail = self.head
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            
    def setTail(self, node):
        if(self.tail==None):
            self.tail = node
            if(self.head==None):
                self.head = self.tail
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    def insertBefore(self, node, nodeToInsert):
        currentNode = self.head
        while(currentNode != None):
            if(currentNode.value == node.value):
                if(currentNode.prev == None):
                    #currentNode is head 
                    currentNode.prev = nodeToInsert
                    self.head = nodeToInsert
                    self.head.next = currentNode
                else:
                    #not done
                    currentNode.prev.next = nodeToInsert
                    nodeToInsert.prev = currentNode.prev
                    nodeToInsert.next = currentNode
                    currentNode.prev = nodeToInsert

            currentNode = currentNode.next        

    def insertAfter(self, node, nodeToInsert):
        currentNode = self.head;
        while(currentNode != None):
            if(currentNode.value == node.value):
                if(currentNode.next == None):
                    #currentNode is tail 
                    currentNode.next = nodeToInsert
                    self.tail = nodeToInsert
                    self.tail.prev = currentNode
                else:
                    currentNode.next.prev = nodeToInsert
                    nodeToInsert.next = currentNode.next
                    currentNode.next = nodeToInsert
                    nodeToInsert.prev = currentNode

            currentNode = currentNode.next

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if(position==1):
            if(self.head==None):
                self.head = nodeToInsert;
                if(self.tail==None):
                    self.tail = nodeToInsert;
            else:
                nodeToInsert.next = self.head
                self.head = nodeToInsert
            return;

        currentNode = self.head;
        count = 1;
        while(True):
           if(count==position-1):
                nodeToInsert.next = currentNode.next
                currentNode.next.prev = nodeToInsert
                
                nodeToInsert.prev = currentNode
                currentNode.next = nodeToInsert
                return;

           currentNode = currentNode.next
           count += 1 

    def removeNodesWithValue(self, value):
        # remove all node with value
        currentNode = self.head
        if(currentNode==None):
            return
        while(currentNode != None):
            if(currentNode.next.value == value):
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next

    def remove(self, node):
        # remove existing node with value
        currentNode = self.head
        if(currentNode==None):
            return
        while(currentNode != None):
            if(currentNode.next == node):
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next

    def containsNodeWithValue(self, value):
        currentNode = self.head;
        if(currentNode==None):
            return False
        while(currentNode!=None):
            if(currentNode.value == value):
                return True
            currentNode = currentNode.next
        return False