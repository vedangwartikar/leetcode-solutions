class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector <int> spiral;
        int left = 0;
        int right = matrix[0].size();
        int top = 0;
        int bottom = matrix.size();
        
        while (left < right && top < bottom) {
            int i;
            
            // get all elements from left to right
            for(i = left; i < right; i++) {
                spiral.push_back(matrix[top][i]);
            }
            top += 1;
            
            // get all elements from top to bottom
            for (i = top; i < bottom; i++) {
                spiral.push_back(matrix[i][right - 1]);
            }
            right -= 1;
            
            // break incase the pointers cross
            if (!(left < right && top < bottom)) {
                break;
            }
            
            //get all elements from right to left
            for (i = right - 1; i > left - 1; i--) {
                spiral.push_back(matrix[bottom - 1][i]);
            }
            bottom -= 1;
            
            // get all elements from bottom to top
            for (i = bottom - 1; i > top - 1; i--) {
                spiral.push_back(matrix[i][left]);
            }
            left += 1;
        }
        return spiral;
    }
};