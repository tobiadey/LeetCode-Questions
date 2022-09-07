'''
maximum_subarray - Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

check if half of array is sorted in order to find pivot,
arr is guaranteed to be in at most two sorted subarrays
'''

# Time: O(n) and Space: O(1)
# Runtime: 761 ms
# Memory Usage: 28.5 MB

def max_sub_array(nums):
    '''
    max_sub_array(): List -> Int
    '''

    max_value = nums[0]
    curr = nums[0]

    for num in nums[1:]:
        if curr < 0:
            curr = 0

        curr += num
        max_value = max(curr,max_value)

    return max_value

INPUT_LIST = [2,3,-2,4]
print(max_sub_array(INPUT_LIST))
