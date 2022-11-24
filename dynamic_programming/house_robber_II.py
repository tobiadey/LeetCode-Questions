'''
Question: Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
All houses at this place are arranged in a circle - That means the first house is the neighbor of the last one. 
two adjacent houses cant be robbed
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Solution:
Perfom house robber I on a slice of the arrays. arr1 = remove first index arr2= remove last index arr3= only first index
'''


# Time: O(n) and Space: O(m+k+o) where m,k and o are the size of the sub arrays
# Runtime:  28 ms, faster than 98.49%
# Memory Usage: 13.9 MB, less than 72.44%
def rob(nums):
    
    def help(arr):
        rob1,rob2 = 0,0
        for x in arr:
            temp = max(rob1+x,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


    #remove first index and remove last index and get the max also with first index as     
    #array length can be of size 1 [4]
    res = max(help(nums[1:]),help(nums[:-1]),nums[0]) 

    return res
            

# Time: O(n) and Space: O(m+k+o) where m,k and o are the size of the sub arrays
# Runtime: 63 ms, faster than 40.58%
# Memory Usage: 13.9 MB, less than 72.44%
'''
Since we are only keeping tract of 2 values then we can just update these as we go on
'''
def rob2(nums):
    return max(self.helper(nums[1:]),self.helper(nums[:-1]),nums[0]) 
    
def helper(self,arr):
    rob1,rob2 = 0,0
    for x in arr:
        temp = max(rob1+x,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
        
            
        
INPUT_LIST = [1,2,3,1]
print(rob(INPUT_LIST)) #output 4
print(rob2(INPUT_LIST)) #output 4