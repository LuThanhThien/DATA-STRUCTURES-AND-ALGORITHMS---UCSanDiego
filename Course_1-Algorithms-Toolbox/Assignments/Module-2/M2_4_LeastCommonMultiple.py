import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])

def lcm(a,b):

    def gcd(a,b):
        if b>a:
            i = b
            b = a
            a = i
        if b==0:
            return a
        a_remain = a%b
        return gcd(b,a_remain)
    
    gcd = gcd(a,b)
    return int(a*b/gcd)

print(lcm(a,b))