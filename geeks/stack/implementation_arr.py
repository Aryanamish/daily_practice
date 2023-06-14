class Stack:

    def __str__(self):
        x = self.data.copy()
        x.reverse()
        return str(x)

    def __repr__(self):
        return self.__str__()

    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    @property
    def isEmpty(self):
        return len(self.data) == 0

    @property
    def length(self):
        return len(self.data)

    def peek(self):
        return self.data[-1] if not self.isEmpty else None

    def pop(self):
        if not self.isEmpty:
            return self.data.pop()
        return None