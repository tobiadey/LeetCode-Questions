'''
how many distinct ways can you climb to the top of a staircase with n steps where you can only take 1 or 2 steps?
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

bottom-up: compute the last 2 numbers n and n-1 which are 1 and 1 then work from there for find (n- 2) -> (n-n)
'''

# Time: O(n) and Space: O(n)
# Runtime: 60 ms
# Memory Usage: 13.8 MB
def climbStairs(n):
    '''
    Takes extra space climbStairs2 is mpre efficient
    '''
    dp = [0]*(n+1)
    dp[-1] = 1
    dp[-2] = 1
    
    for i in range(len(dp)-3,-1,-1):
        dp[i] = dp[i+1]+dp[i+2]
    
    
    return dp[0]

n = 5
print(climbStairs(n)) #output 8

# Time: O(n) and Space: O(1)
# Runtime: 51 ms
# Memory Usage: 13.8 MB
def climbStairs2(n):
    one,two=1,1
    
    for i in range(n-1):
        temp = one
        one = one+two 
        two = temp
    
    return one

n = 5
print(mclimbStairs2(n)) #output 8
