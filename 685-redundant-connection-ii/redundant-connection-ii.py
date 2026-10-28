class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        
        edge1 = None
        edge2 = None
        
        # Step 1: Check for any node with two parents
        for u, v in edges:
            if parent[v] != 0:
                # Node v has two parents: parent[v] and u
                edge1 = [parent[v], v]
                edge2 = [u, v]
                break
            parent[v] = u
            
        # Step 2: Use Union-Find to process edges and look for cycles
        uf = UnionFind(n)
        for u, v in edges:
            # If this is edge2 (the second incoming edge to a node), skip it temporarily
            if edge2 and [u, v] == edge2:
                continue
                
            # If union returns False, a cycle is detected
            if not uf.union(u, v):
                # If there were two parents, then edge1 must be part of the cycle
                if edge1:
                    return edge1
                # If no duplicate parent exists, this edge creates the cycle
                return [u, v]
                
        # If no cycle was found after skipping edge2, edge2 is the redundant one
        return edge2
