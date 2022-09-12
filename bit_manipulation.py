'''
Bit manipulation cheatsheet
'''


'''bit operators'''

# And (&)
def is_even(n):
    if n & 1: 
        return 1
    else:
        return 0
