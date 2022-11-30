class Solution {
public:
    int vec_max(vector<int>& a) {return *max_element(a.begin(), a.end());}
    
    int maxProduct(vector<int>& nums) {
        int current_max = 1; // define current max as 1 (neutral number for *)
        int current_min = 1; // define current min as 1 (neutral number for *)
        int result = vec_max(nums); // define result as the current vector max
        
        for (auto element: nums) { // iterate through each element
            if (element == 0) { // if element is 0
                current_max = 1; // reset the current max
                current_min = 1; // reset the current min
                continue; // no need to compute max/min
            }
            int temp_max = element * current_max; // precomute temp because current_max gets altered in the next step and needs to be used for current_min
            current_max = max(max(element * current_max, element * current_min), element); // max of element, with positive max, negative max
            current_min = min(min(temp_max, element * current_min), element); // min of element, with positive max, negative max
            result = max(result, current_max); // update result with the max value till now
        }
        
        return result; // return result
    }
};