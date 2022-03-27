import collections


class FIFO:

    def __init__(self, max_size):
        self.max_size = max_size

        self.double_linked_queue = collections.deque([])
        self.queue_set = set()

    def add(self, element):
        if element not in self.queue_set:
            if len(self.double_linked_queue) >= self.max_size:
                removed_element = self.double_linked_queue.pop()
                self.queue_set.remove(removed_element)

            self.double_linked_queue.appendleft(element)
            self.queue_set.add(element)

    def cache(self, element):
        was_cached = element in self.queue_set
        self.add(element)
        return was_cached
