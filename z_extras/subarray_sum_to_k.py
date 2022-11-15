'''
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2


Brute force approach: find all possible sub arrays and find all the ones that sum up to k
Brute force approach: O(n^2)time & O(n)space

Prefix sum approach: store the sums of each subarray in prefix sum and find out if current sum -k is in prefix sum hashmap.
Prefix sum approach: O(n)time & O(n)space
https://www.youtube.com/watch?v=fFVZt-6sgyo
'''

# Time: O(n) and Space: O(n)
# Runtime: 757 ms, faster than 41.23%
# Memory Usage: 16.6 MB, less than 75.36%
def subarraySum(nums,k):
    n = len(nums)
    prefix_sum = {0:1}
    _sum = 0
    res = 0
    
    for i in range(n):
        _sum += nums[i]
        diff = _sum -k
        res += prefix_sum.get(diff,0)
        prefix_sum[_sum] = 1 + prefix_sum.get(_sum,0)

            
    return res

INPUT_LIST= [1,2,3]
k = 3
print(subarraySum(INPUT_LIST,k)) #output 2
