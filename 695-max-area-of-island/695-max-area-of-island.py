"""
Same as numOfIslands() but while traversing keep a track of dfs '1' counts and return int accordingly -> 1 + up + down + right + left, else return 0
Finally in matrix traversal return max (global_count, dfs())
"""
class Solution:
    max_counter = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.max_counter = max(self.max_counter, self.dfs(grid, i, j))
        return self.max_counter
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        right = self.dfs(grid, i+1, j)
        down = self.dfs(grid, i, j+1)
        left = self.dfs(grid, i-1, j)
        up  = self.dfs(grid, i, j-1)
        return 1 + right + down + left + up