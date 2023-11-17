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

if __name__ == '__main__':
    unittest.main()