'''
Best Time to Buy and Sell Stock - choose a single day to buy one stock
and choose a different day in the future to sell that stock.

# Time: O(n) and Space: O(1)
# Runtime: 1451 ms
# Memory Usage: 24.6 MB
'''

def max_profit(prices):
    '''
    max_profit: list -> int
    '''
    _max_profit, min_buy = 0,float('inf')

    for price in prices:
        if price < min_buy:
            min_buy = price

        profit = price - min_buy
        if profit > _max_profit:
            _max_profit = profit

    return _max_profit



INPUT_LIST = [2,7,4,2]
print(max_profit(INPUT_LIST))
