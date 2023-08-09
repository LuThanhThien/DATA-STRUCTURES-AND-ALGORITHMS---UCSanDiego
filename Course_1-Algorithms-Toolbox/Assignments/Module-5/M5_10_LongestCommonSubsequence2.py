def LongestCommonSub(arr1, arr2):
    memo={}
    memo[0,0]=0
    len1 = len(arr1)
    len2 = len(arr2)

    for i in range(1,len1+1):
        memo[i,0]=i
    for j in range(1,len2+1):
        memo[0,j]=j

    
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            memo[i,j] = float('inf')
            if memo[i,j]>memo[i,j-1]+1:
                memo[i,j]=memo[i,j-1]+1
            if memo[i,j]>memo[i-1,j]+1:
                memo[i,j]=memo[i-1,j]+1
            if arr1[i-1]==arr2[j-1] and memo[i,j]>memo[i-1,j-1]:
                memo[i,j]=memo[i-1,j-1]

    return (len1+len2-memo[len1,len2])//2


if __name__=='__main__':
    len1 = int(input())
    arr1_input = input()
    len2 = int(input())
    arr2_input = input()
    arr1 = [int(i) for i in arr1_input.split()]
    arr2 = [int(i) for i in arr2_input.split()]
    assert len1 == len(arr1)
    assert len2 == len(arr2)
    print(LongestCommonSub(arr1,arr2))