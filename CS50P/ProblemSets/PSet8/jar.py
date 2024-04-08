class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        cookies = ""
        for _ in range(self.size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError()
        self.size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError()
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError()
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError()
        self._size = size


def main():
    jar = Jar()
    jar.deposit(3)
    print(jar)


if __name__ == "__main__":
    main()
