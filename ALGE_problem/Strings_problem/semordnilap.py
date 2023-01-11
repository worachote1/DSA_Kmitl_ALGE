def semordnilap(words):
    # Write your code here.
    res = []
    data = []
    for item in words:
        if(item[::-1] in data):
            res.append([item,item[::-1]])
        if(item not in data):
            data.append(item)
    return res

print(semordnilap(["dog", "desserts", "god", "stressed"]))
print(semordnilap(["aaa", "bbbb"]))