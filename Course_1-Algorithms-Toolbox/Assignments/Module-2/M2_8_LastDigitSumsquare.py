import sys

input = sys.stdin.read()
n = int(input)

def LastDigitSumsquare(n):
    if n<2: return n
    F = [0, 1]
    if n==1: return 1 
    for i in range(2,n+1): 
        F.append(F[i-1]+F[i-2]) 
        if i>2 and F[i-1]%10==1 and F[i-2]%10==0:
                k = (n)%(i-2)
                t = k-1
                sum = F[k]*(F[t]+F[k])
                return int(sum%10) 
    sum = F[n]*(F[n]+F[n-1])
    return int(sum%10)   


print(LastDigitSumsquare(n))