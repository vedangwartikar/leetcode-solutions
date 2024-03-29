"""
Create a directed graph and store the a/b values as a->b as value and b->a as 1/value
Recursively using DFS, traverse nodes to find the path using the logic a/c = a/b * b/c and store the values accordingly
Create a resultant list and ad values for each path and return the resultant list
"""
class Solution:
    def dfs(self, source, value):
        if source == self.destination:
            return value
        for adjacent, adjacent_value in self.graph[source].items():
            if adjacent not in self.seen:
                self.seen.add(adjacent)
                result = self.dfs(adjacent, value*adjacent_value)
                if result != -1:
                    return result
                self.seen.remove(adjacent)
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:        
        self.graph = defaultdict(dict)
        self.seen = set()
        
        for (source, destination), value in zip(equations, values):
            self.graph[source][destination] = value
            self.graph[destination][source] = 1/value
        
        query_result = []
        for source, self.destination in queries:
            query_result.append(self.dfs(source, 1) if source in self.graph else -1)
            self.seen.clear()
        return query_result