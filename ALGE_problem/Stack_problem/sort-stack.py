def sortStack(stack):
    if(len(stack)==0):
        return [];
    top = stack.pop();
    sortStack(stack);
    insert_In_sortedOrder(stack,top);

    return stack

def insert_In_sortedOrder(stack,val):
    if(len(stack)==0):
        stack.append(val);
        return;
    if(stack[-1]<=val):
        stack.append(val);
        return;
    
    topInSorted = stack.pop();
    insert_In_sortedOrder(stack,val);
    stack.append(topInSorted);

arr1 = [-5, 2, -2, 4, 3, 1];
print(sortStack(arr1))
