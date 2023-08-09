def LongestCommonSub3(arr1, arr2, arr3):
    memo={}
    memo[0,0,0]=0
    len1 = len(arr1)
    len2 = len(arr2)
    len3 = len(arr3)
    
    for i in range(len1+1):
        for j in range(len2+1):
             for k in range(len3+1):
                if i-1>=0 or j-1>=0 or k-1>=0:
                    memo[i,j,k] = float('inf')
                if j-1>=0 and memo[i,j,k]>memo[i,j-1,k]+1:
                    memo[i,j,k]=memo[i,j-1,k]+1
                if i-1>=0 and memo[i,j,k]>memo[i-1,j,k]+1:
                    memo[i,j,k]=memo[i-1,j,k]+1
                if k-1>=0 and memo[i,j,k]>memo[i,j,k-1]+1:
                    memo[i,j,k]=memo[i,j,k-1]+1
                if i-1>=0 and j-1>=0 and k-1>=0 and arr1[i-1]==arr2[j-1]==arr3[k-1]:
                    if memo[i,j,k]>memo[i-1,j-1,k-1]:
                        memo[i,j,k]=memo[i-1,j-1,k-1]
            

    return (len1+len2+len3-memo[len1,len2,len3])//3


if __name__=='__main__':
    len1 = int(input())
    arr1_input = input()
    len2 = int(input())
    arr2_input = input()
    len3 = int(input())
    arr3_input = input()
    arr1 = [int(i) for i in arr1_input.split()]
    arr2 = [int(i) for i in arr2_input.split()]
    arr3 = [int(i) for i in arr3_input.split()]
    assert len1==len(arr1)
    assert len2==len(arr2)
    assert len3==len(arr3)
    print(LongestCommonSub3(arr1,arr2,arr3))