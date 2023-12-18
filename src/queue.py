class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""



    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next_node:
                last = last.next_node

            last.next_node = node
            self.tail = last.next_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head:
            del_head = self.head.data
            new_head = self.head.next_node
            self.head = new_head
            return del_head
        return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ""
        head = self.head
        all_data = []
        while head:
            all_data.append(head.data)
            head = head.next_node
        return '\n'.join(all_data)
