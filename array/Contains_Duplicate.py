


# Hash Map - Time: O(n) and Space: O(1) 
# Runtime: 816 ms
# Memory Usage: 25.8 MB
def containsDuplicate(nums):
    dict = {}
    for val in nums:
        # check if value exists in dict (a duplicate)
        if val in dict:
            return True
        else:
            dict[val] = val
    return False
        

# Set - Time: O(1) and Space: O(1) as set operation in pyton is implemented as hashtables
# Runtime: 472 ms
# Memory Usage: 25.9 MB
def containsDuplicate2(nums):
    return len(set(nums)) != len(nums)


'''
Print result
'''
list = [2,7,4,2]
print(containsDuplicate2(list))

