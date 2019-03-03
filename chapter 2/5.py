from LinkedList import Node
from LinkedList import SLinkedList

def buildtest():
    
    list = SLinkedList()
    list1 = SLinkedList()
    list.AtEnd(7)
    list.AtEnd(1)
    list.AtEnd(6)
    list1.AtEnd(5)
    list1.AtEnd(9)
    list1.AtEnd(2)
    
    # 71 + 102
    #33 + 332
   # list.LListprint()
    return list,list1
def padzero(list,total):
    while total != 0:
        list.Atbegining(0)
        total = total - 1
    return list
    
def ones_leading_add(list,list1):
    sum = SLinkedList()
    if list1.length() > list.length():
        list = padzero(list, list1.length() - list.length())
    elif list.length() > list1.length():
        list1 = padzero(list1, list.length() - list1.length())
    node = list.head
    node2 = list1.head
    while node:
        total = node.data + node2.data
        if total >= 10:
            total = total - 10
            
            # carry bit over
            if node.next:
                node.next.data = node.next.data + 1
            else:
                sum.AtEnd(1)
        sum.AtEnd(total)
        node = node.next
        node2 = node2.next
        
            
    return sum
def rev(list):
    node = list.head
    list = SLinkedList()
    while node:
        list.Atbegining(node.data)
        node = node.next
    
    
    return list
def leading_high_add(list,list1):
    list = rev(list)
    list1 = rev(list1)
    return rev(ones_leading_add(list,list1))
    
list,list1 = buildtest()
ones_leading_add(list,list1).LListprint()

