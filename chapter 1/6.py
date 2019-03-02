def stringcompress(word):
    newword = ""
    pos = 0
    counter = 1
    check = False
    while pos < len(word):
        char = word[pos]
        while pos < len(word)-1 and  word[pos] == word[pos+1]:
            counter = counter + 1
            pos = pos + 1   
        if counter > 0:
            newword = newword + char+ str(counter)
            if counter > 1:
                check = True
            counter = 1
        #else:
            #newword = newword + char 
        pos = pos + 1
    if check:
        return newword
    return word
    
    
            
            
   
print(stringcompress('aabBBBBcccc'))

