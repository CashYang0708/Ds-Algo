from typing import List


# selection sort, time complexity O(n^2)
def SelectionSort(arr: List) -> None:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


arr = [8, 6, 5, 0, 4, 7, 1]
SelectionSort(arr)
print("after selection sort:", arr)


# Bubble sort, time complexity O(n^2)
def BubbleSort(arr: List) -> None:
    for i in range(0, len(arr) - 1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [-3, 6, 5, -1, 0, 9, 3]
BubbleSort(arr)
print("after bubble sort:", arr)


# Insertion sort, time complexity O(n^2)
def InsertionSort(arr: List) -> None:
    for i in range(len(arr) - 1):
        key = arr[i + 1]
        j = i
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [6, 7, 4, 2, 9, 0, -4]
InsertionSort(arr)
print("after insertion sort:", arr)


# Merge sort, time complexity O(nlogn)
def Merge_Sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        Merge_Sort(left_array)
        Merge_Sort(right_array)

        right_index = 0
        left_index = 0
        merged_index = 0
        while right_index < len(right_array) and left_index < len(left_array):
            if right_array[right_index] < left_array[left_index]:
                array[merged_index] = right_array[right_index]
                right_index += 1
            else:
                array[merged_index] = left_array[left_index]
                left_index += 1

            merged_index += 1

        while right_index < len(right_array):
            array[merged_index] = right_array[right_index]
            right_index += 1
            merged_index += 1

        while left_index < len(left_array):
            array[merged_index] = left_array[left_index]
            left_index += 1
            merged_index += 1


arr = [41, 33, 17, 80, 61, 5, 55]
Merge_Sort(arr)
print("after merge sort:", arr)
