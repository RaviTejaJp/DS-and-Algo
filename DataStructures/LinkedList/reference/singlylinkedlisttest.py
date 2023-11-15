from __future__ import annotations

import logging
import unittest

from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import SinglyLinkedListNode

logging.basicConfig(level=logging.INFO)


class TestSinglyLinedListNode(unittest.TestCase):
    def test_sll_node(self):
        test_node = SinglyLinkedListNode(data=1)
        self.assertEqual(1, test_node.data)
        self.assertIsNone(test_node.next)

    def test_next_setter(self):
        # Case 1
        with self.assertRaises(TypeError) as context:
            test_node = SinglyLinkedListNode(data=1, next=2)

        exception = context.exception
        self.assertIn(
            'Next value must be a SinglyLinkedListNode or None not', str(
                exception,
            ),
        )

        # Case 2
        with self.assertRaises(TypeError) as context:
            SinglyLinkedListNode(data=1).next = 2

        exception = context.exception
        self.assertIn(
            'Next value must be a SinglyLinkedListNode or None not', str(
                exception,
            ),
        )

    def test_str_method(self):
        node = SinglyLinkedListNode(10)
        result = str(node)
        expected = f'SinglyLinkedListNode Containing:[10, None]'
        self.assertEqual(result, expected)

    def test_repr_method(self):
        node = SinglyLinkedListNode(10)
        result = repr(node)
        expected = f'<SinglyLinkedListNode: [10, None]>'
        self.assertEqual(result, expected)

    def test_equal_method(self):
        node1 = SinglyLinkedListNode(10)
        node2 = SinglyLinkedListNode(10)
        node3 = SinglyLinkedListNode(11)
        node4 = SinglyLinkedListNode(data=10, next=node2)
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.sll = SinglyLinkedList()

    def test_sll_creation(self):
        self.assertIsNone(self.sll.head)
        self.assertIsNone(self.sll.tail)
        self.assertEqual(0, self.sll.length)

    def test_append_node(self):
        data_to_append = 1
        node_to_append = SinglyLinkedListNode(data=data_to_append)

        length_before_append = len(self.sll)
        data_before = list(self.sll)

        self.sll.append_node(node_to_append)

        data_after = self.sll.to_list()
        length_after_append = self.sll.length

        data_before.append(data_to_append)
        expected = data_before

        self.assertEqual(length_before_append + 1, length_after_append)
        self.assertListEqual(expected, data_after)

    def test_append(self):
        data_to_append = 1

        length_before_append = len(self.sll)
        data_before = list(self.sll)

        self.sll.append(data_to_append)

        data_after = self.sll.to_list()
        length_after_append = self.sll.length

        data_before.append(data_to_append)
        expected = data_before

        self.assertEqual(length_before_append + 1, length_after_append)
        self.assertListEqual(expected, data_after)

    def test_prepend_node(self):
        data_to_prepend = 1
        node_to_prepend = SinglyLinkedListNode(data=data_to_prepend)

        length_before_prepend = len(self.sll)
        data_before = list(self.sll)

        self.sll.prepend_node(node_to_prepend)

        data_after = self.sll.to_list()
        length_after_prepend = self.sll.length

        data_before.insert(0, data_to_prepend)
        expected = data_before

        self.assertEqual(length_before_prepend + 1, length_after_prepend)
        self.assertListEqual(expected, data_after)

    def test_prepend(self):
        data_to_prepend = 1

        length_before_prepend = len(self.sll)
        data_before = list(self.sll)

        self.sll.append(data_to_prepend)

        data_after = self.sll.to_list()
        length_after_prepend = self.sll.length

        data_before.insert(0, data_to_prepend)
        expected = data_before

        self.assertEqual(length_before_prepend + 1, length_after_prepend)
        self.assertListEqual(expected, data_after)

    def test_insert_node(self):
        data_to_insert = 1
        node_to_insert = SinglyLinkedListNode(data=data_to_insert)
        self.sll.append(SinglyLinkedListNode(0))
        self.sll.append(SinglyLinkedListNode(10))
        self.sll.append(SinglyLinkedListNode(20))
        length_before_insert = len(self.sll)
        data_before = list(self.sll)

        self.sll.insert_node(node_to_insert, length_before_insert-1)

        data_after = self.sll.to_list()
        length_after_insert = self.sll.length

        data_before.insert(length_before_insert-1, data_to_insert)
        expected = data_before

        self.assertEqual(length_before_insert + 1, length_after_insert)
        self.assertListEqual(expected, data_after)

    def test_insert(self):
        data_to_insert = 1
        self.sll.append(SinglyLinkedListNode(0))
        self.sll.append(SinglyLinkedListNode(10))
        self.sll.append(SinglyLinkedListNode(20))

        length_before_insert = len(self.sll)
        data_before = list(self.sll)

        self.sll.insert(data_to_insert, length_before_insert-1)

        data_after = self.sll.to_list()
        length_after_insert = self.sll.length

        data_before.insert(length_before_insert-1, data_to_insert)
        expected = data_before

        self.assertEqual(length_before_insert + 1, length_after_insert)
        self.assertListEqual(expected, data_after)


if __name__ == '__main__':
    unittest.main()
