import numpy as np
import random

def max_pairwise_product(n, array):
    '''Use loop to found multiple of every pairwise
    and compare them to obtain the highest one.
    The complexity is n*n
    '''
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            multiple = array[i]*array[j]
            if multiple>result: result=multiple
    
    return result

def max_pairwise_product_fast(n, array):
    '''Use 2 loop to find 2 highest values in the array 
    such that their index are different.
    The complexity is n+n
    '''
    id1 = 0
    id2 = 0
    for i in range(1,n):
        if array[id1]<array[i]:
            id1 = i
    
    for j in range(1,n):
        if id1==id2==0 or (j!=id1 and array[id2]<array[j]):
            id2 = j

    result = array[id1]*array[id2]
    return result

max_loop = 100000
count = 1

while True:
    n = random.randint(2,11)
    array = random.sample(range(1,100),n)
    res1 = max_pairwise_product(n,array)
    res2 = max_pairwise_product_fast(n,array)
    print('n  = ',n)
    print('Array: ', array)
    print('Max pair wise: ', res1)
    print('Max pair wise fast: ', res2)

    if res1!=res2:
        print('Wrong!!')
        break
    else: print('OK')

    print('Running time: ',count, '\n')
    
    if count==max_loop:   
        print('Successful test!')
        break
    count+=1
