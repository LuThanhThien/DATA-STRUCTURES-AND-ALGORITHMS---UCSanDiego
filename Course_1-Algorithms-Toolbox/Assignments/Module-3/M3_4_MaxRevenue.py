def InsertionSort(array, order='asc'):
    '''Insertion Sort with order
    Input:
    - arr: array contain of non-sorting numbers, 
    Output:
    - sorted_arr: array that sorted with order
    Running time: O(n^2)
    '''
    n = len(array)
    sort_arr = array.copy()
    if order=='asc':
        for i in range(1,n):
            key = sort_arr[i]
            j = i - 1
            while j>=0 and sort_arr[j]>key:
                sort_arr[j+1] = sort_arr[j]
                j -= 1
            sort_arr[j+1] = key
        return sort_arr
    if order=='desc':
        for i in range(1,n):
            key = sort_arr[i]
            j = i - 1
            while j>=0 and sort_arr[j]<key:
                sort_arr[j+1] = sort_arr[j]
                j -= 1
            sort_arr[j+1] = key
        return sort_arr

def MaxRevenue(n,price,click):
    '''Calculate maximum of Revenue from Advertisement by Clicks
    Input:
    - n: number of advertisement slots
    - price: array contains pricing values of each advertisement per click
    - click: number of expected clicks
    Output:
    revenue: maximum revenue
    '''
    price_sort = InsertionSort(price,order='desc')
    click_sort = InsertionSort(click,order='desc')
    max_revenue = 0
    for i in range(n):
        max_revenue += price_sort[i]*click_sort[i]
    
    return max_revenue

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(MaxRevenue(n,prices, clicks))