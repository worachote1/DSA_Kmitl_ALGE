# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    Idx_remove = findLenght(head) - k
    #if remove the head node
    if(Idx_remove==0):
        temp = head.next
        head.value = head.next.value
        head.next = head.next.next
        temp.next = None
        return     
    #shift to node before the one that wanted to remove
    cur = head
    count = 0
    while(count<Idx_remove-1):
        count+=1
        cur = cur.next
    #remove
    cur.next = cur.next.next

def findLenght(head):
    cur = head;
    count = 0;
    while(cur != None):
        count+=1;
        cur = cur.next
    return count