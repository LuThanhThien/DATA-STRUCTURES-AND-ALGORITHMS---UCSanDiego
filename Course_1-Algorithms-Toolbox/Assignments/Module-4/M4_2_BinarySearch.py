def BinarySearch(arr,low,high,key):
    if high<low:
        return -1
    mid = low + (high-low)//2
    if key==arr[mid]:
        return mid
    elif key<arr[mid]:
        return BinarySearch(arr,low,mid-1,key)
    else: 
        return BinarySearch(arr,mid+1,high,key)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(BinarySearch(input_keys, 0, len(input_keys)-1, q), end=' ')
