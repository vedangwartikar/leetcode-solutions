class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = nums[0]; // max subarray sum is initially the first element
        int current_sum = 0; // initialize the current sum to 0
        for (auto element: nums) { // for each element
            if (current_sum < 0) { // if the current sum goes negative
                current_sum = 0; // reset the current sum to 0 (exclude the negative numbers locally)
            }
            current_sum += element; // update the current sum with the current element
            max_sum = max(max_sum, current_sum); // check if newly computed sum is greater than max sum
        }
        return max_sum; // return the max sum
    }
};