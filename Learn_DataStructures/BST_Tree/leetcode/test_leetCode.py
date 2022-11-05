import collections


s = "abcavaghc"

data = {}

for item in s :
    if(item not in data):
        data[item] = 1
        continue
    data[item]+=1

print(data)
print("EF")


for jj in data:
    print(data[jj])