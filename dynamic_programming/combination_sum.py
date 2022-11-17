'''
Question: Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Solution:
'''

# Time: O(2^t) and Space: O(n)
# Runtime: 155 ms, faster than 33.61%
# Memory Usage: 14 MB, less than 30.49%
def combinationSum(candidates,target):
    res = []
    def dfs(i,curr,total):
        if total == target:
            res.append(curr.copy())
            return
        
        if i >= len(candidates) or total>target:
            return 
        
        curr.append(candidates[i])
        dfs(i,curr,total+candidates[i])
        curr.pop()
        dfs(i+1,curr,total)
        
        
    dfs(0,[],0)
    return res

INPUT_LIST = [1,2,5]
print(combinationSum(INPUT_LIST,K)) #output ?
