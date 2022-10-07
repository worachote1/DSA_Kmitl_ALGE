data = {'t': 2, 'h': 1, 'i': 1, 's': 1, 'a': 1, 'd': 2, 'e': 2, 'm': 1, '!': 1}

res = []

for item in data:
    for j in range(data[item]):
        res.append(item)

print(res)

a = []
ss = "e"
a.append(ss*3)
print(a)