# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    newLL = head
    cur = head
    prev = None
    while(cur != None):
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    
    return prev
