class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int i, result = 0;
        for (i = 0; i < nums.size(); i++) {
            result ^= i;
            result ^= nums[i];
            // cout << i << " " << nums[i] << "\n";
        }
        result ^= i;
        return result;
    }
};