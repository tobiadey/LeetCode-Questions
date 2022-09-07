'''
Two Sum - Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Brute Force - Use 2 loops. Try allpossible values until they add up to the target
Hash Map - Single loop. Hashing each value (before hashing check if the difference exists)
'''

# Brute force - Time: O(n*n) and Space: O(1)
# Runtime: 4464 ms
# Memory Usage: 15 MB
def two_sum_old(nums,_target):
    '''
    two_sum: list, target -> list
    '''
    # find the correct indexes
    for _x, val1 in enumerate(nums):
        # only check after x as we've seen all values before x previously
        for _y, val2 in enumerate(nums):
            if val1 + val2 == _target and _x!=_y:
                return [_x,_y]


# Hash Map - Time: O(n) and Space: O(1)
# Runtime: 110 ms
# Memory Usage: 15.1 MB
def two_sum(nums, _target):
    '''
    two_sum: list, target -> list
    '''
    storage = {}
    # find the correct indexes
    for i, val in enumerate(nums):

        # check if (target - val) exists in dict
        bal = _target - val

        # check if key exist
        if bal in storage:
            return [storage[bal], i]
        storage[val] = i


INPUT_LIST = [2,7,4,2]
_TARGET= 4
print(two_sum(INPUT_LIST,_TARGET))
