class PrefixTree():
    def __init__(self) :
        self.children = {}
        self.isEndOfWord = False
    
x= {"a" : PrefixTree()}
 
print(list(x))
# del x["b"]
del x["a"]
print((x))