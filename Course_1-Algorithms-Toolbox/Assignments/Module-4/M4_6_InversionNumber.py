def Merge(B,C):
    count = 0
    merge_arr = []
    while len(B)>0 and len(C)>0:
        b = B[0]
        c = C[0]
        if b<=c:
            merge_arr.append(b)
            B.pop(0)
        else:
            merge_arr.append(c)
            C.pop(0)
            count+=len(B)
    merge_arr.extend(B)       
    merge_arr.extend(C)
    return count, merge_arr

def InversionNumber(arr):
    if len(arr)==1:
        return 0, arr
    m = len(arr)//2
    a, B = InversionNumber(arr[0:m])
    b, C = InversionNumber(arr[m:])
    count, arr_sort = Merge(B,C)
    count+=a+b
    return count, arr_sort

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(InversionNumber(elements)[0])