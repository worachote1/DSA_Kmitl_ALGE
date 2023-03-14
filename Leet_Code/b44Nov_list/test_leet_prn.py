j = ['aa','bb','cc']
while j!=[]:
    word = input()
    j = [item for item in j.copy()] if word not in j else [item for item in j.copy() if item != word]
    
        