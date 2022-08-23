dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print(dict);
ss = "Age"
print(dict.get(ss));

n =   [["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]]


# print(list(dict.keys()));

#set
for i in range(len(n)):
    for j in range(len(n[0])):
        if(n[i][j] not in list(dict.keys())):
            dict[n[i][j]] = 0;

print("After change dict : ");
print(dict)
print(dict.items());
print("-----------------------------");
for key,val in dict.items():
    print(key);
print(0%1);