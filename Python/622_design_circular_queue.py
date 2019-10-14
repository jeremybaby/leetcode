class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        # 队列长度
        self._len = k
        self._elems = [0] * self._len
        # 第一个元素的下标
        self._head = 0
        # 队列中元素个数
        self._num = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self._num == self._len:
            return False
        else:
            self._elems[(self._head + self._num) % self._len] = value
            self._num += 1
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self._num == 0:
            return False
        else:
            self._head = (self._head + 1) % self._len
            self._num -= 1
            return True

    def Front(self) :
        """
        Get the front item from the queue.
        """
        if self._num == 0:
            return -1
        return self._elems[self._head]

    def Rear(self):
        """
        Get the last item from the queue.
        """
        if self._num == 0:
            return -1
        return self._elems[(self._head + self._num - 1) % self._len]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return self._num == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return self._num == self._len

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()