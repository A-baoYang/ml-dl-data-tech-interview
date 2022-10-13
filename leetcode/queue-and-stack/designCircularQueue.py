class MyCircularQueue:
    def __init__(self, k: int):
        self.length = k
        self._list = [None] * k
        self.head, self.tail = -1, -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0

        self.tail = (self.tail + 1) % self.length
        self._list[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head, self.tail = -1, -1
            return True

        self.head = (self.head + 1) % self.length
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._list[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._list[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.length == self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
