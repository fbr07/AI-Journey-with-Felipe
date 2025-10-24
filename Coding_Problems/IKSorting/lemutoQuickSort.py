import random


def quickSortHelper(arr, start, end):
    if start >= end:
        return

    random_index = random.randint(start, end)
    arr[start], arr[random_index] = arr[random_index], arr[start]
    pivot = arr[start]

    leftSidePointer = start
    for currentElementPointer in range(start + 1, end + 1):
        if arr[currentElementPointer] <= pivot:
            leftSidePointer += 1
            arr[leftSidePointer], arr[currentElementPointer] = (
                arr[currentElementPointer],
                arr[leftSidePointer],
            )

    arr[start], arr[leftSidePointer] = arr[leftSidePointer], arr[start]

    quickSortHelper(arr, start, leftSidePointer - 1)
    quickSortHelper(arr, leftSidePointer + 1, end)


def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)
    return arr


print(quickSort([5, 8, 3, 9, 4, 1, 7]))
