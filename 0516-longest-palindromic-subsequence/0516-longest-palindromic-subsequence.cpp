class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size(); // string size
        vector <vector <int>> dp(n, vector<int>(n, 0)); // initialize dp grid with 0s
        for (int i = n-1; i >= 0; i--) { // get all indexes above the diagonal
            dp[i][i] = 1; // each alphabet with itself makes a palindrome
            for (int j = i + 1; j < n; j++) { // for loops such that we get indexes 23 12 13 01 02 03
                if (s[i] == s[j]) { // if the characters match
                    dp[i][j] = dp[i+1][j-1] + 2; // increment dp[i][j] with the count of alphabets matched (2)
                }
                else {
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]); // else it is max of the previous strings
                }
            }
        }
        return dp[0][n-1]; // result is always present at the top right corner
    }
};