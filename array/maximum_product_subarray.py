'''
Given an integer array nums,
find a contiguous non-empty subarray within the array that has the largest product,
and return the product.

# Time: O(n) and Space: O(1)
# Runtime: 92 ms
# Memory Usage: 14.4 MB
'''

def max_product(nums):
    '''
    Max Product Function: List -> Int
    '''
    max_product_value = nums[0]
    curr_max_product, curr_min_product = nums[0],nums[0]

    for num in nums[1:]:
        temp_value = curr_max_product * num
        curr_max_product = max(num, curr_max_product * num, curr_min_product * num )
        curr_min_product = min(num, temp_value, curr_min_product * num,curr_min_product * num)
        max_product_value  = max (curr_max_product, curr_min_product,max_product_value )

    return max_product_value


INPUT_LIST = [-2,1,-3,4,-1,2,1,-5,4]
print(max_product(INPUT_LIST))
