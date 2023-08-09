def ShortestSum(target,numbers,memo={}):
    '''
    - Input:
        target: target sum, positive
        numbers: array contains numbers, positive
        memo: dictionary for memorization of sum elements
    - Output: 
        shortestSum: shortest combination of elements that sum to target
    - Approach: recursive call with memorization
    - Time complexity: O(n*m^2)
    - Space complexity: O(m^2)
    Where: 
        n is value of target sum
        m is number of elements in numbers
    '''
    if target in memo:
        return memo[target]
    if target==0: return []
    if target<0: return None
    shortestSum = None
    for num in numbers:
        remainder = target-num
        remaindercombination = ShortestSum(remainder,numbers,memo)
        if remaindercombination!=None:
            remaindercombination.append(num)
            if shortestSum==None or len(shortestSum)>len(remaindercombination):
                shortestSum=remaindercombination
    memo[target]=shortestSum
    return shortestSum

if __name__=='__main__':
    target = int(input('target sum = '))
    numbers_input = input()
    numbers = [int(num) for num in numbers_input.split()]
    print(ShortestSum(target,numbers))