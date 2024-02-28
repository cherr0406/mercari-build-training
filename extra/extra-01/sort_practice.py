# bubble, selection, insertion, quick, merge, heap


import sys


def bubble(numbers: list[int]) -> list[int]:  # O(n)
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def bubble_rec(numbers: list[int]) -> list[int]:
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    numbers[0 : len(numbers) - 1] = bubble(numbers[0 : len(numbers) - 1])
    return numbers


def selection(numbers: list[int]) -> list[int]:  # O(n)
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i + 1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


def selection_rec(numbers: list[int]) -> list[int]:  # O(n)
    min_idx = 0
    if len(numbers) < 1:
        return numbers
    for i in range(1, len(numbers)):
        if numbers[min_idx] > numbers[i]:
            min_idx = i
    numbers[0], numbers[min_idx] = numbers[min_idx], numbers[0]
    numbers[1 : len(numbers)] = selection_rec(numbers[1 : len(numbers)])
    return numbers


def insertion(numbers: list[int]) -> list[int]:  # O(n)
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[j] > numbers[i]:
                numbers[j : i + 1] = [numbers[i]] + numbers[j:i]
                break
    return numbers


def insertion_2(numbers: list[int]) -> list[int]:  # O(n)
    for i in range(1, len(numbers)):
        tmp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > tmp:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = tmp

    return numbers


def quick(numbers: list) -> list[int]:  # O(n*log(n))
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left, right = [], []
    for n in numbers[1:]:  # O(n)
        if n < pivot:
            left.append(n)  # O(1)
        else:
            right.append(n)

    return quick(left) + [pivot] + quick(right)  # O(log(n))


def quick_2(numbers: list) -> list[int]:  # reduce spaces
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    idx = 1
    for i in range(len(numbers[1:])):
        if numbers[i + 1] <= pivot:
            numbers[i + 1], numbers[idx] = numbers[idx], numbers[i + 1]
            idx += 1

    piv_idx = idx - 1
    numbers[0], numbers[piv_idx] = numbers[piv_idx], numbers[0]

    numbers[:piv_idx] = quick_2(numbers[:piv_idx])
    numbers[piv_idx + 1 :] = quick_2(numbers[piv_idx + 1 :])

    return numbers


def merge(numbers: list) -> list[int]:  # O(n*log(n))
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = merge(numbers[:mid])  # O(log n)
    right = merge(numbers[mid:])

    i, il, ir = 0, 0, 0
    while il < mid and ir < len(numbers) - mid:  # O(n)
        if left[il] <= right[ir]:
            numbers[i] = left[il]
            il += 1
        else:
            numbers[i] = right[ir]
            ir += 1
        i += 1
    if il == mid:
        numbers[i:] = right[ir:]
    else:
        numbers[i:] = left[il:]
    return numbers


class MiniHeap(object):
    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    def parent(self, index: int) -> int:
        return index // 2

    def left(self, index: int) -> int:
        return 2 * index

    def right(self, index: int) -> int:
        return 2 * index + 1

    def min_child(self, index: int) -> int:
        if self.right(index) > self.current_size:
            return self.left(index)
        return (
            self.left(index)
            if self.heap[self.left(index)] < self.heap[self.right(index)]
            else self.right(index)
        )

    def swap(self, index1, index2) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        while self.parent(index) > 0:
            if self.heap[index] < self.heap[self.parent(index)]:
                self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify_down(self, index: int) -> None:
        while self.left(index) < self.current_size:
            min_child_index = self.min_child(index)
            if self.heap[min_child_index] < self.heap[index]:
                self.swap(index, min_child_index)
            index = min_child_index

    def push(self, value):
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def pop(self) -> int | None:
        if len(self.heap) == 1:
            return None

        root = self.heap[1]
        data = self.heap.pop()

        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.current_size -= 1
        self.heapify_down(1)

        return root


def heap(numbers: list) -> list[int]:
    mini_heap = MiniHeap()
    for n in numbers:
        mini_heap.push(n)

    for i in range(len(numbers)):
        numbers[i] = mini_heap.pop()

    return numbers


if __name__ == "__main__":
    import random

    numbers = [random.randint(0, 100) for _ in range(10)]
    test = [6, 1, 9, 3, 6, 2, 5]
    print(numbers)
    # print(bubble(numbers))
    # print(bubble_rec(numbers))
    # print(selection(numbers))
    # print(selection_rec(numbers))
    # print(insertion(numbers))
    # print(insertion_2(numbers))
    # print(quick(numbers))
    # print(quick_2(numbers))
    # print(merge(numbers))
    print(heap(numbers))
