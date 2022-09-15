class node:
    def __init__(self,data,next = None ):
        self.data = data;
    def __str__(self):
        pass;
def createList(l=[]):
    LL = node(-44);
    cur = LL;
    for i in range(len(l)):
        newNode = node(int(l[i]))
        cur.next = newNode
        cur = cur.next 

    cur.next = None;

    return LL.next

def printList(H):
    ss=""
    cur = H
    while(cur != None):
        ss+=str(cur.data)+" ";
        cur = cur.next
    print(ss)

def mergeOrderesList(p,q):
    QP = q
    PP = p
    PP_prev = None
    while(PP != None and QP != None):
        if(PP.data <= QP.data):
            PP_prev = PP
            PP = PP.next
        elif(PP.data > QP.data):
            if(PP_prev == None):
                PP_prev = QP
                QP = QP.next
                PP_prev.next = PP
            else:
                PP_prev.next = QP
                PP_prev = QP
                QP = QP.next
                PP_prev.next = PP
    
    if(PP == None and QP != None):
        PP_prev.next = QP
    
    return p if p.data <= q.data else q; 
#################### FIX comand ####################   
# input only a number save in L1,L2
inp = input("Enter 2 Lists : ").split(" ");
L1 = inp[0].split(",");
L2 = inp[1].split(",");

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)