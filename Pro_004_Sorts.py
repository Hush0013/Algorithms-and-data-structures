import time


def Insertion_sort(ar):
    arr = [x for x in ar]
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            #  print(*arr)
    return arr


def Bubble_sort(ar):
    arr = [x for x in ar]
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                swap = True
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                #  print(*arr)
        if not swap:
            return arr


def Selection_sort(ar):
    arr = [x for x in ar]
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
        #  print(*arr)
    return arr


def Shell_sort(ar):
    n = len(ar)
    arr = [x for x in ar]
    step = n // 2
    while step > 0:
        start = step
        while start < n:
            i = start - step
            while i >= 0:
                if arr[i] > arr[i + step]:
                    arr[i], arr[i + step] = arr[i + step], arr[i]
                i -= step
            start += 1
        step //= 2
    return arr


def Merge_sort(ar):
    n = len(ar)
    if n == 1:
        return ar
    arr = [x for x in ar]
    mid = n // 2
    L = arr[:mid]
    R = arr[mid:]
    L = Merge_sort(L)
    R = Merge_sort(R)
    i, j, k = 0, 0, 0
    while i < mid and j < n - mid:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < mid:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n - mid:
        arr[k] = R[j]
        j += 1
        k += 1
    return arr


def Quick_sort(ar):
    n = len(ar)
    arr = [x for x in ar]
    quicksort(arr, 0, n - 1)
    return arr


def quicksort(arr, left, right):
    if left < right:
        partition = pos(arr, left, right)
        quicksort(arr, left, partition - 1)
        quicksort(arr, partition + 1, right)


def pos(arr, left, right):
    pivot = arr[right]
    i = left
    j = right - 1
    while i <= j:
        while i <= right and arr[i] < pivot:
            i += 1
        while j >= left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


a = list(map(int, input().split()))
t1 = time.perf_counter() * 1000
print(Insertion_sort(a))
t2 = time.perf_counter() * 1000
print(Bubble_sort(a))
t3 = time.perf_counter() * 1000
print(Selection_sort(a))
t4 = time.perf_counter() * 1000
print(Shell_sort(a))
t5 = time.perf_counter() * 1000
print(Merge_sort(a))
t6 = time.perf_counter() * 1000
print(Quick_sort(a))
t7 = time.perf_counter() * 1000
print(t2 - t1, t3 - t2, t4 - t3, t5 - t4, t6 - t5, t7 - t6, sep=' milliseconds\n', end=' milliseconds\n')
