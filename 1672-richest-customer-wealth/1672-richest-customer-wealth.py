class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(nums) for nums in accounts ])