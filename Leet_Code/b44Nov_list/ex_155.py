class MinStack:
    
    def __init__(self):
        self.q = []
        self.min = [float('inf')]

    def push(self, val: int) :
        newData = min(val,self.min[-1])
        self.min.append(newData)
        self.q.append(val)

    def pop(self) :
        self.min.pop()
        return self.q.pop()

    def top(self) :
        return self.q[-1]

    def getMin(self) :
        return self.min[-1]
        