def build_letter_count(word):
    answer = {}
    for c in word:
        if c in answer.keys():
            answer[c] = answer[c] + 1
        else:
            answer[c] = 1
    return answer
def dict_check(data):
    # if more than one odd word return false
    check = 0
    for key in data.keys():
        if data[key] % 2 == 1:
            check = check + 1
    if check > 1:
        return False
    return True
def panper(word):
    dict_word = build_letter_count(word)
    return dict_check(dict_word)

print(panper('aawsaa'))
    
