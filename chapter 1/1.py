def is_unique_no_data(data):
    char_pos= 0
    while char_pos <  len(data):
        check = char_pos-1
        if check == -1:
            check =  0
        else:
            check = char_pos-1
        check_end = char_pos+1
        if check_end == len(data):
            check_end = len(data)
        else:
            check_end = char_pos+1
        print(data[0:check] + data[check_end:])
        if data[char_pos] in data[0:check] + data[check_end:]:
            return False
        char_pos = char_pos + 1
    
    
    return True
print(is_unique_no_data(''))
