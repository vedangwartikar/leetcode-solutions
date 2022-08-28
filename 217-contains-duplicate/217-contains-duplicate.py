class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element_dict = {}
        for each_element in nums:
            if each_element in element_dict:
                return True
            else:
                element_dict[each_element] = None
        return False