from random import sample, shuffle
from time import time


def InsertionSort(arr):
    for i in range(1, len(arr)):
        while arr[i] < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr

def main():
    arr = sample(range(1,100000), 10000)
    shuffle(arr)
    t0 = time()
    generic_sort = sorted(arr)
    print('generic sort:', time() - t0)
    t0 = time()
    insertion_sort = InsertionSort(arr)
    print('selection sort:', time() - t0)
    print(generic_sort == insertion_sort)


if __name__ == '__main__':
    main()