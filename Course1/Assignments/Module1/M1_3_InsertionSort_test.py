import numpy as np
import random 
import time

def InsertionSort(array, n, order='asc'):
    sort_arr = array.copy()
    if order=='asc':
        for i in range(1,n):
            key = sort_arr[i]
            j = i - 1
            while j>=0 and sort_arr[j]>key:
                sort_arr[j+1] = sort_arr[j]
                j -= 1
            sort_arr[j+1] = key
        return sort_arr
    if order=='desc':
        for i in range(1,n):
            key = sort_arr[i]
            j = i - 1
            while j>=0 and sort_arr[j]<key:
                sort_arr[j+1] = sort_arr[j]
                j -= 1
            sort_arr[j+1] = key
        return sort_arr

n = random.randint(2,10)
array = np.random.randint(1,100,size=n)
array_sorted = InsertionSort(array,n,order='desc')


print('Initial array: ', array)
print('n  = ',n)
print('Sorted array: ', array_sorted)