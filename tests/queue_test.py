"""Test Cases for Queue

"""
import sys
import os
import unittest

file_path = os.path.dirname(os.path.abspath(__file__).replace("tests",""))
sys.path.insert(0, file_path)

from src import *

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_empty_queue(self):
        self.assertListEqual(self.queue.to_list(), [])
    
    def test_queue_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.assertListEqual(self.queue.to_list(), [1,2,3,4])
    
    def test_queue_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.assertListEqual(self.queue.to_list(), [1,2,3,4])
        self.assertEqual(self.queue.dequeue(),1)
        self.assertEqual(self.queue.dequeue(),2)
        self.assertEqual(self.queue.dequeue(),3)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.dequeue(),4)
        self.assertFalse(self.queue.isEmpty())
        self.assertEqual(self.queue.dequeue(),5)
        self.assertTrue(self.queue.isEmpty())
        self.assertListEqual(self.queue.to_list(),[])
    
    def test_neg_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()
            self.queue.peek()
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(),1)
        self.assertEqual(self.queue.dequeue(),1)
        with self.assertRaises(IndexError):
            self.queue.dequeue()
            self.queue.peek()


class CircularQueueTest(unittest.TestCase):
    def setUp(self):
        self.cq = CircularQueue(capacity=5)
    
    def test_empty_circular_queue(self):
        self.assertTrue(self.cq.isEmpty())
    
    def test_enqueue_dequeue_cq(self):
        self.cq.enqueue(1)
        self.assertFalse(self.cq.isEmpty())
        self.assertEqual(self.cq.dequeue(),1)
        self.assertTrue(self.cq.isEmpty())
        self.cq.enqueue(1)
        self.cq.enqueue(2)
        self.cq.enqueue(3)
        self.cq.enqueue(4)
        self.cq.enqueue(5)
        self.cq.dequeue()
        self.cq.enqueue(1)
        self.assertListEqual(list(self.cq), [2,3,4,5,1])





if __name__ == "__main__":
    unittest.main()