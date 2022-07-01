class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # aka Dutch National Flag
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            # if element at mid is 0: swap element at low and mid; increment low and mid
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # if element at mid is 1: increment mid
            elif nums[mid] == 1:
                mid += 1
            # if element at mid is 2: swap element at mid and high; increment high
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        