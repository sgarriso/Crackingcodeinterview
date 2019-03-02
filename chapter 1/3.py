def urlify(link,length):
    newlink = ""
    counter = 0
    for char in link:
        if char == ' ' and counter < length:
            newlink = newlink + '%20'
        elif counter < length:
            newlink = newlink + char
        counter = counter + 1
    return newlink
print(urlify('MR JOHN SMITH    ',13))
        
            
