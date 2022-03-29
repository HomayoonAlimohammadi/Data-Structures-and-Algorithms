from random import sample, shuffle
from time import time


def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main():
    arr = sample(range(1,100000), 10000)
    shuffle(arr)
    t0 = time()
    generic_sort = sorted(arr)
    print('generic sort:', time() - t0)
    t0 = time()
    selection_sort = SelectionSort(arr)
    print('selection sort:', time() - t0)
    print(generic_sort == selection_sort)


if __name__ == '__main__':
    main()