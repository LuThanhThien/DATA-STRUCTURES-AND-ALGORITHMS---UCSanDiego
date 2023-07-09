import sys

input = sys.stdin.read()
tokens = input.split()
n = int(tokens[0])
m = int(tokens[1])

def FibMod(n, m):
    F = [0, 1]
    if n==1: return 1 
    for i in range(2,n+1): 
        F.append((F[i-1]+F[i-2])%m)
        if i>2 and F[i-1]==1 and F[i-2]==0:
                k = n%(i-2)
                return int(F[k]%m) 
    return int(F[n]%m)

print(FibMod(n,m))
