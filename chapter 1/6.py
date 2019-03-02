def stringcompress(word):
    newword = ""
    pos = 0
    counter = 1
    print(len(word))
    while pos < len(word):
        char = word[pos]
        while pos < len(word)-1 and  word[pos] == word[pos+1]:
            counter = counter + 1
            pos = pos + 1   
        if counter > 1:
            newword = newword + char+ str(counter)
            counter = 1
        else:
            newword = newword + char 
        pos = pos + 1 
            
            
   
    return newword
print(stringcompress('AAAAbbbAAA2232Ssss'))

