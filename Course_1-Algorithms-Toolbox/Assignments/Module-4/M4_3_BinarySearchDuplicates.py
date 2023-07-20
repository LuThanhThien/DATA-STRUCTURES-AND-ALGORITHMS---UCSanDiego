def BinarySearchDuplicates(arr,low,high,key):
    if high<low:
        return -1
    if high==low and arr[high]==key:
        return low
    mid = low + (high-low)//2 
    if arr[mid]==key:
        mid = BinarySearchDuplicates(arr,low,mid,key)
        return mid
    elif arr[mid]<key:
       return BinarySearchDuplicates(arr,mid+1,high,key)
    else: 
        return BinarySearchDuplicates(arr,low,mid-1,key)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(BinarySearchDuplicates(input_keys, 0, len(input_keys)-1, q), end=' ')