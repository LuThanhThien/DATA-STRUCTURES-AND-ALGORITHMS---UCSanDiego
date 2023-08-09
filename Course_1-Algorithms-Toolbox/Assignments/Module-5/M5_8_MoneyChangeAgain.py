def MoneyChange(money):
    memo={}
    memo[0] = 0

    for i in range(1,money+1):
        memo[i]=memo[i-1]+1

        if i>=3 and memo[i]>memo[i-3]:
            memo[i]=memo[i-3]+1

        if i>=4 and memo[i]>memo[i-4]:
            memo[i]=memo[i-4]+1

    return memo[money]

if __name__=='__main__':
    money = int(input())
    print(MoneyChange(money))
