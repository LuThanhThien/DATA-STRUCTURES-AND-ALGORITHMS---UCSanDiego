def Fibonacci(n):
    '''
    - Input: 
        n: positive integer
    - Output: 
        Fibonacci number of n 
    - Approach: sum of F(i-1) and F(i-2) without storing 
        the whole set of previous values in Fibonacci series
    - Time complexity: O(n)
    - Space complexity: O(1)
    '''
    if n<2: return n
    Fi = 1
    Fi1 = 1
    for i in range(3,n+1):
        Fi2 = Fi1
        Fi1 = Fi
        Fi = Fi1 + Fi2
    return int(Fi)


if __name__ == '__main__':
    input_n = int(input())
    print(Fibonacci(input_n))
