
'''
Reverse Bits - Reverse bits of a given 32 bits unsigned integer.

for each n and with 1 and shift >>. 
Take the bit gotten from anding with 1 and xor with the reserve value which is initially 0. 
Before Xor shift the bit << by the correct amount.
'''



def reverseBits(n):
    
    reverse = 0
    for i in range(32):
        bit  = n & 1
        reverse = reverse ^ (bit<< (31-i) )
        n = n >> 1
        
    return reverse
        
            
            
# 00000010100101000001111010011100
# 00111001011110000010100101000000