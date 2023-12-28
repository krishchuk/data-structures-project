"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_insert_beginning(self):
        self.assertIsNone(self.ll.head)
        self.ll.insert_beginning({'id': 1})
        self.assertIs(self.ll.head.data['id'], 1)
        self.ll.insert_beginning({'id': 0})
        self.assertIs(self.ll.head.data['id'], 0)
        self.assertIs(self.ll.head.next_node.data['id'], 1)

    def test_insert_at_end(self):
        self.assertIsNone(self.ll.head)
        self.ll.insert_at_end({'id': 2})
        self.assertIs(self.ll.tail.data['id'], 2)
        self.ll.insert_at_end({'id': 3})
        self.assertIs(self.ll.tail.data['id'], 3)

    def test___str__(self):
        self.assertMultiLineEqual(str(self.ll), 'None')
        self.ll.insert_beginning({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 1})
        self.assertMultiLineEqual(str(self.ll), "{'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        self.assertMultiLineEqual(str(self.ll), 'None')
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.assertMultiLineEqual(str(self.ll.to_list()), "[{'id': 1, 'username': 'lazzy508509'}]")
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertMultiLineEqual(str(self.ll.to_list()),
                                  "[{'id': 0, 'username': 'serebro'}, "
                                  "{'id': 1, 'username': 'lazzy508509'}, "
                                  "{'id': 2, 'username': 'mik.roz'}, "
                                  "{'id': 3, 'username': 'mosh_s'}]")

    def test_get_data_by_id(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertMultiLineEqual(str(self.ll.get_data_by_id(3)), "{'id': 3, 'username': 'mosh_s'}")

    def test_get_data_by_id_error(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end('idusername')
        self.ll.insert_at_end([1, 2, 3])
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertRaises(self.ll.get_data_by_id(2), AttributeError)

