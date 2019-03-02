def edits(typo,correct):
    dict_typo = build_letter_count(typo)
    dict_correct = build_letter_count(correct)
    return compare(dict_typo,dict_correct)
def diff(a, b):
    a=set(a)
    b= set(b)
    
    return list(a.difference(b) )
def compare(dict_typo,dict_correct):
    # check keys
    check = 0
    if len(diff(dict_typo.keys(),dict_correct.keys())) > 2:
        return False
    for key in dict_typo.keys():
        if key not in dict_correct.keys():
            dict_correct[key] = 0
        
        if abs(dict_typo[key] - dict_correct[key]) > 0:
            check = check + 1
    if check > 1:
        return False
    else:
        return True
            
    
def build_letter_count(word):
    answer = {}
    for c in word:
        if c in answer.keys():
            answer[c] = answer[c] + 1
        else:
            answer[c] = 1
    return answer

print(edits('pale','ple'))
