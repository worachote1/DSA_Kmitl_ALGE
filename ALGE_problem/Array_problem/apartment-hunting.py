from array import array


def apartmentHunting(blocks, reqs):
    
  data = {};
  #set data of request
  for item in reqs:
    data[item] = [float("inf")  for i in range(len(blocks))];
  
  #cal from left to right
  for item in reqs:
    for i in range(len(blocks)):
      #if that block already have a item that request
      if(blocks[i][item]==True):
        data[item][i]=0;
      
      #if item that requested not in that block then sum up distance with left side value
      elif(i>0 and blocks[i][item] != True):
        data[item][i] = data[item][i-1]+1;
  
  #cal from right to left
  for item in reqs:
    for i in range(len(blocks)-1,-1,-1):
      #if that block already have a item that request
      if(blocks[i][item]==True):
        data[item][i]=0;
      
      #if item that requested not in that block then sum up distance with right side value
      elif(i<len(blocks)-1 and blocks[i][item] != True):
        data[item][i] = min(data[item][i+1]+1,data[item][i]);  
          
  #prn test print
  print(data);
  # {'gym': [1, 0, 0, 1, 2], 'school': [0, 1, 0, 0, 0], 'store': [4, 3, 2, 1, 0]}
  
  #cal result
  res = [];
  for i in range(len(blocks)):
    maxVal = float("-inf");
    for item in data:
      if(maxVal<data[item][i]):
        maxVal = data[item][i];
    res.append(maxVal);
  
  #print("res -> ",res);
  #res ->  [4, 3, 2, 1, 2]

  return res.index(min(res));

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

print(apartmentHunting(blocks,reqs));