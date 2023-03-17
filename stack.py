class Node:
    next = None

    def __init__(self, value):
        self.value = value


class Stack:
    head = None
    length = 0

    def push(self, item):
        self.length += 1
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.length == 0:
            return None

        self.length -= 1
        head = self.head
        self.head = head.next

        return head.value

    def peek(self):
        return self.head.value if self.head is not None else None


def run():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == "__main__":
    run()
