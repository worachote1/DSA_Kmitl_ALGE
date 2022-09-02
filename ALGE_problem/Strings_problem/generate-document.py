def generateDocument(characters, document):

    data = {};

    for item in characters:
        if(item not in data.keys()):
            data[item] = 1;
        #    print(item," -> ",data[item]);
            continue;
        
        data[item]+=1;
        #print(item," -> ",data[item]);

    #print(data);
    
    for item in document:
        if(item not in data.keys()):
            return False;
        
        data[item]-=1;
        if(data[item]<0):
            return False;
 
    return True

characters = "Bste!hetsi ogEAxpelrt x ";
document = "AlgoExpert is the Best!";
print(generateDocument(characters,document));