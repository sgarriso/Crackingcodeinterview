from LinkedList import Node
from LinkedList import SLinkedList

def buildtest():
    
    list = SLinkedList()
    list1 = SLinkedList()
    list.AtEnd(2)
    list.AtEnd(2)
    list.AtEnd(2)
    list1.AtEnd(5)
    list1.AtEnd(9)
    list1.AtEnd(1)
    
    # 71 + 102
    #33 + 332
   # list.LListprint()
    return list,list1

def find_intersection(llist1, llist2):
    if (llist1.head is None or llist2.head is None):
        return False
 
    intersection = SLinkedList()
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        data = current1.data
        while current2:
            if current2.data == data:
                #node = Node(data)
                intersection.AtEnd(data)
                break
            current2 = current2.next
        current1 = current1.next
    #remove_duplicates(intersection)
 
    return intersection.length() > 0
list,list1 = buildtest()
print(find_intersection(list,list1))
