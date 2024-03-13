from typing import List


# Linear Search, time complexity O(n)
def LinearSearch(arr: List, target: int) -> bool:
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False


# Binary search, the input of array should be sorted, time complexity:O(logn)
def BinarySearchIterative(arr: List, target: int) -> int:
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    # if array doesn't contain the target, return -1
    return -1


print(BinarySearchIterative([1, 2, 3, 4, 5], 4))


def BinarySearchRecursive(left: int, right: int, arr: List, target: int) -> int:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        BinarySearchRecursive(left, mid - 1, arr, target)
    else:
        BinarySearchRecursive(mid + 1, right, arr, target)
    # if array doesn't contain the target, return -1
    return -1


arr = [1, 2, 3, 4, 5]
print(BinarySearchRecursive(0, len(arr) - 1, arr, 4))
