class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        low, high = 0, len(nums) - 1
        while low <= high:
            if abs(nums[low]) >= abs(nums[high]):
                res.append(nums[low] ** 2)
                low += 1
            else:
                res.append(nums[high] ** 2)
                high -= 1
        return res[::-1]