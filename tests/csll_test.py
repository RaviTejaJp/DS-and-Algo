"""Test Cases for Circular linked lists

"""
import unittest

from src.datastructures.linkedlist.nodes import SinglyLinkedListNode
from src.datastructures.linkedlist.circularsinglylinkedlist import CircularSinglyLinkedList


class TestCircularLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.node_1 = SinglyLinkedListNode(1)
        self.node_2 = SinglyLinkedListNode(2)
        self.cll = CircularSinglyLinkedList()
    
    def empty_cll_test(self):
        self.assertListEqual(self.cll.to_list(), [])
