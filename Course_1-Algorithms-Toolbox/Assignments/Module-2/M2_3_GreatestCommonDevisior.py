import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])

def gcd(a,b):
    '''
    - Input: 
        a: positive integer
        b: positive integer
    - Output: 
        Fibonacci number of n 
    - Approach: sum of F(i-1) and F(i-2) without storing 
        the whole set of previous values in Fibonacci series
    - Time complexity: O(n)
    - Space complexity: O(1)
    '''
    if b>a:
        i = b
        b = a
        a = i
    if b==0:
        return a
    a_remain = a%b
    return gcd(b,a_remain)

print(gcd(a,b))
