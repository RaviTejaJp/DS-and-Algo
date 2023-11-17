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

    def test_append_value_cll(self):
        self.cll.append_node(SinglyLinkedListNode(1))
        self.cll.append_node(SinglyLinkedListNode(2))
        self.cll.append(SinglyLinkedListNode(3))
        self.cll.append(4)
        self.assertListEqual(self.cll.to_list(), [1,2,3,4])


    def test_prepend_node_cll(self):
        self.cll.prepend_node(SinglyLinkedListNode(1))
        self.cll.prepend_node(SinglyLinkedListNode(2))
        self.cll.prepend_node(SinglyLinkedListNode(3))
        self.cll.prepend(4)
        self.assertListEqual(self.cll.to_list(), [4,3,2,1])
    
    def test_insert_node_cll(self):
        self.cll.append_node(SinglyLinkedListNode(1))
        
        self.cll.insert_node(SinglyLinkedListNode(2),0)
        self.assertListEqual(self.cll.to_list(), [2,1])
        
        self.cll.insert_node(SinglyLinkedListNode(3),1)
        self.assertListEqual(self.cll.to_list(), [2,3,1])
        
        self.cll.insert_node(SinglyLinkedListNode(4),3)
        self.assertListEqual(self.cll.to_list(), [2,3,1,4])
        
        self.cll.insert_node(SinglyLinkedListNode(5),-1)
        self.assertListEqual(self.cll.to_list(), [2,3,1,5,4])
        
        self.cll.insert_node(SinglyLinkedListNode(6),-3)
        self.assertListEqual(self.cll.to_list(), [2,3,6,1,5,4])
        
        self.cll.insert_node(SinglyLinkedListNode(7),-10)
        self.assertListEqual(self.cll.to_list(), [7,2,3,6,1,5,4])
    
        self.cll.insert_node(SinglyLinkedListNode(8),10)
        self.assertListEqual(self.cll.to_list(), [7,2,3,6,1,5,4,8])

        self.cll.insert_node(SinglyLinkedListNode(9),8)
        self.assertListEqual(self.cll.to_list(), [7,2,3,6,1,5,4,8,9])


    def test_insert_cll(self):
        self.cll.append(1)
        
        self.cll.insert(2,0)
        self.assertListEqual(self.cll.to_list(), [2,1])
        
        self.cll.insert(3,1)
        self.assertListEqual(self.cll.to_list(), [2,3,1])
        
        self.cll.insert(4,3)
        self.assertListEqual(self.cll.to_list(), [2,3,1,4])
        
        self.cll.insert(5,-1)
        self.assertListEqual(self.cll.to_list(), [2,3,1,5,4])
        
        self.cll.insert(6,-3)
        self.assertListEqual(self.cll.to_list(), [2,3,6,1,5,4])
        
        self.cll.insert(7,-10)
        self.assertListEqual(self.cll.to_list(), [7,2,3,6,1,5,4])
    
        self.cll.insert(8,10)
        self.assertListEqual(self.cll.to_list(), [7,2,3,6,1,5,4,8])

        self.cll.insert(9,8)
        self.assertListEqual(self.cll.to_list(), [7,2,3,6,1,5,4,8,9])


if __name__ == '__main__':
    unittest.main()