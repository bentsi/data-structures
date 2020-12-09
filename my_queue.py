from linked_list import LinkedList
import time


class Queue:
    def __init__(self):
        self._linked_list = LinkedList()

    def enqueue(self, data):
        self._linked_list.append(data=data)

    def dequeue(self):
        return self._linked_list.erase(index=0)

    def front(self):
        return self._linked_list.get(index=0)

    def back(self):
        return self._linked_list.get_last_node()

    def is_empty(self):
        return self._linked_list.length() == 0

    def __str__(self):
        return self._linked_list.__str__()


if __name__ == '__main__':
    q = Queue()
    print("Queue empty: ", q.is_empty())
    q.enqueue(data="Fedor")
    q.enqueue(data="Bentsi")
    q.enqueue(data="Julia")
    q.enqueue(data="Roman")
    q.enqueue(data="Alexey")
    print(q)
    print("Fedor is going to leave the Queue...")
    time.sleep(3)
    print(f"{q.dequeue()} left the Queue.")
    print(q)
    print("Front item in Queue: ", q.front())
    print("Back item in Queue: ", q.back())
    print("Queue empty: ", q.is_empty())
