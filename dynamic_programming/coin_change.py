'''
coin change - given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Bottom up solution:
Solve for number of coins it will take for coin of value 1-amount

top-down: recursive dfs, for amount, branch for each coin, cache to store prev coin_count for each amount; 
bottom-up: compute coins for amount = 1, up until n, using for each coin (amount - coin), cache prev values
'''

# Time: O(amount*coins) and Space: O(amount)
# Runtime: 1621 ms
# Memory Usage: 14.2 MB

def coinChange(coins, amount):
    n = len(coins)
    dp = [float('inf')] * (amount+1)
    dp[0]=0
    
    for i in range(1,amount+1):
        for c in coins:
            if i-c >=0:
                dp[i]= min(dp[i], 1+dp[i-c])
        
    return dp[amount] if dp[amount] != float('inf') else -1

INPUT_LIST = [1,2,5]
K = 11
print(coinChange(INPUT_LIST,K)) #output 3
