from time import sleep

from my_queue import Queue


class PriorityQueue(Queue):

    def dequeue(self):
        pointer = self._linked_list.head
        idx = 0
        largest_priority = 0
        largest_priority_idx = 0
        while pointer.next is not None:
            pointer = pointer.next
            priority, data = pointer.data
            if priority > largest_priority:
                largest_priority = priority
                largest_priority_idx = idx
            idx += 1
        return self._linked_list.erase(index=largest_priority_idx)


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(data=(0, "Bentsi"))
    pq.enqueue(data=(93287, "Tim"))
    pq.enqueue(data=(328, "Fedor"))
    pq.enqueue(data=(8479, "Julia"))
    pq.enqueue(data=(42, "Alexey"))
    pq.enqueue(data=(93287, "Guido"))
    print(pq)
    while not pq.is_empty():
        print(f"{pq.dequeue()} left the Queue")
        sleep(2)

