import sys

input = sys.stdin.read()
n = int(input)

def LastDigitSum(n):
    F = [0, 1]
    if n==1: return 1 
    for i in range(2,n+3): 
        F.append(F[i-1]+F[i-2]) 
        if i>2 and F[i-1]%10==1 and F[i-2]%10==0:
                k = (n+2)%(i-2)
                sum = F[k]-1
                return int(sum%10) 
    sum = F[n+2]-1
    return int(sum%10)   


print(LastDigitSum(n))
