class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_subarray = nums[0];
        int current_sum = 0;
        for (auto element: nums) {
            if (current_sum < 0) {
                current_sum = 0;
            }
            current_sum += element;
            max_subarray = max(max_subarray, current_sum);
        }
        return max_subarray;
    }
};