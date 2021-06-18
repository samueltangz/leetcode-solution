# Find the MSB of k
def msb(k):
    i = 0
    while (1<<i) <= k:
        i += 1
    return i
'''
msb(1) = 1
msb(2) = 2
msb(3) = 2
'''

# Bits 2, 4, 8, ... are 1's (separator) -- one indexed
def find_kth_bit(k):
    if k == 1: return 0
    
    # Find MSB
    b = msb(k)
    # They are bit 2^b for b>0
    if k == 2**(b-1): return 1
    
    # "k = 2^b + u" is refering bit "2^b - u", but inverted
    u = k - 2**(b-1)
    return 1 - find_kth_bit(2**(b-1) - u)

    
class Solution:
    # k is one-indexed
    def findKthBit(self, _: int, k: int) -> str:
        return str(find_kth_bit(k))