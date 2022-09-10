class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XORing of all the numbers will result in the only element that exists by itself
        Note: XOR of a number with itself returns 0
        """
        x = 0
        for i in nums:
            x = x ^ i
        return x