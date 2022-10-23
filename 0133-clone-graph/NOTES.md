Create a hashmap old_to_new to main the key: value as old_node: new_node
Traverse the nodes using dfs, if the old is already in the hashmap return its new node else create a copy and add it to the hashmap
For each neighbor of the old node, append the dfs(neighbor) to copy's neighbor
​
O(V+E)