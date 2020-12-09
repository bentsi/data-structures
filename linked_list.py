class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListIndexError(IndexError):
    pass


class LinkedList:
    def __init__(self):
        self.head = Node()

    def _get_last_node(self):
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        return pointer

    def get_last_node(self):
        return self._get_last_node().data

    def append(self, data):
        new_node = Node(data=data)
        last = self._get_last_node()
        last.next = new_node

    def print(self):
        print(self.__str__())

    def __str__(self):
        pointer = self.head
        idx = 0
        ll_str = ""
        while pointer.next is not None:
            pointer = pointer.next
            ll_str += f"{idx}: {pointer.data}\n"
            idx += 1
        return ll_str

    def length(self):
        pointer = self.head
        counter = 0
        while pointer.next is not None:
            pointer = pointer.next
            counter += 1
        return counter

    def _get(self, index):
        pointer = self.head
        counter = 0
        if not(0 <= index < self.length()):
            raise LinkedListIndexError(f"Index '{index}' does not exist")
        while pointer.next is not None:
            pointer = pointer.next
            if counter == index:
                return pointer
            counter += 1

    def get(self, index):
        return self._get(index=index).data

    def __getitem__(self, item):
        return self.get(index=item)

    def erase(self, index):
        if index == 0:
            prev = self.head
        else:
            prev = self._get(index=index - 1)
        to_del = prev.next
        prev.next = to_del.next
        data = to_del.data
        del to_del
        return data

    def set(self, index, new_data):
        node = self._get(index=index)
        node.data = new_data

    def __del__(self):
        length = self.length()
        while length != 0:
            self.erase(index=length - 1)
            length -= 1
        del self.head


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(data="Fedor")
    ll.append(data="Julia")
    ll.append(data="Bentsi")
    ll.print()
    print("Length of the Linked list is: ", ll.length())
    idx = 1
    print(ll.get(index=idx))
    print(f"Data at index {idx} is {ll[idx]}")
    print("Deleted: ", ll.erase(index=0))
    ll.append(data="Fedor")
    ll.append(data="Bentsi")
    ll.set(index=3, new_data="Tim Peters")
    print(ll)
