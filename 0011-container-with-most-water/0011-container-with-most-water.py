class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(min(height[left], height[right]) * (right - left), max_area)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area