from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the storage is full remove before appending
        if len(self.storage) == self.capacity:
            # Set item as current value
            self.current.value = item
            # if current value is the tail
            if self.current == self.storage.tail:
                print("Tail")
                # the next will be the head so set it as current value
                self.current = self.storage.head
            else:
                self.current = self.current.next
        # if the storage is not yet full
        else:
            # add item to the tail
            self.storage.add_to_tail(item)
            # if we have only one item set it as the current item
            if len(self.storage) == 1:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # set the current value
        current_value = self.storage.head
        # while the current is not none which means is at the tail
        while current_value is not None:
            # append to list
            list_buffer_contents.append(current_value.value)
            # set current to next to keep moving
            current_value = current_value.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
