x = {1:2,2:3}
def vb(data : dict):
    data[1]-=1
    print(data)

vb(x)
print(x)