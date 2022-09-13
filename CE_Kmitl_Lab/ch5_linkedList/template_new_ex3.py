class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
        pass
    def __str__(self):
        ### Code Here ###
        pass

def createList(l=[]):
    ### Code Here ###
    pass

def printList(H):
    ### Code Here ###
    pass

def mergeOrderesList(p,q):
    ### Code Here ###
    pass

#################### FIX comand ####################   
# input only a number save in L1,L2
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)