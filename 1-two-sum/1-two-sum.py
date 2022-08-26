class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict and i != dict[nums[i]]:
                return [i, dict[nums[i]]]
            dict[target - nums[i]] = i