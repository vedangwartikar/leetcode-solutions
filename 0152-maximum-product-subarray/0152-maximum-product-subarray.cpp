class Solution {
public:
    int vec_max(vector<int>& a) {return *max_element(a.begin(), a.end());}
    
    int maxProduct(vector<int>& nums) {
        int current_max = 1;
        int current_min = 1;
        int result = vec_max(nums);
        
        for (auto element: nums) {
            if (element == 0) {
                current_max = 1;
                current_min = 1;
                continue;
            }
            int temp_max = element * current_max;
            current_max = max(max(element * current_max, element * current_min), element);
            current_min = min(min(temp_max, element * current_min), element);
            result = max(result, current_max);
        }
        
        return result;
    }
};