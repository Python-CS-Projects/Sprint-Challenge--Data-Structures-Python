from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the sotrage is full
        if len(self.storage) == self.capacity:
            #check which element is the  oldest

            #overwrite the oldest element

            #inster the new element on the place of the oldest element

            pass
        # if is not full
        else:
            #insert to the tail until we reach max capacity
            pass

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
