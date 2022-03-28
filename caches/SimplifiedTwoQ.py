import collections


class SimplifiedTwoQ:

    def __init__(self, k_am, k_a1):
        self.k_am = k_am
        self.k_a1 = k_a1

        self.am_queue = collections.deque([])
        self.am_set = set()

        self.a1_queue = collections.deque([])
        self.a1_set = set()

    def add(self, element):
        if element in self.am_set:
            self.am_queue.remove(element)
            self.am_queue.appendleft(element)
        elif element in self.a1_set:
            self.a1_queue.remove(element)
            self.a1_set.remove(element)

            self.am_queue.appendleft(element)
            self.am_set.add(element)
        else:
            if len(self.a1_queue) + len(self.am_queue) < self.k_am + self.k_a1:
                pass
            elif len(self.a1_queue) > self.k_a1:
                removed_element = self.a1_queue.pop()
                self.a1_set.remove(removed_element)
            else:
                removed_element = self.am_queue.pop()
                self.am_set.remove(removed_element)
            self.a1_queue.appendleft(element)
            self.a1_set.add(element)

    def cache(self, element):
        was_cached = element in self.am_set or element in self.a1_set
        self.add(element)
        return was_cached
