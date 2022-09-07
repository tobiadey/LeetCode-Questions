'''
Find Minimum in Rotated Sorted Array - Given the sorted rotated array nums of unique elements,
return the minimum element of this array.

Binary search while comparing mid point to the value at the left and right. 
'''

# Time: O(log n) and Space: O(1)
# Runtime: 45 ms
# Memory Usage: 14.1 MB
def find_min(nums):
    '''
    find_min(): List -> Int
    '''
    _l,_r = 0, len(nums)-1

    while _l < _r:
        _m = (_l+_r) //2

        if nums[_m] > nums[_r]:
            # search right
            _l = _m +1
        else:
            # search left
            _r= _m

    return nums[_r]

INPUT_LIST = [3,4,5,1,2]
print(find_min(INPUT_LIST))
