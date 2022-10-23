"""
Create a hashmap old_to_new to main the key: value as old_node: new_node
Traverse the nodes using dfs, if the old is already in the hashmap return its new node else create a copy and add it to the hashmap
For each neighbor of the old node, append the dfs(neighbor) to copy's neighbor
O(V+E)
"""

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