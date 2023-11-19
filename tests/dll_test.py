"""Test Cases for Doubly linked lists

"""
import sys
import os
import unittest

file_path = os.path.dirname(os.path.abspath(__file__).replace("tests",""))
sys.path.insert(0, file_path)

from src import *


class DoublyLinkedListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.node_1 = DoublyLinkedListNode(1)
        self.node_2 = DoublyLinkedListNode(2)
        self.node_3 = DoublyLinkedListNode(3)
        
        self.dll = DoublyLinkedList()
    
    def test_empty_dll(self):
        self.assertListEqual(self.dll.to_list(), [])

    def test_single_node_dll(self):
        self.dll.append_node(DoublyLinkedListNode(1))
        self.assertListEqual(self.dll.to_list(), [1])

    def test_two_node_dll(self):
        self.dll.append_node(DoublyLinkedListNode(1))
        self.dll.append_node(DoublyLinkedListNode(2))
        self.assertListEqual(self.dll.to_list(), [1,2])
    
    def test_append_value_dll(self):
        self.dll.append_node(DoublyLinkedListNode(1))
        self.dll.append_node(DoublyLinkedListNode(2))
        self.dll.append(DoublyLinkedListNode(3))
        self.dll.append(4)
        self.assertListEqual(self.dll.to_list(), [1,2,3,4])

    def test_prepend_node_dll(self):
        self.dll.prepend_node(DoublyLinkedListNode(1))
        self.dll.prepend_node(DoublyLinkedListNode(2))
        self.dll.prepend_node(DoublyLinkedListNode(3))
        self.dll.prepend(4)
        self.assertListEqual(self.dll.to_list(), [4,3,2,1])

    def test_insert_node_dll(self):
        self.dll.append_node(DoublyLinkedListNode(1))
        
        self.dll.insert_node(DoublyLinkedListNode(2),0)
        self.assertListEqual(self.dll.to_list(), [2,1])
        
        self.dll.insert_node(DoublyLinkedListNode(3),index=1)
        self.assertListEqual(self.dll.to_list(), [2,3,1])
        
        self.dll.insert_node(DoublyLinkedListNode(4),3)
        self.assertListEqual(self.dll.to_list(), [2,3,1,4])
        
        self.dll.insert_node(DoublyLinkedListNode(5),-1)
        self.assertListEqual(self.dll.to_list(), [2,3,1,5,4])
        
        self.dll.insert_node(DoublyLinkedListNode(6),-3)
        self.assertListEqual(self.dll.to_list(), [2,3,6,1,5,4])
        
        self.dll.insert_node(DoublyLinkedListNode(7),-10)
        self.assertListEqual(self.dll.to_list(), [7,2,3,6,1,5,4])
    
        self.dll.insert_node(DoublyLinkedListNode(8),10)
        self.assertListEqual(self.dll.to_list(), [7,2,3,6,1,5,4,8])

        self.dll.insert_node(DoublyLinkedListNode(9),8)
        self.assertListEqual(self.dll.to_list(), [7,2,3,6,1,5,4,8,9])
        
        self.dll.traverse()
        self.dll.traverse(reverse=True)
        
        self.assertTrue(self.dll.search(9))
        self.assertFalse(self.dll.search(10))
    
    def test_delete_dll(self):
        self.dll.prepend_node(DoublyLinkedListNode(1))
        self.dll.prepend_node(DoublyLinkedListNode(2))
        self.dll.prepend_node(DoublyLinkedListNode(3))
        self.dll.prepend(4)
        self.assertListEqual(self.dll.to_list(), [4,3,2,1])
        self.dll.delete(4)
        self.assertListEqual(self.dll.to_list(), [3,2,1])
        self.dll.delete(2)
        self.assertListEqual(self.dll.to_list(), [3,1])
        self.dll.delete(1)
        self.assertListEqual(self.dll.to_list(), [3])
        self.dll.delete(3)
        self.assertListEqual(self.dll.to_list(), [])
        self.dll.delete(3)
        self.assertListEqual(self.dll.to_list(), [])


if __name__ == '__main__':
    unittest.main()