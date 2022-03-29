import BubbleSort, InsertionSort, MergeSort, QuickSort, SelectionSort
from random import sample, shuffle
from time import time


def main():

    arr = sample(range(1,100000), 10000)
    shuffle(arr)

    t0 = time()
    generic_sort = sorted(arr)
    print('generic sort:', time() - t0)

    t0 = time()
    bubble_sort = BubbleSort.BubbleSort(arr)
    print('bubble sort:', time() - t0)
    print(generic_sort == bubble_sort)

    t0 = time()
    insertion_sort = InsertionSort.InsertionSort(arr)
    print('insertion sort:', time() - t0)
    print(generic_sort == insertion_sort)

    t0 = time()
    merge_sort = MergeSort.MergeSort(arr)
    print('merge sort:', time() - t0)
    print(generic_sort == merge_sort)

    t0 = time()
    quick_sort = QuickSort.QuickSort(arr)
    print('quick sort:', time() - t0)
    print(generic_sort == quick_sort)

    t0 = time()
    selection_sort = SelectionSort.SelectionSort(arr)
    print('selection sort:', time() - t0)
    print(generic_sort == selection_sort)

    



if __name__ == '__main__':
    main()