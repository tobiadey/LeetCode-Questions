'''
Search in Rotated Sorted Array - Given the sorted rotated array nums of unique elements,
return the minimum element of this array.

at most two sorted halfs, 
mid will be apart of left sorted or right sorted, 
if target is in range of sorted portion then search it, 
otherwise search other half

'''
# Time: O(log n) and Space: O(1)
# Runtime: 45 ms
# Memory Usage: 14.2 MB


def search(nums, target):
    '''
    search(): List -> int -> int
    '''

    _l,_r= 0, len(nums)-1
    _m =  (_l+_r)//2


    if not nums:
        return -1

    while _l<= _r:
        _m =  (_l+_r)//2

        if nums[_m] == target:
            return _m


        # lhs is incresing
        if nums[_m] >= nums[_l]:

            if nums[_l] <= target and target < nums[_m]:
                # search lhs
                _r = _m-1
            else:
                _l = _l+1

        # rhs is increasing
        else:
            if nums[_r] >= target and target > nums[_m]:
                # search rhs
                _l = _l+1
            else:
                _r = _m-1

        # elif target > nums[m] and target >= nums[l]:
        #     # search lhs
        #     r = m -1
        # elif target > nums[m] and target <= nums[l]:
        #     # search rhs
        #     l = m +1
        # elif target < nums[m] and target >= nums[l]:
        #     # search lhs
        #     r = m -1
        # elif target < nums[m] and target <= nums[l]:
        #     # search rhs
        #     l = m +1
    return -1
