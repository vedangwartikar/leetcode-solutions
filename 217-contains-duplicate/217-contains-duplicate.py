class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Create a dictionary for storing the array elements (initially the dictionary will be empty). Traverse through the array and if the element exists in the dictionary return True, else add the element in the dictionary. Return False if the entire array is traversed
        
        element_dict = {}
        for each_element in nums:
            if each_element in element_dict:
                return True
            else:
                element_dict[each_element] = None
        return False