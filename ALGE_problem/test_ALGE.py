from operator import index, indexOf


blocks = [
    {
      "gym": False,
      "school": True,
      "store": False
    },
    {
      "gym": True,
      "school": False,
      "store": False
    },
    {
      "gym": True,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "school": True,
      "store": True
    }
  ];
reqs = ["gym", "school", "store"];

for item in blocks:
    print(item.keys())

print("444444444444444444444");
maxD = [float("inf") for block in blocks];
print(maxD);

n = len(blocks);
dice = [dict() for i in range(n)];
print(dice);


print(list(blocks[2].keys())[1]);

data = {'gym': [1, 0, 0, 1, 2], 'school': [0, 1, 0, 0, 0], 'store': [4, 3, 2, 1, 0]};
print(data.keys());
for item in data:
    print(data[item][2])

res = [4, 3, 2, 1, 2];
print(res.index(2))