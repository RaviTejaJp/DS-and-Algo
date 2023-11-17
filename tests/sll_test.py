"""Test Cases for Circular linked lists

"""
import sys
import os
import unittest

file_path = os.path.dirname(os.path.abspath(__file__).replace("tests",""))
sys.path.insert(0, file_path)

from src import *


class SinglyLinkedListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.node_1 = SinglyLinkedListNode(1)
        self.node_2 = SinglyLinkedListNode(2)
        self.node_3 = SinglyLinkedListNode(3)
        
        self.sll = SinglyLinkedList()
    
    def test_empty_sll(self):
        self.assertListEqual(self.sll.to_list(), [])

    def test_single_node_sll(self):
        self.sll.append_node(SinglyLinkedListNode(1))
        self.assertListEqual(self.sll.to_list(), [1])

    def test_two_node_sll(self):
        self.sll.append_node(SinglyLinkedListNode(1))
        self.sll.append_node(SinglyLinkedListNode(2))
        self.assertListEqual(self.sll.to_list(), [1,2])

    def test_append_value_sll(self):
        self.sll.append_node(SinglyLinkedListNode(1))
        self.sll.append_node(SinglyLinkedListNode(2))
        self.sll.append(SinglyLinkedListNode(3))
        self.sll.append(4)
        self.assertListEqual(self.sll.to_list(), [1,2,3,4])


    def test_prepend_node_sll(self):
        self.sll.prepend_node(SinglyLinkedListNode(1))
        self.sll.prepend_node(SinglyLinkedListNode(2))
        self.sll.prepend_node(SinglyLinkedListNode(3))
        self.sll.prepend(4)
        self.assertListEqual(self.sll.to_list(), [4,3,2,1])
    
    def test_insert_node_sll(self):
        self.sll.append_node(SinglyLinkedListNode(1))
        
        self.sll.insert_node(SinglyLinkedListNode(2),0)
        self.assertListEqual(self.sll.to_list(), [2,1])
        
        self.sll.insert_node(SinglyLinkedListNode(3),1)
        self.assertListEqual(self.sll.to_list(), [2,3,1])
        
        self.sll.insert_node(SinglyLinkedListNode(4),3)
        self.assertListEqual(self.sll.to_list(), [2,3,1,4])
        
        self.sll.insert_node(SinglyLinkedListNode(5),-1)
        self.assertListEqual(self.sll.to_list(), [2,3,1,5,4])
        
        self.sll.insert_node(SinglyLinkedListNode(6),-3)
        self.assertListEqual(self.sll.to_list(), [2,3,6,1,5,4])
        
        self.sll.insert_node(SinglyLinkedListNode(7),-10)
        self.assertListEqual(self.sll.to_list(), [7,2,3,6,1,5,4])
    
        self.sll.insert_node(SinglyLinkedListNode(8),10)
        self.assertListEqual(self.sll.to_list(), [7,2,3,6,1,5,4,8])

        self.sll.insert_node(SinglyLinkedListNode(9),8)
        self.assertListEqual(self.sll.to_list(), [7,2,3,6,1,5,4,8,9])


    def test_insert_sll(self):
        self.sll.append(1)
        
        self.sll.insert(2,0)
        self.assertListEqual(self.sll.to_list(), [2,1])
        
        self.sll.insert(3,1)
        self.assertListEqual(self.sll.to_list(), [2,3,1])
        
        self.sll.insert(4,3)
        self.assertListEqual(self.sll.to_list(), [2,3,1,4])
        
        self.sll.insert(5,-1)
        self.assertListEqual(self.sll.to_list(), [2,3,1,5,4])
        
        self.sll.insert(6,-3)
        self.assertListEqual(self.sll.to_list(), [2,3,6,1,5,4])
        
        self.sll.insert(7,-10)
        self.assertListEqual(self.sll.to_list(), [7,2,3,6,1,5,4])
    
        self.sll.insert(8,10)
        self.assertListEqual(self.sll.to_list(), [7,2,3,6,1,5,4,8])

        self.sll.insert(9,8)
        self.assertListEqual(self.sll.to_list(), [7,2,3,6,1,5,4,8,9])


if __name__ == '__main__':
    unittest.main()