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
            
            //get all elements from left to right
            for(i = left; i < right; i++) {
                spiral.push_back(matrix[top][i]);
            }
            top += 1;
            
            for (i = top; i < bottom; i++) {
                spiral.push_back(matrix[i][right - 1]);
            }
            right -= 1;
                
            if (!(left < right && top < bottom)) {
                break;
            }
                
            for (i = right - 1; i > left - 1; i--) {
                spiral.push_back(matrix[bottom - 1][i]);
            }
            bottom -= 1;
            
            for (i = bottom - 1; i > top - 1; i--) {
                spiral.push_back(matrix[i][left]);
            }
            left += 1;
        }
        return spiral;
    }
};