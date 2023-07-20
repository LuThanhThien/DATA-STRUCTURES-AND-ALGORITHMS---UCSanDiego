import math 

def BinarySearch(arr,low,high):
    if high<low: 
        return print('x = ',arr[low-1])
    mid = low + math.ceil((high-low)/2)
    print('Is x = ',arr[mid],', choose one of three options:')
    print('1. Yes')
    print('2. x > ',arr[mid])
    print('3. x < ',arr[mid])
    ans = int(input('Your choice: '))
    if ans==1:
        return print('x = ',arr[mid])
    if ans==2:
        return BinarySearch(arr,mid+1,high)
    else:
        return BinarySearch(arr,low,mid-1)

arr = list(range(1,2097152))
BinarySearch(arr,0,len(arr)-1)




