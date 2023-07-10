
import numpy as np
import random as rd

# O(nlogn)
def MinTotalWatingTime(t,n):
    waitingTime = 0

    for i in range(1,n):
        key = t[i]
        j = i-1
        while t[j]>key and j>=0:
            t[j+1]=t[j]
            j-=1
        t[j+1]=key
    
    for i in range(n):
        waitingTime += (n-i-1)*t[i]
    return t, waitingTime

