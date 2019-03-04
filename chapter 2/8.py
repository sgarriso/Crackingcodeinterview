from LinkedList import Node
from LinkedList import SLinkedList

def buildtest():
    
    list = SLinkedList()
    list1 = SLinkedList()
    list.AtEnd(2)
    #list.AtEnd(25)
    list.head.next = Node(20)
   # list.head.next.next = list.head.next
    
    # 71 + 102
    #33 + 332
    #list.LListprint()
    return list
def findloop(list):
    slow = list.head
    fast = list.head
    while fast  and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast == None  or  fast.next == None:
        return None
    slow = list.head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return fast
list=buildtest()
print(findloop(list))

