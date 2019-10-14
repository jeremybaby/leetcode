class MovingAverage1_1:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.queue = []
        for _ in range(size):
            self.queue.append(0)
        self.len = 0
        self.size = size

    def next(self, val):
        if self.len < self.size:
            self.queue[self.len] = val
            self.len += 1
            return sum(self.queue) / self.len
        else:
            self.queue[:-1] = self.queue[1:]
            self.queue[-1] = val
            return sum(self.queue) / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

import collections
class MovingAverage1_2:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.len = 0
        self.size = size

    def next(self, val):
        if self.len < self.size:
            self.queue.append(val)
            self.len += 1
            return sum(self.queue) / self.len
        else:
            self.queue.popleft()
            self.queue.append(val)
            return sum(self.queue) / self.size

class MovingAverage1_3:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.sum = 0
        self.size = size

    def next(self, val):
        self.queue.append(val)
        self.sum += val

        while len(self.queue) > self.size:
            top = self.queue.popleft()
            self.sum -= top

        return self.sum / len(self.queue)


class MovingAverage1_4:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size

    def next(self, val):
        if len(self.queue) == self.size:
            self.queue.pop(0)

        self.queue.append(val)

        return sum(self.queue) / len(self.queue)
