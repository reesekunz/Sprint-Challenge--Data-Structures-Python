from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Still room in DLL storage - Add item to head (defining head as newest element and tail as oldest)
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            # newly added item becomes current
            self.current = self.storage.head
        # DLL storage is at capacity. Need to make room - remove from tail then add to head
        elif self.storage.length == self.capacity:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)
            if self.storage.head == self.current:
                self.current = self.storage.tail
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # while list is not empty
        while self.storage.length > 0:
            list_buffer_contents.append(self.storage.head.value)
            self.storage.head = self.storage.head.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
