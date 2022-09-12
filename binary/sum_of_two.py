'''
Sum of Two Integers - If x and y don’t have set bits at same position(s), 
then bitwise XOR (^) of x and y gives the sum of x and y. 
To incorporate common set bits also, bitwise AND (&) is used. Bitwise AND of x and y gives all carry bits. We calculate (x & y) << 1 and add it to x ^ y to get the required result. 

'''

def getSum(self, a: int, b: int) -> int:

    mask = 0xffffffff # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
    while (b & mask) > 0:
        
        carry = (a & b) << 1
        a = a ^ b
        b = carry


    return (a & mask) if b > 0 else a


 # Note the final check, if b = 0 that means the carry bit 'finished', but when there is a negative number ( like -1), the carry bit will continue until it exceeds our 32 bit mask ( to end while loop ) it wont be 0 so in that case we use the mask.