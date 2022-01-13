class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maximum = -10001
        for i in nums:
            total += i
            maximum = total if total > maximum else maximum 
            total = 0 if total < 0 else total
        return maximum