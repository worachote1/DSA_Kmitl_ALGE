# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    P1 = headOne
    P2 = headTwo
    P1_prev = None;
    H1_Val = headOne.value;
    H2_Val = headTwo.value;
    while(P1 != None and P2 != None):
        if(P1.value <= P2.value):
            P1_prev = P1
            P1 = P1.next
        else:
            if(P1_prev == None):
                P1_prev = P2
                P2 = P2.next
                P1_prev.next = P1
            else:
                P1_prev.next = P2
                P1_prev = P2
                P2 = P2.next
                P1_prev.next = P1;
    if(P2 != None and P1 == None):
        P1_prev.next = P2
   
    return headOne if headOne.value<=headTwo.value else headTwo;
                
    