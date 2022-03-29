from random import sample, shuffle
from time import time


def Merge(arr1, arr2):
    merged = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            merged.append(arr2[j])
            j += 1
        else:
            merged.append(arr1[i])
            i += 1

    if i != len(arr1):
        merged += arr1[i:]
    if j != len(arr2):
        merged += arr2[j:]

    return merged


def MergeSort(arr):

    if len(arr) == 1:
        return arr

    return Merge(MergeSort(arr[:len(arr)//2]), MergeSort(arr[len(arr)//2:]))



def main():
    arr = sample(range(1,100000), 10000)
    shuffle(arr)

    t0 = time()
    generic_sort = sorted(arr)
    print('generic sort:', time() - t0)
    t0 = time()
    merge_sort = MergeSort(arr)
    print('merge sort:', time() - t0)
    print(generic_sort == merge_sort)


if __name__ == '__main__':
    main()