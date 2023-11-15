from __future__ import annotations

from SinglyLinkedList import *

node1 = SinglyLinkedListNode(1)
node2 = SinglyLinkedListNode(2)
node3 = SinglyLinkedListNode(3)
node4 = SinglyLinkedListNode(4)
node5 = SinglyLinkedListNode(5)
node6 = SinglyLinkedListNode(6)
node7 = SinglyLinkedListNode(7)
node8 = SinglyLinkedListNode(8)
node9 = SinglyLinkedListNode(9)
# print(node1)
# node1.next = node2
# print(node1)
# node2.next = node3
# print(repr(node1))


sll = SinglyLinkedList()
sll2 = SinglyLinkedList()

sll.append_node(node1)
sll.append_node(node2)
sll.prepend_node(node3)

# 3 -> 1 -> 2
print(sll == sll2)

sll.insert_node(node=node4, index=0)
# 4 -> 3 -> 1 -> 2

sll.insert_node(node=node5, index=sll.length)
# 4 -> 3 -> 1 -> 2 -> 5

sll.insert_node(node=node6, index=sll.length+2)
# 4 -> 3 -> 1 -> 2 -> 5 -> 6

sll.insert_node(node=node7, index=-1)
# 4 -> 3 -> 1 -> 2 -> 5 -> 7 -> 6

sll.insert_node(node=node8, index=-1*sll.length)
# 8 -> 4 -> 3 -> 1 -> 2 -> 5 -> 7 -> 6

sll.insert_node(node=node9, index=-1*sll.length)
# 9 -> 8 -> 4 -> 3 -> 1 -> 2 -> 5 -> 7 -> 6
sll.reverse()
print(sll)
