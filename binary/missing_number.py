'''
Missing Number- Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Create a new list containing all the numbers, and subtract the sum of both individual lists.
'''

def missingNumber(nums):
    
    lst = list(range(0,len(nums)+1))
    
    ans = sum(lst) - sum(nums)

    return ans