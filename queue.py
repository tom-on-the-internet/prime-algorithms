from __future__ import annotations


class Node:
    next = None

    def __init__(self, value):
        self.value = value


class Queue:
    head = None
    tail = None
    length = 0

    def enqueue(self, item):
        self.length += 1
        node = Node(item)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def deque(self):
        if self.length == 0:
            return None

        self.length -= 1

        head = self.head
        self.head = head.next
        head.next = None

        return head.value

    def peek(self):
        return self.head.value if self.head is not None else None


def run():
    queue = Queue()
    queue.enqueue(99)
    queue.enqueue(123)
    print(queue.peek())
    print(queue.deque())
    print(queue.deque())
    print(queue.deque())
    queue.enqueue(123)
    queue.enqueue(123)
    print(queue.deque())


if __name__ == "__main__":
    run()
