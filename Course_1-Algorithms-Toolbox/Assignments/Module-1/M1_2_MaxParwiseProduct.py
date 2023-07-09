
import numpy as np
import sys

input = sys.stdin.read()
tokens = input.split()
n = int(tokens[0])
array = list(map(int, tokens[1:]))

def MaxPairwiseProduct(n, array):
    '''
    - Input: 
        n: number of elements in an array
        array: array contains real numbers
    - Output: 
        max_product: maximum product of 2 elements in array
    - Approach: Maximum pairwise product is the product of 2
    maximum values in array
    - Time complexity: O(n)
    - Space complexity: O(1)
    '''
    id_min = 0
    id_max = 0
    for i in range(1,n):
        if array[id_min]<array[i]:
            id_min = i
    
    for j in range(1,n):
        if id_min==id_max==0 or (j!=id_min and array[id_max]<array[j]):
            id_max = j

    max_product = array[id_min]*array[id_max]
    return max_product

print(MaxPairwiseProduct(n,array))

