'''
Counting Bits - Given an integer n, 
return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
'''

def countBits(n):
    
    
    offset = 1
    ans = [0] * (n+1)
    for i in range(0,n+1): 
        

        if (offset * 2 == i):
            offset = offset * 2
            
        if i == 0:
            ans[i] = 0
        else:
            ans[i] = 1 + ans[i - offset]

        # print(i,offset)
    return ans