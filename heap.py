from __future__ import annotations


class MaxHeap:
    items: list[int] = []

    def insert(self: MaxHeap, item: int) -> None:
        self.items.append(item)
        self.heapify_up(len(self.items) - 1)

    def delete(self: MaxHeap) -> int:
        value = self.items[0]
        self.items[0] = self.items.pop()
        self.heapify_down(0)
        return value

    def heapify_up(self: MaxHeap, idx: int) -> None:
        if idx == 0:
            return

        parent_idx = self.parent(idx)
        value = self.items[idx]
        parent_value = self.items[parent_idx]

        if parent_value < value:
            self.swap_items(parent_idx, idx)
            self.heapify_up(parent_idx)

    def heapify_down(self: MaxHeap, idx: int) -> None:
        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)

        if idx >= len(self.items) or left_idx >= len(self.items):
            return

        value = self.items[idx]
        left_value = self.items[left_idx]

        # no right child
        if right_idx >= len(self.items):
            if value > left_value:
                return

            self.swap_items(idx, left_idx)
            return

        right_value = self.items[right_idx]

        if value > left_value and value > right_value:
            return

        if left_value > right_value:
            self.swap_items(left_idx, idx)
            self.heapify_down(left_idx)

        if left_value <= right_value:
            self.swap_items(idx, right_idx)
            self.heapify_down(right_idx)

    def parent(self: MaxHeap, idx: int) -> int:
        return (idx - 1) // 2

    def left_child(self: MaxHeap, idx: int) -> int:
        return (idx * 2) + 1

    def right_child(self: MaxHeap, idx: int) -> int:
        return (idx * 2) + 2

    def swap_items(self: MaxHeap, idx1: int, idx2: int) -> None:
        self.items[idx1], self.items[idx2] = [self.items[idx2], self.items[idx1]]


m_heap = MaxHeap()

m_heap.insert(3)
m_heap.insert(40)
m_heap.insert(20)
m_heap.insert(19)

print(m_heap.items)
print(m_heap.delete())
print(m_heap.items)
print(m_heap.delete())
print(m_heap.items)
m_heap.insert(1)
print(m_heap.items)
