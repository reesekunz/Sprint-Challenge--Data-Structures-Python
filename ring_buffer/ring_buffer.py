from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Checking to see if storage is at capacity
        if self.storage.length == self.capacity:
            # remove tail (defining head as newest and tail as oldest)
            self.storage.remove_from_tail()
            self.storage.length -= 1
        # Adding item to head (newest)
        self.storage.add_to_head(item)
        # update length
        self.storage.length += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        while self.storage.length > 0:
            if self.storage.head is not None:
                list_buffer_contents.append(self.storage.head.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
