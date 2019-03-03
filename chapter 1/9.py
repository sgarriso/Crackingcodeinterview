#book best answer
def isrot(st1,st2):
    length = len(st1)
    if len(st2) == length and length > 0:
        st1st1 = st1 + st1
        return st2 in st1st1
    return False

# my soultion using sorting not ideal but quick
def isrot_not_ideal(st1,st2):
    st1 = ''.join(sorted(st1))
    st2 = ''.join(sorted(st2))
    return st1 in st2
print(isrot_not_ideal('waterbottle','erbottlewat'))
