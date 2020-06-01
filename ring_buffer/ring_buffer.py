from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.old_node = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
           self.storage.add_to_tail(item)
           self.old_node = self.storage.head
           
        elif not self.old_node.next:
               self.old_node.value = item
               self.old_node = self.storage.head
               
        else:    
            self.old_node.value = item
            self.old_node = self.old_node.next     

    def get(self):
        empty_array = []
        
        current = self.storage.head
        while current:
            empty_array.append(current.value)
            current = current.next
        return empty_array