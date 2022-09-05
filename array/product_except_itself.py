'''
Product of Array Except Self- Given an integer array nums,
return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].

loop forward (caluclating prefix) and loop backwards (calculating suffix)
multiply prefix and suffix in same index
'''


# Time: O(n) and Space: O(1)
# Runtime: 734 ms
# Memory Usage: 21.3 MB

def product_except_self_old(nums):
    '''
    product_except_self_old: List -> List
    '''
    dynamiclist = [1]*len(nums)

    pre = 1
    # for x in range(len(nums)):
    for _x, val in enumerate(nums):
        dynamiclist[_x] = pre
        pre = pre * val

    suff= 1
    for _x in range(len(nums)-1, -1, -1):
        dynamiclist[_x] = dynamiclist[_x] * suff
        suff = suff * nums[_x]

    return dynamiclist


# Time: O(n) and Space: O(1)
# Runtime: 244 ms ms
# Memory Usage: 21.2 MB
def product_except_self(nums):
    '''
    product_except_self_old: List -> List
    '''
    dynamiclist = []
    pre = 1

    for _x in nums:
        dynamiclist.append(pre)
        pre *= _x

    suff= 1
    for _x in range(len(nums)-1, -1, -1):
        dynamiclist[_x] *= suff
        suff *= nums[_x]

    return dynamiclist



INPUT_LIST = [-1,-1,0,-3,3]
print(product_except_self(INPUT_LIST))
