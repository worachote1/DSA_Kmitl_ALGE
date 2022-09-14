# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    Fp = head
    Sp = head
    #reach overlap spot
    while(Fp != Sp):
        Fp = Fp.next;
        Sp = Sp.next.next
    #reset then shift Fp to origin of loop
    #Because distance from overlap spot to origin of loop = distance from head to origin of loop 
    Fp = head
    while(True):
        Fp = Fp.next
        Sp = Sp.next
        if(Fp==Sp):
            break;
    return Fp;