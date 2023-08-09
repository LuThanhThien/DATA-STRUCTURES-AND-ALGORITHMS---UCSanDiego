def FibonancciMemo(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        memo[n]=n
        return memo[n]
    memo[n] = FibonancciMemo(n-2,memo)+FibonancciMemo(n-1,memo)
    return memo[n]

if __name__=='__main__':
    n = int(input('n = '))
    print(FibonancciMemo(n))