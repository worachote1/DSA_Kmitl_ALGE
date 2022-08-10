print("*** Reading E-Book ***");
x, y = input("Text , Highlight : ").split(",")

for text in x:
    if(text!=y):
        print(text,end="")
    else:
        print("[",end="")
        print(text,end="")
        print("]",end="")