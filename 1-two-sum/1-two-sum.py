class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        create a dict to store target - current element. 
        first, if the current element has the counterpart in the dict, return the indexes
        else add the target - current element to the dict
        O(n)
        """
        dict = {}
        for i, j in enumerate(nums):
            if j in dict:
                return [dict[j], i]
            else:
                dict[target - j] = i
                