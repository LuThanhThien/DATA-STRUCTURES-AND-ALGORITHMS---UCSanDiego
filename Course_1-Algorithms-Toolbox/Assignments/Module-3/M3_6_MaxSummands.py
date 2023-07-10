def MaxSummands(n):
    arr = []
    k = 0
    while n>0:
        k += 1
        if n-k>k:
            arr.append(k)
            n-=k
        if n==k: 
            arr.append(k)
            break
    return arr


if __name__ == '__main__':
    n = int(input())
    summands = MaxSummands(n)
    print(len(summands))
    print(*summands)