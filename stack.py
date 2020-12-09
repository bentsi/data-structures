class Stack:
    """This class implements Stack data structure"""
    def __init__(self):
        self._container = []

    def push(self, obj):
        self._container.append(obj)

    def pop(self):
        value = self._container[-1]
        del self._container[-1]
        return value

    def is_empty(self):
        return len(self._container) == 0

    def top(self):
        return self._container[-1]

    def __str__(self):
        width = 30
        tmp_str = ""
        for i in range(len(self._container) - 1, -1, -1):
            tmp_str = tmp_str + f"|{self._container[i].center(width)}|\n"
        tmp_str += "-" * (width + 2)
        return tmp_str

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    s = Stack()

