class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None


class Dlist:
    def __init__(self):
        self.head = None

    def list_print(self):
        """Prints linked list from the head to tail, while the Node is not None"""
        value = self.head
        while value is not None:
            print(value.data)
            value = value.next

    def add_to_start(self, data):
        new_item = Node(data)
        if self.head is None:
            self.head = new_item
        else:
            self.head.prev = new_item
            new_item.next = self.head
            self.head = new_item

    def add_to_end(self, data):
        new_item = Node(data)
        if self.head is None:
            self.head = new_item
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_item
            new_item.prev = temp

    def add_by_data(self, after, data):
        new_item = Node(data)
        if self.head is None:
            self.head = new_item
        else:
            temp = self.head
            while temp.data != after:
                temp = temp.next
            new_item.next = temp.next
            temp.next = new_item
            new_item.prev = temp

    def del_start(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next.prev = None
            temp.next = None

    def del_item_by_data(self, after):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        elif self.head.data == after:
            to_delete = self.head.next
            self.head.next = to_delete.next
            to_delete.next.prev = self.head
            to_delete.next = None
            to_delete.prev = None
            to_delete = None
        else:
            temp = self.head
            while temp is not None and temp.data != after:
                temp = temp.next
            to_delete = temp.next
            temp.next = to_delete.next
            if to_delete.next is not None:
                to_delete.next.prev = temp
            to_delete.next = None
            to_delete.prev = None
            to_delete = None

    def del_list(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            while self.head:
                to_delete = self.head
                self.head = self.head.next
                to_delete.next = None
                to_delete = None

dllist = Dlist()
dllist.add_to_start("Monday")
dllist.add_to_start("Thursday")
dllist.add_to_end("Wednesday")
dllist.add_by_data("Monday", "Thursday")
dllist.del_start()
dllist.del_end()
dllist.del_list()
dllist.list_print()
