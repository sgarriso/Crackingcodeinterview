from LinkedList import Node
from LinkedList import SLinkedList
def buildtest():
    
    list = SLinkedList()
    list.Atbegining("2")
    list.Atbegining("2")
    list.Atbegining("5")
    list.Atbegining("2")
   # list.LListprint()
    return list
def kth_last(head,k):
    kth = ""
    if not head:
        return 0,kth
    index,kth = kth_last(head.next,k)
    index = index + 1
    if index == k:
        kth=(head.data)
        #print(kth)
    return index,kth
def wrapper(list,kth):
    index,kth=kth_last(list.head, 3)
    return kth
list = buildtest()
print(wrapper(list, 3))
