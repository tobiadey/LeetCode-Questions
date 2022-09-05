'''
Best Time to Buy and Sell Stock
'''

# Brute force - Time: O(n) and Space: O(1) 
# Runtime: 1451 ms
# Memory Usage: 24.6 MB
def maxProfit(prices):
    maxProfit, minBuy = 0,float('inf')  

    for price in prices:
        if price < minBuy:
            minBuy = price
            
        profit = price - minBuy
        if profit > maxProfit:
            maxProfit = profit
            
    return maxProfit
                

'''
Print result
'''
list = [2,7,4,2]
print(maxProfit(list))




