

def DPChange(money,coins):   
    min_num = [None]*(money+1)
    maxcoin_id = 0
    min_num[0]=0
    for m in range(1,money+1):
        min_num[m]=float("inf")
        for i in range(len(coins)):
            if m>=coins[i]:
                num = min_num[m-coins[i]]+1
                if num<min_num[m]:
                    min_num[m] = num
                    if coins[i]>coins[maxcoin_id]:
                        maxcoin_id=i
            else: break
    j = maxcoin_id
    coins_list = [0]*len(coins)
    money_change = money
    while money_change>0:
        if money_change>=coins[j]:
            coins_list[j]+=1
            money_change-=coins[j]
        else: j-=1
        if j<0: 
            return 0, coins_list
    return min_num[money], coins_list

def PrintCoins(money,min_coins,coins,coins_list):
    k=0
    print('{:>5s}{:>15s}{:>15s}'. format('No.', 'No. of coins','Coin'))
    print('{:>5s}{:>15s}{:>15s}'.format('-'*5,'-'*15,'-'*15))
    for i in range(len(coins)):
        if coins_list[i]!=0:
            k+=1
            print('{:>5d}{:>15d}{:>15d}'.format(k,coins_list[i],coins[i]))
    print('{:>5s}{:>15s}{:>15s}'.format('-'*5,'-'*15,'-'*15))
    if min_coins==0:
        print('Cannot exchange!')
        print('Total money: ',money)
        max = sum(coins_list[j]*coins[j] for j in range(len(coins)))
        print('Nearest lower amount money can be exchanged: ',max)
        print('No denomination to change other',money-max,'left!')
    else: 
        print('{:>5s}{:>15d}{:>15d}'.format('Total',min_coins,money))
    return None    

if __name__ == '__main__':
    money = int(input('Amount of money: '))
    input_coins = input('Coins lists (ascending)')
    coins = [int(coin) for coin in input_coins.split()]
    min_coins, coins_list = DPChange(money,coins)
    PrintCoins(money,min_coins,coins,coins_list)
