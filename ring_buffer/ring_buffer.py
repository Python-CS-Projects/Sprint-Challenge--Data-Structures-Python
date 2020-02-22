from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if is not full
        if self.storage.length < self.capacity:
            # insert to the tail until we reach max capacity
            # add to tail already checks if the list is empty to add as head instead
            self.storage.add_to_tail(item)
            # set the current oldest as the head
            self.current = self.storage.head

        # if the sotrage is full
        elif self.storage.length == self.capacity:
            # check which element is the  oldest
            remove_head = self.storage.head
            # remove the oldest element
            self.storage.remove_from_head()
            # inster the new element on the place of the oldest element
            self.storage.add_to_head(item)

            # if the current is at the head
            if remove_head == self.current:
                # set as the tail
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
