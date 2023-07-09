import sys

input = sys.stdin.read()
n = int(input)

def FibLastDig(n):
    '''
    - Input: 
        n: positive integer
    - Output: 
        Last digit of F(n) 
    - Approach: last digit of a number is a remainder
    when deviding by 10
    - Time complexity: O(n)
    - Space complexity: O(1)
    '''
    if n<2: return n
    Fi1 = 1
    Fi = 1
    for i in range(3,n+1):
        Fi2 = Fi1
        Fi1 = Fi
        Fi = (Fi1+Fi2)%10
    return int(Fi)


print(FibLastDig(n))
