
from LinkedList import Node
from LinkedList import SLinkedList

def buildtest():
    
    list = SLinkedList()
    list.AtEnd(3)
    list.AtEnd(5)
    list.AtEnd(8)
    list.AtEnd(5)
    list.AtEnd(10)
    list.AtEnd(2)
    list.AtEnd(1)
    #list.LListprint()
    return list
def part(node,x):
    head = node
    tail = node
    while  node:
        next = node.next

        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head
        
        
list=buildtest()
head=(part(list.head,5))
while head:
    print(head.data)
    head = head.next
    
