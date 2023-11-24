class MinStack(object):
    
    def __init__(self):
        self.q = []
        self.minArr = []

    def push(self, val):
        self.q.append(val)
        if(not len(self.minArr)):
            minVal = float('inf')
        else:
            minVal = self.minArr[-1]
        if(val <= minVal):
            self.minArr.append(val)

    def pop(self):
        if(not len(self.q)):
            return None
        val = self.q.pop()
        if(not len(self.minArr)):
            return None
        if(val == self.minArr[-1]):
            self.minArr.pop()
        return val
    
    def top(self):
        if(not len(self.q)):
            return None       
        return self.q[-1]    
        
    def getMin(self):
        return self.minArr[-1]
        
minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
# minStack.getMin();
minStack.pop();
minStack.top();   
# minStack.getMin(); 