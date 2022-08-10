class TorKham :
    
    ### Enter Your Code Here ###
    def __init__(self):
        self.words = []
    
    def restart(self):
        ###Enter Your Code For Add Number###
        self.words = []
        return "game restarted";

    def play(self, word):
        
        ###Enter Your Code For Div Number###
        if(word=="X"):
            return "game over"
        elif(len(self.words)==0):
            self.words.append(word)
        else:
            lastWord = self.words[len(self.words)-1];
            if(lastWord[len(lastWord)-2:len(lastWord)].lower()!=word[0:2].lower()):
                return "game over"
        
            else:
                self.words.append(word)
        ss="["
        for i in range(len(self.words)):
                ss+="'"+self.words[i]+"'"
                if(i!=len(self.words)-1):
                    ss+=", "
        ss+="]"
        return "'"+word+"'"+" -> "+ss;

       


torkham = TorKham()
print("*** TorKham HanSaa ***")
s = input("Enter Input : ").split(',')
# print(s[1][len(s[1])-2:len(s[1])]);
### Enter Your Code Here ###
for i in range(s):
    if(s[i][0]=="P"):
        torkham.play(s[i][2:])
    if(s[i][0]=="R"):
        print(torkham.restart);
    if(s[i][0]=="X"):
        print(torkham.play(s[i][0]));
print(torkham.words);