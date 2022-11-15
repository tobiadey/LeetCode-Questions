'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

# Time: O(n) and Space: O(n)
# Runtime: 63 ms
# Memory Usage: 13.9 MB
def spiralOrder(matrix):

    '''
    List -> List
    '''
    # time - O(n*m)
    # space - O(1)
    
    left, right = 0,len(matrix[0]) #row /x
    top, bottom = 0,len(matrix)  #colums/ y
    res = []

    
    while left <right and top < bottom:
        
        #loop -> 
        for i in range(left,right):
            res.append(matrix[top][i])
        top += 1
        
        # loop down
        for i in range(top,bottom):
            res.append(matrix[i][right-1])
        right -=1
        
        # handle single columns or rows 
        if not (left < right and top < bottom):
            break

        # loop <-
        for i in range(right-1,left-1,-1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        
        # loop ^
        for i in range(bottom-1,top-1,-1):
            res.append(matrix[i][left])
        left +=1
        
    return res

INPUT_LIST= [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(INPUT_LIST)) #output [1,2,3,6,9,8,7,4,5]
