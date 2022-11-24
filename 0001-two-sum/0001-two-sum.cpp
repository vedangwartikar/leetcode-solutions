class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> map; // create a hashmap
        for(int i = 0; i < nums.size(); i++) { // iterate through all elements and their indexes
            if (map.find(nums[i]) != map.end()) { // if the element is found in hashmap
                return {map[nums[i]], i}; // return its value from hashmap and its current index
            }
            else { 
                map[target - nums[i]] = i; // else add its counterpart int the hashmap (target - value): index
            }
        }
        return {};
    }
};