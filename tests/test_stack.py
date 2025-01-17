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

    def test_pop(self):
        stack1 = Stack()
        stack1.push('data1')
        stack1.push('data2')
        del_data = stack1.pop()
        self.assertIs(stack1.top.data, 'data1')
        self.assertIs(del_data, 'data2')
        stack2 = Stack()
        stack2.push('dataaa')
        del_data2 = stack2.pop()
        self.assertIs(stack2.top, None)
        self.assertIs(del_data2, 'dataaa')

    def test___str__(self):
        stack3 = Stack()
        self.assertMultiLineEqual(str(stack3), "Пустой стэк")
        stack3.push(1)
        self.assertMultiLineEqual(str(stack3), "Вершина стэка: 1")
        stack3.push('2')
        self.assertMultiLineEqual(str(stack3), "Вершина стэка: 2")
