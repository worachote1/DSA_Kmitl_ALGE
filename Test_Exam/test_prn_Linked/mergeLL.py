# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def mergeLinkedLists(headOne, headTwo):
        p_One = headOne
        p_Two = headTwo
        prevOne = None

        while(p_One != None and p_Two != None):
            if(p_One.value <= p_Two.value):
                prevOne = p_One
                p_One = p_One.next
            elif(p_Two.value < p_One.value):
                if(prevOne == None):
                    prevOne = p_Two
                    prevOne.next = p_One
                    p_Two = p_Two.next
                else:
                    prevOne.next = p_Two
                    prevOne = p_Two
                    p_Two = p_Two.next
                    prevOne.next = p_One
            
        if(p_Two != None and p_One == None):
            prevOne.next = p_Two
        
        return headOne if (headOne.value <= headTwo.value) else headTwo


                
            

        

