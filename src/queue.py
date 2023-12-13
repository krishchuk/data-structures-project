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
        self.all = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        self.all.append(data)
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
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ""
        else:

            all_data = '\n'.join(self.all)
            return all_data
