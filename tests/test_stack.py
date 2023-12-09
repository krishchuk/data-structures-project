"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push("data")
        self.assertIs(self.stack.top.data, "data")
        self.assertIsNone(self.stack.top.next_node)
        self.stack.push("new_data")
        self.assertIs(self.stack.top.data, "new_data")
        self.assertIs(self.stack.top.next_node.data, "data")
        self.stack.push("again_new_data")
        self.assertIs(self.stack.top.data, "again_new_data")
        self.assertIs(self.stack.top.next_node.data, "new_data")
        self.assertIs(self.stack.top.next_node.next_node.data, "data")
