from random import sample, shuffle
from time import time


def QuickSort(arr, pivot_index=0):
    
    if len(arr) == 1:
        return arr

    left = arr[:pivot_index]
    right = arr[pivot_index+1:]
    left_sorted_by_pivot, new_pivot_index = SortByPivot(left)
    right_sorted_by_pivot, new_pivot_index = SortByPivot(right)
    return left + [arr[pivot_index]] + right
    



def SortByPivot(arr):
    pivot = arr[0]
    swap_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            swap_idx += 1
            arr[swap_idx], arr[i] = arr[i], arr[swap_idx]
    
    arr[swap_idx], arr[0] = arr[0], arr[swap_idx]
    return arr, swap_idx


l = [4,6,1,7,3,2,5]
print(SortByPivot(l))
