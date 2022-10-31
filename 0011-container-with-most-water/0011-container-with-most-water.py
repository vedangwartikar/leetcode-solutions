class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[right] > height[left]:
                left += 1
                max_area = max(min(height[left], height[right]) * (right - left), max_area)
            else:
                right -= 1
                max_area = max(min(height[left], height[right]) * (right - left), max_area)
        return max_area