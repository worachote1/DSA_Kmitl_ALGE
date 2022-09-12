# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    
    currentNode = linkedList;

    while(currentNode.next != None):
        if(currentNode.value==currentNode.next.value):
            currentNode.next=currentNode.next.next        
        else:
            currentNode = currentNode.next
    return linkedList