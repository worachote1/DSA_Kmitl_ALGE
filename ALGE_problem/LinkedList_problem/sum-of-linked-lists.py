class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    resLinkedList = LinkedList(-44)
    curRes = resLinkedList;
    curOne = linkedListOne
    curTwo = linkedListTwo
    carry = 0
    while(curOne != None or curTwo != None):
        sum = 0;
        sum += (curOne.value if curOne != None else 0); 
        sum += (curTwo.value if curTwo != None else 0); 
        sum += carry

        newNode = LinkedList(sum%10);
        curRes.next = newNode;
        curRes = newNode;
        carry = 1 if sum>=10 else 0;

        curOne = curOne.next if curOne != None else None;
        curTwo = curTwo.next if curTwo != None else None;

    if(carry==1):
        newNode = LinkedList(carry);
        curRes.next = newNode;

    return resLinkedList.next
