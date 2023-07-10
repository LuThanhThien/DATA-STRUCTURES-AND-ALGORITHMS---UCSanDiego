import sys
input = sys.stdin.read()
n = int(input)

def MoneyChange(n):
    changes = 0
    while n>0:
        if n>=10:
            changes+=1
            n-=10
        if n>=5 and n<10:
            changes+=1 
            n-=5
        if n>=1 and n<5:
            changes+=1
            n-=1
    return changes

print(MoneyChange(n))
