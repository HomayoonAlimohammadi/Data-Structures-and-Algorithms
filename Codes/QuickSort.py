from random import sample, shuffle
from time import time


def QuickSort(arr):

    if len(arr) <= 1:
        return arr

    arr_sorted, pivot_index = SortByPivot(arr)
    left = arr_sorted[:pivot_index]
    right = arr_sorted[pivot_index+1:]

    left_sorted = QuickSort(left)
    right_sorted = QuickSort(right)

    return left_sorted + [arr_sorted[pivot_index]] + right_sorted


def SortByPivot(arr):
    if len(arr) == 0:
        return [], 0

    pivot = arr[0]
    swap_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            swap_idx += 1
            arr[swap_idx], arr[i] = arr[i], arr[swap_idx]
    
    arr[swap_idx], arr[0] = arr[0], arr[swap_idx]
    return arr, swap_idx



def main():
    arr = sample(range(1,100000), 10000)
    shuffle(arr)

    t0 = time()
    generic_sort = sorted(arr)
    print('generic sort:', time() - t0)
    t0 = time()
    quick_sort = QuickSort(arr)
    print('quick sort:', time() - t0)
    print(generic_sort == quick_sort)

if __name__ == '__main__':
    main()

