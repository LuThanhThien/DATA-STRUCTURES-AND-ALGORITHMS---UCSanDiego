def PrimitiveCalculator(num):
    memo={}
    memo[1] = 0

    for i in range(2,num+1):
        memo[i] = float('inf')
        if i%3==0 and memo[i]>memo[i//3]:
            memo[i] = memo[i//3]+1
        if i%2==0 and memo[i]>memo[i//2]:
            memo[i] = memo[i//2]+1
        if i>1 and memo[i]>memo[i-1]:
            memo[i] = memo[i-1]+1

    return memo

def OutputOperation(num):
    operation = []
    memo = PrimitiveCalculator(num)
    minOperation = memo[num]
    while num>1:
        operation.append(num)
        if memo[num]==memo[num-1]+1:
            num=num-1
        elif num%2==0 and memo[num]==memo[num//2]+1:
            num=num//2
        elif num%3==0 and memo[num]==memo[num//3]+1:
            num=num//3        
    operation.append(1)
    return minOperation, operation[::-1]

if __name__=='__main__':
    num_input = int(input(''))
    min, operation = OutputOperation(num_input)
    print(min)
    print(*operation)
