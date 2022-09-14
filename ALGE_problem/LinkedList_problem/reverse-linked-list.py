# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    Fp = None;
    Sp = head
    while(Sp != None):
        temp = Sp.next
        Sp.next = Fp
        Fp = Sp
        Sp = temp
    return Fp
