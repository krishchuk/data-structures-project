"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        # self.assertIs(len(self.queue.all), 0)
        self.queue.enqueue('data1')
        self.assertIs(self.queue.head.data, "data1")
        self.assertIsNone(self.queue.head.next_node)
        self.assertIsNone(self.queue.tail)
        self.queue.enqueue('data2')
        self.assertIs(self.queue.head.data, "data1")
        self.assertIs(self.queue.head.next_node.data, 'data2')
        self.assertIs(self.queue.tail.data, 'data2')
        self.queue.enqueue('data3')
        self.assertIs(self.queue.head.data, "data1")
        self.assertIs(self.queue.head.next_node.data, 'data2')
        self.assertIs(self.queue.tail.data, 'data3')

    def test___str__(self):
        self.assertMultiLineEqual(str(self.queue), '')
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertMultiLineEqual(str(self.queue), 'data1\ndata2\ndata3')
