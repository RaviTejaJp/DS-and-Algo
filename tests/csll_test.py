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


    def test_insert_search_traverse_cll(self):
        self.cll.traverse()
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
        
        self.cll.traverse()
        
        self.assertTrue(self.cll.search(9))
        self.assertFalse(self.cll.search(10))
    
    def test_getter(self):
        with self.assertRaises(IndexError):
            self.cll[0]
        
        self.cll.append(1)
        self.assertEqual(self.cll[0],1)
        self.assertEqual(self.cll[-1],1)
        with self.assertRaises(IndexError):
            self.assertEqual(self.cll[1],1)
            self.assertEqual(self.cll[-2],1)
        
        self.cll.append(2)
        self.assertEqual(self.cll[0],1)
        self.assertEqual(self.cll[-2],1)
        
        self.assertEqual(self.cll[-1],2)
        self.assertEqual(self.cll[1],2)
        
        
        with self.assertRaises(IndexError):
            self.assertEqual(self.cll[2],2)
            self.assertEqual(self.cll[-3],1)
        
    def test_setter(self):
        with self.assertRaises(IndexError):
            self.cll[0] = 1
        self.cll.append(1)
        self.assertEqual(self.cll[0],1)
        self.cll[0] = 100
        self.assertEqual(self.cll[0],100)

        with self.assertRaises(IndexError):
            self.cll[1] = 1
    
    def test_pop_value(self):
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        self.cll.append(4)
        
        self.assertListEqual(self.cll.to_list(), [1,2,3,4])
        self.cll.pop_value(5)
        self.assertListEqual(self.cll.to_list(), [1,2,3,4])
        self.cll.pop_value(3)
        self.assertListEqual(self.cll.to_list(), [1,2,4])
        self.cll.pop_value(1)
        self.assertListEqual(self.cll.to_list(), [2,4])
        self.cll.pop_value(4)
        self.assertListEqual(self.cll.to_list(), [2])
        self.cll.pop_value(2)
        self.assertListEqual(self.cll.to_list(), [])
        self.cll.pop_value(2)
        self.assertListEqual(self.cll.to_list(), [])


    def test_pop_first(self):
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        self.cll.append(4)

        self.assertListEqual(self.cll.to_list(), [1,2,3,4])
        self.cll.pop_first()
        self.assertListEqual(self.cll.to_list(), [2,3,4])
        self.cll.pop_first()
        self.assertListEqual(self.cll.to_list(), [3,4])
        self.cll.pop_first()
        self.assertListEqual(self.cll.to_list(), [4])
        self.cll.pop_first()
        self.assertListEqual(self.cll.to_list(), [])
        self.cll.pop_first()
        self.assertListEqual(self.cll.to_list(), [])

    def test_pop(self):
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)
        self.cll.append(4)

        self.assertListEqual(self.cll.to_list(), [1,2,3,4])
        self.cll.pop()
        self.assertListEqual(self.cll.to_list(), [1,2,3])
        self.cll.pop()
        self.assertListEqual(self.cll.to_list(), [1,2])
        self.cll.pop()
        self.assertListEqual(self.cll.to_list(), [1])
        self.cll.pop()
        self.assertListEqual(self.cll.to_list(), [])
        self.cll.pop()
        self.assertListEqual(self.cll.to_list(), [])



if __name__ == '__main__':
    unittest.main()