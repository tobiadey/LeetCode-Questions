'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

each index counts as its own subsequence, 
find all possible subsequence for each value
solving from rhs as nums[-1] only has 1 subsequence
use this to calculate the rest
'''

# Time: O(n^2) and Space: O(n)
# Runtime: 7098 ms
# Memory Usage: 14.3 MB
def lengthOfLIS(nums):  # O(n^2) 
    dp = [1]*len(nums)
    
    for i in range(len(nums)-1,-1,-1):
        for j in range(i,len(nums)):
            if nums[i]<nums[j]:
                dp[i] = max(dp[i],1+dp[j])


    # print(dp)
    
    return max(dp)

INPUT_LIST = [1,2,4,3] 
print(lengthOfLIS(INPUT_LIST)) #output 3