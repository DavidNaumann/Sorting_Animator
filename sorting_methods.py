# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right,sorts):
    for i in range(left + 1, right + 1):

        temp = arr[i]
        j = i - 1
        sorts.append([item for item in arr])
        while arr[j] > temp and j >= left:
            arr[j + 1] = arr[j]
            j -= 1
            sorts.append([item for item in arr])

        arr[j + 1] = temp
        sorts.append([item for item in arr])
    # merge function merges the sorted runs


def merge(arr, l, m, r,sorts):
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
        sorts.append([item for item in arr])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
        sorts.append([item for item in arr])

    i, j, k = 0, 0, l
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            sorts.append([item for item in arr])

        else:
            arr[k] = right[j]
            j += 1
            sorts.append([item for item in arr])

        k += 1

    # copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
        sorts.append([item for item in arr])
    # copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
        sorts.append([item for item in arr])


# iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr,RUN):
    n = len(arr)
    sorts = []
    # Sort individual subarrays of size RUN
    for i in range(0, n, RUN):
        insertionSort(arr, i, min((i + 31), (n - 1)), sorts)

        # start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = RUN
    while size < n:

        # pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
            # find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            # merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            merge(arr, left, mid, right, sorts)

        size = 2 * size

    return sorts


def bubble_sort(arr):
    n = len(arr)
    sorts = []
    sorts.append([item for item in arr])
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorts.append([item for item in arr])
    return sorts