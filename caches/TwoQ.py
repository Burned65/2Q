import collections


class TwoQ:

    def __init__(self, k_in, k_out, k_am):
        self.k_in = k_in
        self.k_out = k_out
        self.k_am = k_am

        self.am = collections.deque([])
        self.am_set = set()

        self.a1_in = collections.deque([])
        self.a1_in_set = set()

        self.a1_out = collections.deque([])
        self.a1_out_set = set()

    def add(self, element):
        if element in self.am_set:
            self.am.remove(element)
            self.am.appendleft(element)
        elif element in self.a1_out_set:
            self.reclaim()
            self.am.appendleft(element)
            self.am_set.add(element)
        elif element in self.a1_in_set:
            pass
        else:
            self.reclaim()
            self.a1_in.appendleft(element)
            self.a1_in_set.add(element)

    def reclaim(self):
        if len(self.a1_in) + len(self.a1_out) + len(self.am) < self.k_in + self.k_out + self.k_am:
            pass
        elif len(self.a1_in) > self.k_in:
            removed_element = self.a1_in.pop()
            self.a1_in_set.remove(removed_element)

            self.a1_out.appendleft(removed_element)
            self.a1_out_set.add(removed_element)
            if len(self.a1_out) > self.k_out:
                removed_element = self.a1_out.pop()
                self.a1_out_set.remove(removed_element)
        else:
            removed_element = self.am.pop()
            self.am_set.remove(removed_element)

    def cache(self, element):
        was_cached = (element in self.am_set) or (element in self.a1_in_set)
        self.add(element)
        return was_cached
