"""Test Cases for Circular linked lists

"""
import sys
import os
import unittest

file_path = os.path.dirname(os.path.abspath(__file__).replace("tests",""))
sys.path.insert(0, file_path)

from src import *


class CircularLinkedListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.node_1 = SinglyLinkedListNode(1)
        self.node_2 = SinglyLinkedListNode(2)
        self.node_3 = SinglyLinkedListNode(3)
        
        self.cll = CircularSinglyLinkedList()
    
    def test_empty_cll(self):
        self.assertListEqual(self.cll.to_list(), [])

    def test_single_node_cll(self):
        self.cll.append_node(SinglyLinkedListNode(1))
        self.assertListEqual(self.cll.to_list(), [1])

    def test_two_node_cll(self):
        self.cll.append_node(SinglyLinkedListNode(1))
        self.cll.append_node(SinglyLinkedListNode(2))
        self.assertListEqual(self.cll.to_list(), [1,2])


if __name__ == '__main__':
    unittest.main()