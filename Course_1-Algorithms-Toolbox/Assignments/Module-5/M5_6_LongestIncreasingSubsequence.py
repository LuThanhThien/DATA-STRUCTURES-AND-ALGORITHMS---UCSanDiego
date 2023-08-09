def LongestIncrease(arr, i ,memo={}):
    if i==0:
        memo[i] = 1

    if i not in memo:
        memo[i] = 1
        for j in range(i):
            if arr[j]<arr[i]:
                memo[i] = max(memo[i], LongestIncrease(arr,j,memo)+1) 

    return memo[i]

if __name__=='__main__':
    arr_input = input('A = ')

    arr = [int(num) for num in arr_input.split()]
    print(max(LongestIncrease(arr,i) for i in range(len(arr))))
