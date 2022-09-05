'''
Contains Duplicates - Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Hash map- Using hash map to check if a value has been stored as a key
Compare length-  Using a set to get unique vlaues then comparing length to original list
'''


# Time: O(n) and Space: O(1)
# Runtime: 816 ms
# Memory Usage: 25.8 MB
def contains_duplicate_old(nums):
    '''
    contains_duplicate: List -> Boolean
    '''
    storage = {}
    for val in nums:
        # check if value exists in dict (a duplicate)
        if val in storage:
            return True
        else:
            storage[val] = val
    return False


# Set - Time: O(1) and Space: O(1) as set operation in pyton is implemented as hashtables
# Runtime: 472 ms
# Memory Usage: 25.9 MB
def contains_duplicate(nums):
    '''
    contains_duplicate: List -> Boolean
    '''
    return len(set(nums)) != len(nums)



INPUT_LIST = [2,7,4,2]
print(contains_duplicate(INPUT_LIST))
