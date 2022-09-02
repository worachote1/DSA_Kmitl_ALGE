def caesarCipherEncryptor(string, key):
    res = [];
    key = key%26;
    for item in string:
        newWord = ""
        if(ord(item)+key>ord('z')):
            newWord = chr(((ord(item)+key)%ord('z'))+ord('a')-1);

        else:
            newWord = chr(ord(item)+key);
        
        res.append(newWord);
    
    return "".join(res);

print(caesarCipherEncryptor("xyz",2));
print(caesarCipherEncryptor("abc",52));

print("prn -> ",(ord('a')+52)%ord('z'));