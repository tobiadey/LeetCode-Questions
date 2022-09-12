'''
Number of 1 Bits - function takes an unsigned integer and 
returns the number of '1' bits it has (also known as the Hamming weight).

while number is not 0, continiously and with 1, then shift >> 
each time the return value is 1 increament counter.
'''

def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        if (n & 1):count += 1
            
        n = n >> 1
    return count