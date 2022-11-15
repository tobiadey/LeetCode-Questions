'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

111    101
101 -> 000
111    101
'''

# Time: O(n*m) and Space: O(1)
# Runtime: 310 ms, faster than 41.72% 
# Memory Usage: 14.8 MB, less than 16.63% 
def setZeroes(matrix):
"""
Do not return anything, modify matrix in-place instead.
"""
    rows,columns = len(matrix),len(matrix[0])
    rowZero = False
    
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                matrix[0][c]= 0
                
                if r > 0:
                    matrix[r][0]=0
                else:
                    rowZero = True
                
    for r in range(1,rows):
        for c in range(1,columns):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c]=0
    
    if matrix[0][0]==0:
        for r in range(rows):
            matrix[r][0] = 0
        
    if rowZero == True:
        for c in range(columns):
            matrix[0][c] = 0
        

    return matrix

INPUT_LIST= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(INPUT_LIST)) #output [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
