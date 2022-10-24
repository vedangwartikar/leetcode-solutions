class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]        
        long_start, long_end = 0, 0
        
        for i in range(n):
            dp[i][i] = True
            long_start, long_end = i, i+1
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                long_start, long_end = i, i+2
        
        for k in range(3, n+1, 1):
            for start in range(0, n-k+1, 1):
                end = start + k - 1
                if s[start] == s[end] and dp[start+1][end-1] == True:
                    dp[start][end] = True
                    long_start, long_end = start, end+1

        return s[long_start: long_end]