'''
Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
You cant rob 2 adjacent houses.
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

DP problem using bottoms up approach - 
as the last 2 houses only have a max sum of their actual value
as they have no adjacent house after that meet requirement.
'''


# Time: O(n^2) and Space: O(n)
# Runtime: 59 ms
# Memory Usage: 13.8 MB
def rob(nums):
    
    n = len(nums)
    dp = [*nums]

    maximimum = 0

    for i in range(len(nums)-3,-1,-1):
        maximum = 0
        for j in range(i+2,len(nums)):
            maximum = max(maximum, dp[j])
            dp[i] = nums[i] + maximum


    return max(dp)

INPUT_LIST = [4,3,1,2] 
print(rob(INPUT_LIST)) #output 4


# Time: O(n) and Space: O(1)
# Runtime: 59 ms
# Memory Usage: 13.8 MB
'''
Since we are only keeping tract of 2 values then we can just update these as we go on
'''
def rob2(nums):
    _rob1,_rob2 = 0,0
    
    #[rob1,rob2,n,n+1,n+2...]
    for x in nums:
        temp = max(x+rob1,rob2)
        _rob1=_rob2
        _rob2 = temp
    return _rob2

INPUT_LIST = [4,3,1,2] 
print(rob2(INPUT_LIST)) #output 4