from LinkedList import Node
from LinkedList import SLinkedList
def buildtest():
    
    list = SLinkedList()
    list.Atbegining("Sun")
    list.Atbegining("Mon")
    list.Atbegining("Mon")
    #list.LListprint()
    return list
def removedups_withoutbuffer(head):
    return head
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
list = removedups(list)
list.LListprint()


