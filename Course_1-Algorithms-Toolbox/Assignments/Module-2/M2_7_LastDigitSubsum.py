import sys

input = sys.stdin.read()
tokens = input.split()
n = int(tokens[1])
m = int(tokens[0])

def LastDigitSubsum(m,n):
    if n<2: return n
    F = [0, 1]
    if n==1: return 1 
    for i in range(2,n+3): 
        F.append(F[i-1]+F[i-2]) 
        if i>2 and F[i-1]%10==1 and F[i-2]%10==0:
                k = (n+2)%(i-2)
                t = (m+1)%(i-2)
                sum = F[k]-F[t]
                return int(sum%10) 
    sum = F[n+2]-F[m+1]
    return int(sum%10)   

print(LastDigitSubsum(m,n))