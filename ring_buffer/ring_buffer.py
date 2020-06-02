from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.old_node = None
        self.storage = DoublyLinkedList()

    # This overwrites the old node with new by adding it to the tail
    def append(self, item):
        if len(self.storage) < self.capacity:
           self.storage.add_to_tail(item)
           self.old_node = self.storage.head

         # When the capacity has been reached it checks for next
         # If not next sets old node(current) to equal to item
        elif not self.old_node.next:
               self.old_node.value = item
               self.old_node = self.storage.head

        # Set the old node equal to item, moves current node to next and replaces that value
        else:    
            self.old_node.value = item
            self.old_node = self.old_node.next     

    def get(self):
        # Empty array
        array = []
        # Sets value to head
        current = self.storage.head
        # Loops though and appends to current value and moves the current to the next node
        while current:
            array.append(current.value)
            current = current.next
        return array