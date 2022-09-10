class Solution:
    """
    Traverse through the grid, if 1 is found - increment the count and call DFS()
    Return back if the indexes are invalid or the grid element is 0
    Else mark the current grid element as 0 and do DFS (horizontal and vertical) on the adjacent elements
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, grid)
        return count
    
    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i > len(grid) - 1 or j  > len(grid[0]) - 1 or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(i + 1, j, grid)
        self.dfs(i, j + 1, grid)
        self.dfs(i, j - 1, grid)
        self.dfs(i - 1, j, grid)