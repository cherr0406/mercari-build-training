def binary_search(numbers: list, value: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if value == numbers[mid]:
            return mid
        elif value < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_rec(numbers: list, value: int) -> int:
    def _binary_search_rec(numbers: list, value: int, left: int, right: int):
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif value < numbers[mid]:
            return _binary_search_rec(numbers, value, left, mid - 1)
        else:
            return _binary_search_rec(numbers, value, mid + 1, right)

    return _binary_search_rec(numbers, value, 0, len(numbers) - 1)


if __name__ == "__main__":
    import random

    numbers = [random.randint(0, 100) for _ in range(10)]
    value = numbers[0]
    numbers = sorted(numbers)
    print(numbers, value)
    # print(binary_search(numbers, value))
    print(binary_search_rec(numbers, value))
