class Solution:
    """
    Check if the last bit is 1 using n % 2, if it is then increment the counter by 1 (n % 2 itself works)
    Right shift the bits of n by using pythonic syntax n >> 1
    Do this till n becomes 0 i.e no bits left to shift
    """
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2
            n = n >> 1
        return result