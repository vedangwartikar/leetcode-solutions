"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node):
        
        if node in self.old_to_new:
            return self.old_to_new[node]
        
        copy = Node(node.val)
        self.old_to_new[node] = copy
        
        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor))
        
        return copy
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.old_to_new = {}
        return self.dfs(node) if node else node