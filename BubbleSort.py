from random import sample, shuffle
from time import time

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

def main():
    arr = sample(range(1,100000), 10000)
    shuffle(arr)
    t0 = time()
    generic_sort = sorted(arr)
    print('generic sort:', time() - t0)
    t0 = time()
    bubble_sort = BubbleSort(arr)
    print('bubble sort:', time() - t0)
    print(sorted(arr) == BubbleSort(arr))

if __name__ == '__main__':
    main()