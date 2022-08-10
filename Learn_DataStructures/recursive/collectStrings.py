def collectStrings(obj):
    res  = [];
    for key in obj:
        if(type(obj[key]) is str):
            res.append(obj[key]);
        if(type(obj[key]) is dict):
            res=res + collectStrings(obj[key]);
    
    return res;


obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collectStrings(obj)) # ['foo', 'bar', 'baz']

# for key in obj:
#     print(obj[key]);