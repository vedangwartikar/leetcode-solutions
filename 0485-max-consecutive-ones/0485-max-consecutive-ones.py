"""
Keep and increment a count whenever there is a 1
Set max_count to count if it is greater than the current local count
If a 0 is encountered, set the local count back to 0
Return the max_count in the end
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_count = 0, 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0
        return max_count