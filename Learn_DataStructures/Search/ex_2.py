#first greater value

def search_firstGreater(data : list,val : int):
    for item in sorted(data):
        if(item>val):
            return str(item)
    return "No First Greater Value"
        
inp = input("Enter Input : ").split("/")
data = [int(item) for item in inp[0].split(" ")]
val_search = [int(item) for item in inp[1].split(" ")]

for item in val_search:
    print(search_firstGreater(data,item))
