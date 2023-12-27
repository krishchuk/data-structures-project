class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.data_list = []

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.tail:
            self.tail.next_node = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        self.data_list = []
        node = self.head
        while node:
            self.data_list.append(node.data)
            node = node.next_node
        return self.data_list

    def get_data_by_id(self, id_key):
        data_list = self.to_list()
        for item in range(len(data_list)):
            try:
                for value in self.data_list[item].values():
                    if value == id_key:
                        return self.data_list[item]
            except (TypeError, AttributeError):
                print('Данные не являются словарем или в словаре нет id.')
