def RandomizedQuickSort3(nums,low,high):
    import random as rd
    while low<high:  
        k = rd.randint(low,high)
        nums[low], nums[k] = nums[k], nums[low]
        pivot_low, pivot_high = Partition3(nums,low,high)
        if pivot_low-low<high-pivot_high:
            RandomizedQuickSort3(nums,low,pivot_low-1)
            low = pivot_high+1
        else:
            RandomizedQuickSort3(nums,pivot_high+1,high)
            high = pivot_low-1
    return nums

def Partition3(nums,low,high):
    pivot = nums[low]
    j  = low
    k = low
    for i in range(low+1,high+1):
        if nums[i]<=pivot:
            j+=1
            nums[i], nums[j] = nums[j], nums[i] 
            if nums[j]<pivot:
                nums[j], nums[k] = nums[k], nums[j]
                k+=1
    return k, j


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    RandomizedQuickSort3(elements, 0, len(elements) - 1)
    print(*elements)