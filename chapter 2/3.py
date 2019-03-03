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

def deleteNode(node):
    if not node or not node.next:
        return False
    nextn = node.next
    node.data = nextn.data
    node.next = nextn.next
    return True
list = buildtest()
list.LListprint()
node = list.head.next

deleteNode(node)
print("show new list")
list.LListprint()
