class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0, mid = 0, high = nums.size() - 1;
        int temp = 0;
        while (mid <= high) {
            if (nums[mid] == 0) {
                temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low += 1;
                mid += 1;
            }
            else if (nums[mid] == 1) {
                mid += 1;
            }
            else { // element == 2
                temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high -= 1;
            }
        }
    }
};