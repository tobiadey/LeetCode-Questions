'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

# Time: O(nlogm) and Space: O(1)
# Runtime: 54 ms, faster than 82.87%
# Memory Usage: 14.5 MB, less than 44.18%
def searchMatrix(matrix,target):
    '''
    compare the target with the range of each row to find row
    then perform binary search on the row to find the target

    '''
    
    # find the row O(m)
    for i in range(len(matrix)):
        if (matrix[i][0]) <= target and (matrix[i][-1]) >= target:
            l,r = 0,len(matrix[i])-1
            if matrix[i][l] == target or matrix[i][r] == target:
                return True
            while l < r:
                mid = 1+(l+r)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            
            return False

INPUT_LIST= [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
TARGET = 13
print(getIntersectionNode(INPUT_LIST,TARGET)) #output False

