class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        """
        Return how many cookies are there in a jar

        """
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("The jar doesn't have enough space")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("There is not enough cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Capacity can't be a negative number")
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n

