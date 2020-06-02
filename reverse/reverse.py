class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        if node is None and prev is None:
            return
        else:
            if node.next_node is None:
                self.head = node
                node.next_node = prev
                return

            nxt = node.next_node
            node.next_node = prev
            self.reverse_list(nxt, node)


    # prints and test
    def show_results(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.get_next()

result = LinkedList()
result.add_to_head(2)
result.add_to_head(4)
result.add_to_head(6)
result.add_to_head(8)
result.show_results()
result.reverse_list(result.head, None)