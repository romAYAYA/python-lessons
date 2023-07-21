import time


def decorator_time_measure(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()

        result = func(*args, **kwargs)

        print("elapsed time (s): ", round(time.perf_counter() - time_start, 4))
        return result

    return wrapper


# bubble sort
@decorator_time_measure
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# selection sort

@decorator_time_measure
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# insertion sort

@decorator_time_measure
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# quick sort


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# counting sort
@decorator_time_measure
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    counting_array = [0] * (max_val - min_val + 1)

    for num in arr:
        counting_array[num - min_val] += 1

    sorted_array = []
    for i, count in enumerate(counting_array):
        sorted_array.extend([i + min_val] * count)

    return sorted_array


if __name__ == '__main__':
    print(bubble_sort([1, 2, 4, 5, 7, 3, 9, 12, 6]))
    print(selection_sort([1, 2, 4, 5, 7, 3, 9, 12, 6]))
    print(insertion_sort([1, 2, 4, 5, 7, 3, 9, 12, 6]))
    print(quick_sort([1, 2, 4, 5, 7, 3, 9, 12, 6]))
    print(counting_sort([1, 2, 4, 5, 7, 3, 9, 12, 6]))
