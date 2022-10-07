#solution 1
# def minimumCharactersForWords(words):
#     data = {}
#     for item in words:
#         temp_data = {}
#         for index in range(len(item)):
#             if(item[index] not in data):
#                 data[item[index]]=1
#                 temp_data[item[index]]=1
#             else:
#                 if(item[index] in temp_data):
#                     temp_data[item[index]]+=1
#                     # print("temp in ale")
#                 else:
#                     # print("temp not in")
#                     temp_data[item[index]] = 1
                
#             data[item[index]] = max(temp_data[item[index]],data[item[index]])

#     res = []
#     for item in data:
#         for j in range(data[item]):
#             res.append(item) 

#     return res                


#solution 2

def minimumCharactersForWords(words):
    data = {}
    for item in words:
        countChar_data = countChar(item)
        data = update_data(countChar_data,data)
    
    # print(data)
    #display output
    res = []
    for item in data:
        for j in range(data[item]):
            res.append(item)
    return res

def countChar(word):
    data = {}
    for item in word:
        if(item not in data):
            data[item]=1
        else:
            data[item]+=1
    return data

def update_data(countChar_data,data):
    if(data == {}):
        data = countChar_data
        return data
    
    for item in countChar_data:
        if(item not in data):
            data[item]=countChar_data[item]
            continue
        
        maxCount = max(data[item],countChar_data[item])
        data[item]=maxCount
    
    return data
    
    
words= ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(words))