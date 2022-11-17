'''
Question: Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Input: m = 3, n = 7
Output: 28

Solution: dfs + memoization or iteratively calculating each row checking values at bottom + right
'''

# Time: O(n) and Space: O(n)
# Runtime: 72 ms, faster than 11.89%
# Memory Usage: 14.3 MB, less than 6.43% 
def uniquePaths(m,n):
    '''
    dfs + memoization
    '''
    arr = [0]
    dp = {}

        
    def dfs(i,j):
        if (j,i) == (m,n):
            arr[0] +=1
            return 1
        if (j,i) in dp:
            return dp[(j,i)]
        
        if i>n or j>m:
            return 0
        
        dp[(j,i)] = dfs(i+1,j) + dfs(i,j+1)

        return dp[(j,i)]
            
    
    return dfs(1,1)

# Time: O(?) and Space: O(?)
# Runtime: ?
# Memory Usage: ?
def uniquePaths2(m,n):  
    '''

    '''
    return 1

M =3
N = 2
print(uniquePaths(M,N)) #output 3
