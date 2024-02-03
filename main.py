import timeit
import random


# Генеруємо список чисел від 1 до n
def generate_unique_numbers(n):
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    return numbers


# Timsort сортування
def timsort_sorted(array):
    return sorted(array)


def timsort_sort(array):
    return array.sort()


# Сортування вставками
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


# Сортування злиттям
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def sorting_measurement(len):
    print(f"Number of items to measure: '{len}'")
    # Execution time 'Timsort' -> sorted
    execution_time = timeit.timeit(lambda: timsort_sorted(generate_unique_numbers(len)), number=1)
    print(f"Execution time 'Timsort -> sorted': {execution_time} seconds")
    # Execution time 'Timsort' -> sort
    execution_time = timeit.timeit(lambda: timsort_sort(generate_unique_numbers(len)), number=1)
    print(f"Execution time 'Timsort -> sort': {execution_time} seconds")
    # Execution time 'merge'
    execution_time = timeit.timeit(lambda: merge_sort(generate_unique_numbers(len)), number=1)
    print(f"Execution time 'merge': {execution_time} seconds")
    # Execution time 'insertion'
    execution_time = timeit.timeit(lambda: insertion_sort(generate_unique_numbers(len)), number=1)
    print(f"Execution time'insertion': {execution_time} seconds")


# 1000 elements
sorting_measurement(1000)

# 10000 elements
sorting_measurement(10000)

# 100000 elements
sorting_measurement(100000)

# 1000000 elements
sorting_measurement(1000000)