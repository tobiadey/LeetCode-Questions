'''
Two Sum
use hash map to instantly check for difference value, 
map will add index of last occurrence of a num, 
don’t use same element twice;
'''

# Brute force - Time: O(n*n) and Space: O(1) 
# Runtime: 4464 ms 
# Memory Usage: 15 MB
def twoSum(nums, target):
    # find the correct indexes
    for x in range(len(nums)):
        # only check after x as we've seen all values before x previously
        for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target and x!=y:
                    return [x,y]


# Hash Map - Time: O(n) and Space: O(1) 
# Runtime: 110 ms
# Memory Usage: 15.1 MB
def twoSum2(nums, target):
    dict = {}
    # find the correct indexes
    for i, val in enumerate(nums):

        # check if (target - val) exists in dict
        bal = target - val

        # check if key exist
        if bal in dict:
            return [dict[bal], i]
        dict[val] = i
                

'''
Print result
'''
list = [2,7,4,2]
target= 4
print(twoSum2(list,target))




