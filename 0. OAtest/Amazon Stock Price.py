def stockPrice(price:list, k:int)->int:
    currHave = {}
    for i in range(k-1):
        if price[i] not in currHave:
            currHave[price[i]] = 0
        currHave[price[i]] += 1

    currSum = sum(price[:k-1])
    res = []
    for i in range(k-1,len(price)):
        if price[i] not in currHave:
            currHave[price[i]] = 0
        currHave[price[i]] += 1
        currSum += price[i]

        if len(currHave) == k:
            res += [currSum]
        
        currHave[price[i-k+1]] -= 1
        if currHave[price[i-k+1]] == 0:
            currHave.pop(price[i-k+1])
        currSum -= price[i-k+1]

    ans = max(res) if res else 0
    print(ans)
    return  ans


stockPrice([1,2,7,7,4,3,6], 3)
stockPrice([1,2,7,7,4,3], 3)
stockPrice([1,2,1,1,4,3,6], 2)
stockPrice([1,2,2,1,4,3,6], 3)
stockPrice([1,1,1,1,1,1,1], 4)
stockPrice([7,2,7,7,4,4,6], 4)


from collections import deque 
def max_avg_stock_price(prices, k):     
    if len(prices) < k:         
        return -1     
    max_total = -1     
    cur_window_prices = deque([])     
    cur_total = 0     
    l = 0     
    for r in range(len(prices)):         
        cur_total += prices[r]         
        cur_window_prices.append(prices[r])         
        if r-l == k-1:             
            if len(set(cur_window_prices)) == k:                 
                max_total = max(max_total,cur_total)              
            cur_window_prices.popleft()             
            cur_total -=prices[l]             
            l +=1    
    print(max_total)          
    return max_total          


max_avg_stock_price([1,2,7,7,4,3,6], 3)
max_avg_stock_price([1,2,7,7,4,3], 3)
max_avg_stock_price([1,2,1,1,4,3,6], 2)
max_avg_stock_price([1,2,2,1,4,3,6], 3)
max_avg_stock_price([1,1,1,1,1,1,1], 4)
max_avg_stock_price([7,2,7,7,4,4,6], 4)