def MajorityElement(arr,low,high): #Same procedure as Partition in QuickSort
    if high==low: 
        return 0
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
    major_low = MajorityElement(arr,low,k-1)
    major_high = MajorityElement(arr,j+1,high)
    return max(major_low,major_high)

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(MajorityElement(input_elements,0,len(input_elements)-1))
