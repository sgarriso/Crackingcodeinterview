from LinkedList import Node
from LinkedList import SLinkedList

def buildtest():
    
    list = SLinkedList()
    list1 = SLinkedList()
    list.AtEnd(2)
    list.AtEnd(1)
    list.AtEnd(2)
    list1.AtEnd(5)
    list1.AtEnd(9)
    list1.AtEnd(2)
    
    # 71 + 102
    #33 + 332
   # list.LListprint()
    return list
def compare(list,list1):
    if list.length() != list1.length():
        return False
    else:
        node = list.head
        node1 = list1.head
        while node:
            if node.data != node1.data:
                return False
            node = node.next
            node1 = node1.next
        return True
def pan(list):
    list1 = list.rev()
    list1.LListprint()
    
    return compare(list,list1)
print(pan(buildtest()))
