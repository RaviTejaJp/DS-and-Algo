"""Test Cases for Circular linked lists

"""
import unittest

from DS_and_Algo.DataStructures.LinkedList.nodes import SinglyLinkedListNode


class TestCircularLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.node_1 = SinglyLinkedListNode(1)
        self.node_2 = SinglyLinkedListNode(2)
        self.cll = CircularSinglyLinkedList()
    
    def empty_cll_test(self):
        self.assertListEqual(self.cll.to_list(), [])
