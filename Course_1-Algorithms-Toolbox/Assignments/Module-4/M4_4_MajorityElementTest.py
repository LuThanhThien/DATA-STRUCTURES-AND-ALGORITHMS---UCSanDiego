def MajorityElement(arr,low,high): #Same procedure as Partition in QuickSort

    if high-low+1<=len(arr)//2:
        return 0
    pivot = arr[low]
    j = low
    k = low
    for i in range(low+1,high+1):
        if arr[i]<=pivot:
            j+=1
            arr[i], arr[j] = arr[j], arr[i] 
            if arr[j]<pivot:
                arr[j], arr[k] = arr[k], arr[j]
                k+=1
    if j-k+1>len(arr)//2:
        return 1
    is_major = MajorityElement(arr,low,k-1)
    is_major = MajorityElement(arr,j+1,high)
    return is_major

def NaiveMajorityElement(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    max_duplicates = max(count.values()) if count else 0
    if max_duplicates>len(arr)//2: return 1
    else: return 0



import random

def create_random_array(n, min_val, max_val):
    # Generate n random integers between min_val and max_val (inclusive)
    arr = [random.randint(min_val, max_val) for _ in range(n)]
    return arr

# Example usage
n = 0  # Number of elements in the array
min_val = 1  # Minimum value of the integers
max_val = 100  # Maximum value of the integers
num_iters = 10011
for i in range(num_iters):
    arr = create_random_array(n, min_val, max_val)
    arr_copy = arr.copy()
    a = MajorityElement(arr_copy,0,len(arr_copy)-1)
    b = NaiveMajorityElement(arr_copy)
    if a!=b: 
        print('FALSE! Loop', i)
        print(arr)
        print(a, b)
    if i==num_iters-1:
        print('Success!')
