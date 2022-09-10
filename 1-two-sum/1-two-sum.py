class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, j in enumerate(nums):
            if j in dict:
                return [dict[j], i]
            else:
                dict[target - j] = i
                