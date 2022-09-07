'''
Two Sum - Find two values that together with the index form a container,
such that the container contains the most water.

shrinking window,
left/right initially at endpoints,
shift the pointer with min height.
'''

# Time: O(n) and Space: O(1)
# Runtime: 1120 ms
# Memory Usage: 27.4 MB

def max_area(height):
    '''
    max_area(): List -> Int
    '''
    _l, _r, _max_area = 0, len(height)-1, 0

    while _l < _r:
        curr_area = (_r - _l) * min(height[_l], height[_r])
        _max_area = max (curr_area, _max_area)

        if height[_l] > height[_r]:            
            _r -= 1
        else:
            _l += 1

    return _max_area

INPUT_LIST = [1,8,6,2,5,4,8,3,7]  #expected output 49
print(max_area(INPUT_LIST))
