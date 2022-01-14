class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_sum_for_max = 0
        max_sum = -sys.maxsize
        
        curr_sum_for_min = 0
        min_sum = sys.maxsize
        
        total_sum = 0
        
        for i in nums:
            curr_sum_for_max += i
            max_sum = max(curr_sum_for_max, max_sum)
            curr_sum_for_max = 0 if curr_sum_for_max < 0 else curr_sum_for_max
            
            curr_sum_for_min += i
            min_sum = min(curr_sum_for_min, min_sum)
            curr_sum_for_min = 0 if curr_sum_for_min > 0 else curr_sum_for_min
            
            total_sum += i
        
        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        return max_sum