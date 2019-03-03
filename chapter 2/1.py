from LinkedList import Node
from LinkedList import SLinkedList
def buildtest():
    
    list = SLinkedList()
    list.Atbegining("Sun")
    list.Atbegining("Sun")
    list.Atbegining("Sun")
    list.Atbegining("Mon")
    list.Atbegining("Sun")
    list.Atbegining("Mon")
    list.Atbegining("2")
    list.Atbegining("2")
    list.Atbegining("5")
    list.Atbegining("2")
    #list.LListprint()
    return list
def removedups_withoutbuffer(List):
    if not List.head:
        return List
    node = List.head
    data = node.data
    while node:
        perv = node
        check = node.next
        while check:
            if check.data == data:
                # remove check
                perv.next = check.next
            else:
                perv = perv.next
            check = check.next
        node = node.next
        if node:
            data = node.data
            
        
    return List
def removedups(List):
    new_list = SLinkedList()
    check_list = []
    node = List.head
    while  node:
        if node.data not in check_list:
            new_list.AtEnd(node.data)
            check_list.append(node.data)
        node = node.next
    return new_list
list = buildtest()
list.LListprint()
print("remove dups")
list = removedups_withoutbuffer(list)
list.LListprint()


