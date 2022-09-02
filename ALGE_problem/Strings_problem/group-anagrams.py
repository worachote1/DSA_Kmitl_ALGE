def groupAnagrams(words):

    data = {};
    for item in words:
        change_to_sort = "".join(sorted(item));
        if(change_to_sort not in data.keys()):
            data[change_to_sort]=[item];
            continue;
        data[change_to_sort].append(item);
    
    #print(data);
    return list(data.values());

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"];
print(groupAnagrams(words));