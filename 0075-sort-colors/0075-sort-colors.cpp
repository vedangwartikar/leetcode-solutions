class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0, mid = 0, high = nums.size() - 1;
        int temp = 0;
        while (mid <= high) {
            if (nums[mid] == 0) { // if element is 0, swap low - mid and increment low and mid
                swap(nums[low], nums[mid]);
                low += 1;
                mid += 1;
            }
            else if (nums[mid] == 1) { // if element is 1, increment mid
                mid += 1;
            }
            else { // if element is 2, swap mid - high and decrement high
                swap(nums[mid], nums[high]);
                high -= 1;
            }
        }
    }
};