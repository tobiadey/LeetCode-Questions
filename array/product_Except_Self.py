'''
Product of Array Except Self

loop forward (caluclating prefix)
loop backwards (calculating suffix)
multiply prefix and suffix in same index
'''


# Time: O(n) and Space: O(1) 
# Runtime: 734 ms
# Memory Usage: 21.3 MB

def productExceptSelf(nums):

    dynamiclist = [1]*len(nums)
    
    
    pre = 1
    for x in range(len(nums)):
        dynamiclist[x] = pre
        pre = pre * nums[x]
    
    
    suff= 1
    for x in range(len(nums)-1, -1, -1):
        dynamiclist[x] = dynamiclist[x] * suff
        suff = suff * nums[x]
        
    return dynamiclist


# Time: O(n) and Space: O(1) 
# Runtime: 244 ms ms 
# Memory Usage: 21.2 MB
def productExceptSelf2(nums):
    
    dynamiclist = []
    
    pre = 1
    for x in nums:
        dynamiclist.append(pre)
        pre *= x
    
    suff= 1
    for x in range(len(nums)-1, -1, -1):
        dynamiclist[x] *= suff
        suff *= nums[x]
        
    return dynamiclist


'''
Print result
'''
list = [-1,-1,0,-3,3]
print(productExceptSelf2(list))

