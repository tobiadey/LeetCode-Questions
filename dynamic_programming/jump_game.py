'''
Question: You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Solution: 
1- Greedy bottom up approach, dp[-1] is true and is the initial end goal(nums[-1]), keep updating dp[i] and end varibale as see fit
'''

# Time: O(n) and Space: O(n)
# Runtime: 877 ms, faster than 70.67%
# Memory Usage: 15.6 MB, less than 5.57%
def canJump(nums):
    n = len(nums)
    dp = [False]*n
    dp[-1] = True
    end = n-1 
        
    for i in range(n-2,-1,-1):
        if nums[i] + i >= end:
            dp[i] = True
            end = i
        else:
            dp[i]=False
    
    return dp[0]

# Time: O(n) and Space: O(1)
# Runtime: 736 ms, faster than 74.74% 
# Memory Usage: 15.2 MB, less than 49.22%
def canJump2(nums):
    n = len(nums)
    end = n-1 
        
    for i in range(n-2,-1,-1):
        if nums[i] + i >= end:
            end = i
    
    return True if end == 0 else False

INPUT_LIST = [2,3,1,1,4]
print(canJump(INPUT_LIST)) #output True
print(canJump2(INPUT_LIST)) #output True
