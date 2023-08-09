def CanSum(target,numbers,memo={}):
    if target in memo:
        return memo[target]
    if target==0: return True
    if target<0: return False
    for num in numbers:
        remainder = target-num
        if CanSum(remainder,numbers,memo)==True:
            memo[target]=True
            return memo[target]
    memo[target]=False
    return memo[target]

if __name__=='__main__':
    target = int(input('target sum = '))
    numbers_input = input()
    numbers = [int(num) for num in numbers_input.split()]
    print(CanSum(target,numbers))