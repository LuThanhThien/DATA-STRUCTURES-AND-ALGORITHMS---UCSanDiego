def EditDistance(str1, str2):
    memo={}
    memo[0,0]=0
    len1 = len(str1)
    len2 = len(str2)

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
            if str1[i-1]!=str2[j-1] and memo[i,j]>memo[i-1,j-1]+1:
                memo[i,j]=memo[i-1,j-1]+1
            if str1[i-1]==str2[j-1] and memo[i,j]>memo[i-1,j-1]:
                memo[i,j]=memo[i-1,j-1]

    return memo[len1,len2]


if __name__=='__main__':
    str1_input = input()
    str2_input = input()
    print(EditDistance(str1_input,str2_input))