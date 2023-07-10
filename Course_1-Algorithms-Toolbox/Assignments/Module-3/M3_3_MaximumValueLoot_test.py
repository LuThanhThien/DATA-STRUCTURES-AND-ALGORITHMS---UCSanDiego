import numpy as np
import random as rd

def InsertionSortDesc(n,arr):
    '''Insertion Sort with DESENDING order
    Input:
    - n: number of cost and weight pairs, positive integer
    - arr: array contain of cost and weight pairs, c1>=0, wi>0
        i.e.: [3,2,5,4] in this array there are 2 pairs,
        with c1 = 3, w1 = 2 and c2 = 5, w2 = 4.
    Output:
    - sorted_arr: array that sorted with descending order
    in terms of cost per unit weight (ci/wi)
    Running time: O(n^2)
    '''
    sorted_arr = arr.copy()
    for i in range(2,2*n,2):
        keyc = sorted_arr[i]
        keyw = sorted_arr[i+1]
        j = i - 2
        while j>=0 and sorted_arr[j]/sorted_arr[j+1]<keyc/keyw:
            sorted_arr[j+2] = sorted_arr[j]
            sorted_arr[j+3] = sorted_arr[j+1]
            j -= 2
        sorted_arr[j+2] = keyc
        sorted_arr[j+3] = keyw
    return sorted_arr

def MaximumValueLoot(n,W,arr):
    '''Finf the Maximum Loot Value
    Input:
    - n: number of cost and weight pairs, positive integer
    - W: maximum capacity, natural integer
    - arr: array contain of cost and weight pairs, c1>=0, wi>0
        i.e.: [3,2,5,4] in this array there are 2 pairs,
        with c1 = 3, w1 = 2 and c2 = 5, w2 = 4.
    Output:
    - total_value: total maximum value of loot 
    Running time: O(n^2)
    '''
    sorted_arr = InsertionSortDesc(n,arr)
    amount = 0
    total_value = 0
    i = 0
    while amount<W and i<2*n:
        amount += sorted_arr[i+1]
        total_value += sorted_arr[i]
        i+=2
    if amount>W:
        total_value -= (amount-W)*sorted_arr[i-2]/sorted_arr[i-1]
        amount = W
        return total_value
    return total_value


n = rd.randint(1,5)
W = rd.randint(30,1000)
arr = rd.sample(range(1,50),2*n)

print(n, W, arr)
print(InsertionSortDesc(n,arr))
MaximumValueLoot(n,W,arr)


